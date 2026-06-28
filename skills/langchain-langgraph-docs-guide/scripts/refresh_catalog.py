#!/usr/bin/env python3
"""
Build sharded markdown references from LangChain's llms.txt catalog.

Usage:
  uv run scripts/refresh_catalog.py
  uv run scripts/refresh_catalog.py --source references/llms.txt --out-dir references
"""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


ENTRY_RE = re.compile(r"^- \[(.*?)\]\((https?://[^)]+)\)(?::\s*(.*))?$")


@dataclass(frozen=True)
class ShardSpec:
    key: str
    filename: str
    title: str
    use_when: str
    scope: str
    domain: str


SHARDS: list[ShardSpec] = [
    ShardSpec(
        key="00-global-index-and-misc",
        filename="00-global-index-and-misc.md",
        title="Global Index And Misc",
        use_when="Need top-level landing/index pages or uncategorized docs.",
        scope="Root pages like docs index and uncommon paths outside major families.",
        domain="global",
    ),
    ShardSpec(
        key="10-api-auth-and-deployments",
        filename="10-api-auth-and-deployments.md",
        title="API Reference Auth And Deployments",
        use_when="Working on OAuth provider flows or deployment CRUD/revisions.",
        scope="`/api-reference/auth-service-v2/*` and `/api-reference/deployments-v2/*`.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="11-api-platform-infra",
        filename="11-api-platform-infra.md",
        title="API Reference Platform Infra",
        use_when="Working on integrations, listeners, sandboxes, pools, templates, volumes.",
        scope="`/api-reference/integrations-v1/*`, `/listeners-v2/*`, `/sandboxes-v2/*`.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="20-langsmith-agent-server-api",
        filename="20-langsmith-agent-server-api.md",
        title="LangSmith Agent Server API",
        use_when="Implementing or debugging Agent Server endpoints and server-side runtime APIs.",
        scope="`/langsmith/agent-server-api/*` including assistants, threads, runs, MCP, A2A.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="21-langsmith-agent-build-and-serving",
        filename="21-langsmith-agent-build-and-serving.md",
        title="LangSmith Agent Build And Serving",
        use_when="Building/publishing agents or understanding serving entrypoints and remote graph usage.",
        scope="`/langsmith/agent-builder*`, `/langsmith/agent-server*`, `/langsmith/server-*`, `/langsmith/remote-graph*`.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="22-langsmith-eval-observability-and-quality",
        filename="22-langsmith-eval-observability-and-quality.md",
        title="LangSmith Eval Observability And Quality",
        use_when="Designing evaluation pipelines, tracing, prompt iteration, dataset/feedback quality loops.",
        scope="LangSmith pages containing evaluation, experiment, trace, observability, prompt, dataset, feedback, insights, studio.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="23-langsmith-deploy-and-self-host",
        filename="23-langsmith-deploy-and-self-host.md",
        title="LangSmith Deploy And Self Host",
        use_when="Deploying LangSmith/LangGraph infrastructure or configuring self-hosted setups.",
        scope="LangSmith pages with deploy, deployment, self-host, Kubernetes, Docker, Cloud/Hybrid, control/data plane, scaling.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="24-langsmith-ops-security-and-admin",
        filename="24-langsmith-ops-security-and-admin.md",
        title="LangSmith Ops Security And Admin",
        use_when="Handling platform operations, governance, auth/access, billing, org/workspace administration.",
        scope="Remaining non-API LangSmith docs not matched by other LangSmith shards.",
        domain="langsmith-platform",
    ),
    ShardSpec(
        key="30-oss-javascript-foundations",
        filename="30-oss-javascript-foundations.md",
        title="OSS JavaScript Foundations",
        use_when="Reading shared OSS JavaScript concepts that are not specific to Deep Agents, LangChain, or LangGraph.",
        scope="`/oss/javascript/common-errors.md`, `/oss/javascript/concepts/*`, `/oss/javascript/contributing/*` and other shared pages.",
        domain="foundations",
    ),
    ShardSpec(
        key="31-oss-javascript-deep-agents",
        filename="31-oss-javascript-deep-agents.md",
        title="OSS JavaScript Deep Agents",
        use_when="Building or debugging Deep Agents in JavaScript/TypeScript.",
        scope="`/oss/javascript/deepagents/*`.",
        domain="deep-agents",
    ),
    ShardSpec(
        key="32-oss-javascript-langchain",
        filename="32-oss-javascript-langchain.md",
        title="OSS JavaScript LangChain",
        use_when="Building or debugging LangChain JavaScript/TypeScript application logic.",
        scope="`/oss/javascript/langchain/*` with core topics prioritized first.",
        domain="langchain",
    ),
    ShardSpec(
        key="33-oss-javascript-langgraph",
        filename="33-oss-javascript-langgraph.md",
        title="OSS JavaScript LangGraph",
        use_when="Building or debugging LangGraph JavaScript/TypeScript graphs and runtime behavior.",
        scope="`/oss/javascript/langgraph/*`.",
        domain="langgraph",
    ),
    ShardSpec(
        key="34-oss-javascript-integrations",
        filename="34-oss-javascript-integrations.md",
        title="OSS JavaScript Integrations",
        use_when="Selecting and wiring JS/TS providers, chat models, embeddings, retrievers, vector stores, and tools.",
        scope="`/oss/javascript/integrations/*`.",
        domain="langchain",
    ),
    ShardSpec(
        key="40-oss-python-foundations",
        filename="40-oss-python-foundations.md",
        title="OSS Python Foundations",
        use_when="Reading shared OSS Python concepts that are not specific to Deep Agents, LangChain, or LangGraph.",
        scope="`/oss/python/common-errors.md`, `/oss/python/concepts/*`, `/oss/python/contributing/*` and other shared pages.",
        domain="foundations",
    ),
    ShardSpec(
        key="41-oss-python-deep-agents",
        filename="41-oss-python-deep-agents.md",
        title="OSS Python Deep Agents",
        use_when="Building or debugging Deep Agents in Python.",
        scope="`/oss/python/deepagents/*`.",
        domain="deep-agents",
    ),
    ShardSpec(
        key="42-oss-python-langchain",
        filename="42-oss-python-langchain.md",
        title="OSS Python LangChain",
        use_when="Building or debugging LangChain Python application logic.",
        scope="`/oss/python/langchain/*` with core topics prioritized first.",
        domain="langchain",
    ),
    ShardSpec(
        key="43-oss-python-langgraph",
        filename="43-oss-python-langgraph.md",
        title="OSS Python LangGraph",
        use_when="Building or debugging LangGraph Python graphs and runtime behavior.",
        scope="`/oss/python/langgraph/*`.",
        domain="langgraph",
    ),
    ShardSpec(
        key="44-oss-python-integrations",
        filename="44-oss-python-integrations.md",
        title="OSS Python Integrations",
        use_when="Selecting and wiring Python providers, chat models, embeddings, retrievers, vector stores, and tools.",
        scope="`/oss/python/integrations/*`.",
        domain="langchain",
    ),
]

SHARD_BY_KEY = {shard.key: shard for shard in SHARDS}

LANGSMITH_EVAL_KEYWORDS = (
    "evaluation",
    "evaluator",
    "evaluate",
    "experiment",
    "trace",
    "tracing",
    "observability",
    "prompt",
    "dataset",
    "feedback",
    "insights",
    "studio",
)

LANGSMITH_DEPLOY_KEYWORDS = (
    "deploy",
    "deployment",
    "self-host",
    "kubernetes",
    "docker",
    "cloud",
    "hybrid",
    "control-plane",
    "data-plane",
    "components",
    "scale",
    "upgrades",
    "ingress",
    "external-",
    "collector",
)

SHARD_DISPLAY_GROUPS: list[tuple[str, list[str]]] = [
    ("Global Entry Points", ["00-global-index-and-misc"]),
    (
        "LangSmith Platform",
        [
            "10-api-auth-and-deployments",
            "11-api-platform-infra",
            "20-langsmith-agent-server-api",
            "21-langsmith-agent-build-and-serving",
            "22-langsmith-eval-observability-and-quality",
            "23-langsmith-deploy-and-self-host",
            "24-langsmith-ops-security-and-admin",
        ],
    ),
    (
        "Deep Agents",
        ["31-oss-javascript-deep-agents", "41-oss-python-deep-agents"],
    ),
    (
        "LangChain",
        [
            "32-oss-javascript-langchain",
            "34-oss-javascript-integrations",
            "42-oss-python-langchain",
            "44-oss-python-integrations",
        ],
    ),
    (
        "LangGraph",
        ["33-oss-javascript-langgraph", "43-oss-python-langgraph"],
    ),
    (
        "Shared Foundations",
        ["30-oss-javascript-foundations", "40-oss-python-foundations"],
    ),
]

SHARD_PRIORITY_RULES: dict[str, tuple[str, ...]] = {
    "30-oss-javascript-foundations": (
        "/concepts/products.md",
        "/common-errors.md",
        "/concepts/context.md",
        "/concepts/memory.md",
    ),
    "40-oss-python-foundations": (
        "/concepts/products.md",
        "/common-errors.md",
        "/concepts/context.md",
        "/concepts/memory.md",
    ),
    "31-oss-javascript-deep-agents": (
        "/deepagents/overview.md",
        "/deepagents/quickstart.md",
        "/deepagents/customization.md",
        "/deepagents/harness.md",
        "/deepagents/subagents.md",
        "/deepagents/skills.md",
        "/deepagents/backends.md",
        "/deepagents/long-term-memory.md",
        "/deepagents/human-in-the-loop.md",
    ),
    "41-oss-python-deep-agents": (
        "/deepagents/overview.md",
        "/deepagents/quickstart.md",
        "/deepagents/customization.md",
        "/deepagents/harness.md",
        "/deepagents/subagents.md",
        "/deepagents/skills.md",
        "/deepagents/backends.md",
        "/deepagents/long-term-memory.md",
        "/deepagents/human-in-the-loop.md",
    ),
    "32-oss-javascript-langchain": (
        "/langchain/overview.md",
        "/langchain/quickstart.md",
        "/langchain/agents.md",
        "/langchain/models.md",
        "/langchain/messages.md",
        "/langchain/tools.md",
        "/langchain/runtime.md",
        "/langchain/middleware/overview.md",
        "/langchain/middleware/built-in.md",
        "/langchain/middleware/custom.md",
        "/langchain/structured-output.md",
        "/langchain/multi-agent/index.md",
        "/langchain/multi-agent/",
    ),
    "42-oss-python-langchain": (
        "/langchain/overview.md",
        "/langchain/quickstart.md",
        "/langchain/agents.md",
        "/langchain/models.md",
        "/langchain/messages.md",
        "/langchain/tools.md",
        "/langchain/runtime.md",
        "/langchain/middleware/overview.md",
        "/langchain/middleware/built-in.md",
        "/langchain/middleware/custom.md",
        "/langchain/structured-output.md",
        "/langchain/multi-agent/index.md",
        "/langchain/multi-agent/",
    ),
    "33-oss-javascript-langgraph": (
        "/langgraph/overview.md",
        "/langgraph/quickstart.md",
        "/langgraph/install.md",
        "/langgraph/graph-api.md",
        "/langgraph/functional-api.md",
        "/langgraph/choosing-apis.md",
        "/langgraph/thinking-in-langgraph.md",
        "/langgraph/durable-execution.md",
        "/langgraph/persistence.md",
        "/langgraph/streaming.md",
        "/langgraph/interrupts.md",
        "/langgraph/pregel.md",
    ),
    "43-oss-python-langgraph": (
        "/langgraph/overview.md",
        "/langgraph/quickstart.md",
        "/langgraph/install.md",
        "/langgraph/graph-api.md",
        "/langgraph/functional-api.md",
        "/langgraph/choosing-apis.md",
        "/langgraph/thinking-in-langgraph.md",
        "/langgraph/durable-execution.md",
        "/langgraph/persistence.md",
        "/langgraph/streaming.md",
        "/langgraph/interrupts.md",
        "/langgraph/pregel.md",
    ),
    "34-oss-javascript-integrations": (
        "/integrations/providers/overview.md",
        "/integrations/providers/all_providers.md",
        "/integrations/chat/index.md",
        "/integrations/tools/index.md",
        "/integrations/text_embedding/index.md",
        "/integrations/retrievers/index.md",
        "/integrations/vectorstores/index.md",
    ),
    "44-oss-python-integrations": (
        "/integrations/providers/overview.md",
        "/integrations/providers/all_providers.md",
        "/integrations/chat/index.md",
        "/integrations/middleware/index.md",
    ),
}


def classify(url: str) -> str:
    path = urlparse(url).path.strip("/")
    if not path or path == "index.md":
        return "00-global-index-and-misc"

    parts = path.split("/")
    if parts[0] == "api-reference":
        second = parts[1] if len(parts) > 1 else ""
        if second in {"auth-service-v2", "deployments-v2"}:
            return "10-api-auth-and-deployments"
        return "11-api-platform-infra"

    if parts[0] == "langsmith":
        rest = "/".join(parts[1:])
        if rest.startswith("agent-server-api/"):
            return "20-langsmith-agent-server-api"
        if (
            rest.startswith("agent-builder")
            or rest.startswith("agent-server")
            or rest.startswith("server-")
            or rest.startswith("remote-graph")
        ):
            return "21-langsmith-agent-build-and-serving"
        if any(token in rest for token in LANGSMITH_EVAL_KEYWORDS):
            return "22-langsmith-eval-observability-and-quality"
        if any(token in rest for token in LANGSMITH_DEPLOY_KEYWORDS):
            return "23-langsmith-deploy-and-self-host"
        return "24-langsmith-ops-security-and-admin"

    if parts[0] == "oss":
        language = parts[1] if len(parts) > 1 else ""
        if language == "javascript":
            if len(parts) > 2 and parts[2] == "integrations":
                return "34-oss-javascript-integrations"
            if len(parts) > 2 and parts[2] == "deepagents":
                return "31-oss-javascript-deep-agents"
            if len(parts) > 2 and parts[2] == "langchain":
                return "32-oss-javascript-langchain"
            if len(parts) > 2 and parts[2] == "langgraph":
                return "33-oss-javascript-langgraph"
            return "30-oss-javascript-foundations"
        if language == "python":
            if len(parts) > 2 and parts[2] == "integrations":
                return "44-oss-python-integrations"
            if len(parts) > 2 and parts[2] == "deepagents":
                return "41-oss-python-deep-agents"
            if len(parts) > 2 and parts[2] == "langchain":
                return "42-oss-python-langchain"
            if len(parts) > 2 and parts[2] == "langgraph":
                return "43-oss-python-langgraph"
            return "40-oss-python-foundations"

    return "00-global-index-and-misc"


def priority_rank(shard_key: str, url: str) -> tuple[int, int]:
    rules = SHARD_PRIORITY_RULES.get(shard_key)
    if not rules:
        return (999, 999)

    path = urlparse(url).path
    for idx, token in enumerate(rules):
        if token.endswith("/") and token in path:
            return (idx, path.count("/"))
        if path.endswith(token):
            return (idx, path.count("/"))
    return (999, 999)


def global_intro_rank(url: str) -> int:
    path = urlparse(url).path.lower()
    if path.endswith("/overview.md"):
        return 0
    if path.endswith("/quickstart.md"):
        return 1
    return 2


def sort_entries_for_shard(shard_key: str, entries: list[dict]) -> list[dict]:
    return sorted(
        entries,
        key=lambda entry: (
            *priority_rank(shard_key, entry["url"]),
            global_intro_rank(entry["url"]),
            entry["title"].lower(),
            entry["url"],
        ),
    )


def parse_entries(source_path: Path) -> list[dict]:
    lines = source_path.read_text(encoding="utf-8").splitlines()
    entries: list[dict] = []
    current: dict | None = None

    for raw_line in lines:
        line = raw_line.rstrip()
        match = ENTRY_RE.match(line.strip())
        if match:
            if current is not None:
                entries.append(current)
            current = {
                "title": match.group(1).strip(),
                "url": match.group(2).strip(),
                "summary": (match.group(3) or "").strip(),
                "details": [],
            }
            continue

        if current is None:
            continue
        current["details"].append(line)

    if current is not None:
        entries.append(current)

    return entries


def normalize_details(raw_details: list[str]) -> list[str]:
    cleaned: list[str] = []
    for item in raw_details:
        stripped = item.strip()
        if not stripped:
            continue
        if stripped == "## Docs":
            continue
        cleaned.append(stripped)
    return cleaned


def normalize_entry_title(title: str, url: str) -> str:
    path = urlparse(url).path
    if title == "Quickstart":
        if "/deepagents/" in path:
            return "Deep Agents Quickstart"
        if "/langchain/" in path:
            return "LangChain Quickstart"
        if "/langgraph/" in path:
            return "LangGraph Quickstart"
    if title == "Overview":
        if path.endswith("/langchain/middleware/overview.md"):
            return "Middleware Overview"
        if path.endswith("/langchain/streaming/overview.md"):
            return "Streaming Overview"
    if title == "Changelog":
        if "/releases/changelog.md" in path:
            return "OSS Releases Changelog"
        if "/langchain/changelog-" in path:
            return "LangChain Changelog"
        if "/langgraph/changelog-" in path:
            return "LangGraph Changelog"
    if title == "Test":
        if "/langchain/test.md" in path:
            return "LangChain Test"
        if "/langgraph/test.md" in path:
            return "LangGraph Test"
    if title == "Frontend" and path.endswith("/langchain/streaming/frontend.md"):
        return "Streaming Frontend"
    if title == "Memory" and path.endswith("/langgraph/add-memory.md"):
        return "Add Memory"
    return title


def write_index(out_dir: Path, grouped: dict[str, list[dict]]) -> None:
    index_path = out_dir / "00-catalog-index.md"
    lines = [
        "# LangChain Docs Catalog Index (Sharded)",
        "",
        "This index is generated from `references/llms.txt`.",
        "Read only the shard that matches the task, then fetch the exact URL(s) you need.",
        "All shards prioritize Overview and Quickstart first when available. LangChain then prioritizes: Agents, Models, Messages, Tools, Runtime, Middleware, Structured output, Multi-agent.",
        "",
    ]
    for group_title, keys in SHARD_DISPLAY_GROUPS:
        lines.extend([f"## {group_title}", ""])
        for key in keys:
            shard = SHARD_BY_KEY[key]
            count = len(grouped.get(shard.key, []))
            lines.extend(
                [
                    f"### {shard.filename}",
                    f"- Entries: {count}",
                    f"- Use when: {shard.use_when}",
                    f"- Scope: {shard.scope}",
                    "",
                ]
            )
    lines.extend(
        [
            "## Refresh",
            "",
            "Run this to regenerate all shard files after updating `llms.txt`:",
            "",
            "```bash",
            "uv run scripts/refresh_catalog.py",
            "```",
            "",
        ]
    )
    index_path.write_text("\n".join(lines), encoding="utf-8")


def core_priority_note(shard_key: str) -> str | None:
    if shard_key in {"32-oss-javascript-langchain", "42-oss-python-langchain"}:
        return "Priority order: Overview -> Quickstart -> Agents -> Models -> Messages -> Tools -> Runtime -> Middleware -> Structured output -> Multi-agent."
    if shard_key in {"31-oss-javascript-deep-agents", "41-oss-python-deep-agents"}:
        return "Priority order: Overview -> Quickstart -> Customization -> Harness -> Subagents -> Skills."
    if shard_key in {"33-oss-javascript-langgraph", "43-oss-python-langgraph"}:
        return "Priority order: Overview -> Quickstart -> Install -> Graph API -> Functional API -> Durable execution -> Persistence."
    return None


def write_shards(out_dir: Path, grouped: dict[str, list[dict]]) -> None:
    for shard in SHARDS:
        entries = sort_entries_for_shard(shard.key, grouped.get(shard.key, []))
        out_path = out_dir / shard.filename
        lines = [
            f"# {shard.title}",
            "",
            f"- Use when: {shard.use_when}",
            f"- Scope: {shard.scope}",
            f"- Total entries: {len(entries)}",
            "",
        ]
        note = core_priority_note(shard.key)
        if note:
            lines.extend([f"- Priority: {note}", ""])
        lines.extend(
            [
            "## Entries",
            "",
            ]
        )
        for idx, entry in enumerate(entries, start=1):
            title = normalize_entry_title(entry["title"], entry["url"])
            lines.append(f"### {idx}. {title}")
            lines.append(f"- URL: {entry['url']}")
            lines.append(f"- Summary: {entry['summary'] if entry['summary'] else '(No one-line summary in source)'}")
            details = normalize_details(entry["details"])
            if details:
                lines.append("- Details:")
                for detail in details:
                    bullet = detail
                    if bullet.startswith("- "):
                        bullet = bullet[2:].strip()
                    lines.append(f"  - {bullet}")
            lines.append("")
        out_path.write_text("\n".join(lines), encoding="utf-8")


def build(source: Path, out_dir: Path) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Source not found: {source}")
    entries = parse_entries(source)
    grouped: dict[str, list[dict]] = defaultdict(list)
    for entry in entries:
        grouped[classify(entry["url"])].append(entry)
    write_index(out_dir, grouped)
    write_shards(out_dir, grouped)


def main() -> int:
    parser = argparse.ArgumentParser(description="Shard LangChain llms.txt into reference markdown files.")
    parser.add_argument("--source", default="references/llms.txt", help="Path to llms.txt")
    parser.add_argument("--out-dir", default="references", help="Output directory for shard markdown")
    args = parser.parse_args()

    source = Path(args.source).resolve()
    out_dir = Path(args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    build(source, out_dir)
    print(f"[OK] Generated shard catalog from {source}")
    print(f"[OK] Output directory: {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
