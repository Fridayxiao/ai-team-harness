---
name: langchain-langgraph-docs-guide
description: "Verify official LangChain, LangGraph, Deep Agents, and LangSmith docs before implementation and provide API guidance with citations. Mandatory first step is read domain-specific first-check pages and capture migration or deprecation impact before opening other reference pages. Use when building features, debugging integration issues, upgrading versions, or implementing LangSmith platform workflows where exact API names, params, and imports must be confirmed. Workflow is identify task domain (Deep Agents, LangChain, LangGraph, integrations, foundations, or LangSmith), complete first-check pages first, choose the smallest relevant reference file from references/00-catalog-index.md, fetch only required official URLs, and answer with citations and migration notes."
---

# LangChain LangGraph Docs Guide

## What This Skill Does

- Verify API usage against official Deep Agents, LangChain, LangGraph, and LangSmith docs before implementation.
- Reduce errors from outdated memory, guessed imports, or wrong parameter names.
- Produce implementation-ready answers with source citations and migration awareness.

## When To Use This Skill

Use this skill when correctness depends on current official documentation, especially for:

- Building new agent or tool workflows with Deep Agents, LangChain, or LangGraph in Python or JavaScript.
- Debugging integration or runtime issues caused by uncertain API names, parameters, imports, or auth setup.
- Planning or executing version upgrades and migration work.
- Implementing LangSmith tracing, evaluation, deployment, or platform API tasks.

## Quick Workflow

1. Identify the target domain first: Deep Agents, LangChain, LangGraph, Integrations, LangSmith platform, or shared foundations.
2. Mandatory gate: open the domain first-check pages first (from the routing map below) before any other doc pages.
3. Record release-impact notes first: version scope, deprecations, and breaking-change implications.
4. Choose the smallest relevant shard (a focused reference file) via `references/00-catalog-index.md`.
5. Copy URL strings exactly from the selected skill references before fetching docs.
6. Open only the official URLs required for the task and verify concrete API names, params, constraints, and deprecations.
7. Implement or answer using verified details and include citations.
8. Before final output, recheck release or migration pages if recommendations could be version-sensitive.

## Scenario Routing Map (Task-First)

- Deep Agents
  - JavaScript: `references/31-oss-javascript-deep-agents.md`
  - Python: `references/41-oss-python-deep-agents.md`
  - Start with: overview, quickstart, customization, harness/subagents/skills before niche pages.
- LangChain
  - JavaScript: `references/32-oss-javascript-langchain.md`, `references/34-oss-javascript-integrations.md`
  - Python: `references/42-oss-python-langchain.md`, `references/44-oss-python-integrations.md`
  - Priority order requirement: Overview, Quickstart, Agents, Models, Messages, Tools, Runtime, Middleware, Structured output, Multi-agent.
- LangGraph
  - JavaScript: `references/33-oss-javascript-langgraph.md`
  - Python: `references/43-oss-python-langgraph.md`
  - Start with: overview, quickstart, install, graph API, functional API, runtime/persistence.
- Shared foundations (only when request is cross-framework or not product-specific)
  - JavaScript: `references/30-oss-javascript-foundations.md`
  - Python: `references/40-oss-python-foundations.md`
  - Typical use: product choice, shared concepts, common errors, contributing docs.
- LangSmith platform APIs and operations
  - Primary references: `references/10-api-auth-and-deployments.md`, `references/11-api-platform-infra.md`, `references/20-langsmith-agent-server-api.md`, `references/21-langsmith-agent-build-and-serving.md`, `references/22-langsmith-eval-observability-and-quality.md`, `references/23-langsmith-deploy-and-self-host.md`, `references/24-langsmith-ops-security-and-admin.md`
  - Mandatory first check (before any other docs): [LangSmith docs home](https://docs.langchain.com/langsmith/home.md), [LangSmith Agent Server API](https://docs.langchain.com/langsmith/server-api-ref.md), [LangSmith Control Plane API](https://docs.langchain.com/langsmith/api-ref-control-plane.md)
- Catalog entry point
  - Use `references/00-catalog-index.md` to pick the minimal reference file set.
  - Use `references/00-global-index-and-misc.md` only if no domain file covers the request.

## Mandatory First-Check Pages (By Language)

- Python OSS tasks (Deep Agents, LangChain, LangGraph, foundations, integrations): [LangChain v1 release notes](https://docs.langchain.com/oss/python/releases/langchain-v1.md), [LangGraph v1 release notes](https://docs.langchain.com/oss/python/releases/langgraph-v1.md)
- JavaScript OSS tasks (Deep Agents, LangChain, LangGraph, foundations, integrations): [LangChain JS v1 release notes](https://docs.langchain.com/oss/javascript/releases/langchain-v1.md), [LangGraph JS v1 release notes](https://docs.langchain.com/oss/javascript/releases/langgraph-v1.md)

## Output Requirements

- Start with a short "Release Check" summary that lists release URLs used and key migration/deprecation impact.
- Cite every fetched official URL used to justify recommendations.
- Call out migration and deprecation impact when relevant.
- If multiple valid paths exist, provide a concise trade-off and recommend a default.
- If required docs cannot be fetched, stop and report blockers instead of giving memory-only API guidance.

## Source Rules

- Treat fetched pages from `https://docs.langchain.com` and linked official references as source of truth.
- Use only official domains for factual API guidance: `docs.langchain.com` and `reference.langchain.com`.
- Always complete release-notes review before relying on reference/API pages for implementation guidance.
- Treat local `references/*.md` files as routing indexes, not final API truth.
- Apply strict URL matching: use the exact URL text from skill references and mandatory first-check lists.
- Never add, remove, or rewrite URL suffixes (including `.md`), trailing slashes, query parameters, or fragments.
- If an exact URL cannot be fetched, report the exact URL as blocked and stop instead of trying a rewritten variant.

## If Docs Cannot Be Reached

1. State that missing documentation blocks reliable completion.
2. If release notes are missing, stop immediately and report that release-first policy cannot be satisfied.
3. List the exact missing URL(s) and why each is required.
4. Provide next steps: retry fetch, provide a reachable official URL, or restore network access.
5. Do not provide final implementation advice based only on memory.

## Advanced References

- Implementation defaults and selection guidance: `references/90-implementation-defaults.md`
- Catalog maintenance and refresh operations: `references/91-maintenance.md`
- Raw catalog source: `references/llms.txt`
- Refresh helper script: `scripts/refresh_catalog.py`
