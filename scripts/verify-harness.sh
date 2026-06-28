#!/usr/bin/env bash
set -euo pipefail

HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

expected_skills=(
  "skills/automation-opportunity-review"
  "skills/brainstorming"
  "skills/clarify-and-reuse"
  "skills/codebase-design"
  "skills/develop-web-game"
  "skills/diagnosing-bugs"
  "skills/domain-modeling"
  "skills/executing-plans"
  "skills/finishing-a-development-branch"
  "skills/frontend-design"
  "skills/grill-with-docs"
  "skills/grilling"
  "skills/hatch-pet"
  "skills/improve-codebase-architecture"
  "skills/langchain-langgraph-docs-guide"
  "skills/musk-5-step"
  "skills/openai-docs"
  "skills/playwright"
  "skills/prototype"
  "skills/receiving-code-review"
  "skills/set-goal"
  "skills/setup-matt-pocock-skills"
  "skills/tdd"
  "skills/to-issues"
  "skills/to-prd"
  "skills/using-superpowers"
  "skills/verification-before-completion"
  "skills/write-handoff"
  "skills/writing-plans"
  "skills/zoom-out"
)

expected_plugins=(
  "plugins/orchestrated-delivery/.codex-plugin/plugin.json"
  "plugins/orchestrated-delivery/skills/delivery-loop/SKILL.md"
  "plugins/orchestrated-delivery/skills/delivery-loop/agents/openai.yaml"
  "plugins/orchestrated-delivery/skills/codex-thread-manager/SKILL.md"
  "plugins/orchestrated-delivery/skills/codex-thread-manager/agents/openai.yaml"
)

expected_agents=(
  "agents/architect.toml"
  "agents/bug-reproducer.toml"
  "agents/code-reviewer.toml"
  "agents/docs-maintainer.toml"
  "agents/docs-researcher.toml"
  "agents/product-designer.toml"
  "agents/security-auditor.toml"
  "agents/test-engineer.toml"
)

missing=0

for skill in "${expected_skills[@]}"; do
  if [ ! -f "$HARNESS_DIR/$skill/SKILL.md" ]; then
    printf 'missing skill: %s\n' "$skill" >&2
    missing=1
  fi
done

for plugin_file in "${expected_plugins[@]}"; do
  if [ ! -f "$HARNESS_DIR/$plugin_file" ]; then
    printf 'missing plugin file: %s\n' "$plugin_file" >&2
    missing=1
  fi
done

for agent in "${expected_agents[@]}"; do
  if [ ! -f "$HARNESS_DIR/$agent" ]; then
    printf 'missing agent: %s\n' "$agent" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

printf 'harness ok: %s skills, %s plugin files, %s agents\n' "${#expected_skills[@]}" "${#expected_plugins[@]}" "${#expected_agents[@]}"
