#!/usr/bin/env bash
set -euo pipefail

HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

expected_skills=(
  "skills/animation-vocabulary"
  "skills/clarify-and-reuse"
  "skills/code-review"
  "skills/codebase-design"
  "skills/delivery-loop"
  "skills/design-taste-frontend"
  "skills/diagnosing-bugs"
  "skills/domain-modeling"
  "skills/emil-design-eng"
  "skills/grill-with-docs"
  "skills/grilling"
  "skills/idea2implement"
  "skills/improve-codebase-architecture"
  "skills/musk-5-step"
  "skills/prototype"
  "skills/receiving-code-review"
  "skills/redesign-existing-projects"
  "skills/reuse-opportunity-review"
  "skills/review-animations"
  "skills/set-goal"
  "skills/setup-matt-pocock-skills"
  "skills/tdd"
  "skills/to-spec"
  "skills/to-tickets"
  "skills/verification-before-completion"
  "skills/web-design-guidelines"
  "skills/write-handoff"
)

expected_docs=(
  "README.md"
  "docs/manifest.md"
  "licenses/mattpocock-skills-MIT.txt"
)

expected_skill_metadata=(
  "skills/code-review/agents/openai.yaml"
  "skills/prototype/agents/openai.yaml"
  "skills/setup-matt-pocock-skills/agents/openai.yaml"
  "skills/tdd/agents/openai.yaml"
  "skills/to-spec/agents/openai.yaml"
  "skills/to-tickets/agents/openai.yaml"
)

removed_skills=(
  "skills/to-issues"
  "skills/to-prd"
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
  skill_file="$HARNESS_DIR/$skill/SKILL.md"
  if [ ! -f "$skill_file" ]; then
    printf 'missing skill: %s\n' "$skill" >&2
    missing=1
    continue
  fi

  skill_name="${skill#skills/}"
  declared_name="$(sed -n 's/^name:[[:space:]]*//p' "$skill_file" | head -n 1)"
  declared_name="${declared_name#\"}"
  declared_name="${declared_name%\"}"
  declared_name="${declared_name#\'}"
  declared_name="${declared_name%\'}"
  if [ "$declared_name" != "$skill_name" ]; then
    printf 'skill name mismatch: %s declares %s\n' "$skill" "$declared_name" >&2
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

for doc in "${expected_docs[@]}"; do
  if [ ! -f "$HARNESS_DIR/$doc" ]; then
    printf 'missing documentation: %s\n' "$doc" >&2
    missing=1
  fi
done

for metadata in "${expected_skill_metadata[@]}"; do
  if [ ! -f "$HARNESS_DIR/$metadata" ]; then
    printf 'missing skill metadata: %s\n' "$metadata" >&2
    missing=1
    continue
  fi

  skill_dir="${metadata%/agents/openai.yaml}"
  skill_name="${skill_dir#skills/}"
  default_prompt="$(sed -n 's/^[[:space:]]*default_prompt:[[:space:]]*//p' "$HARNESS_DIR/$metadata" | head -n 1)"
  if [[ "$default_prompt" != *"\$$skill_name"* ]]; then
    printf 'skill metadata prompt does not reference $%s: %s\n' "$skill_name" "$metadata" >&2
    missing=1
  fi
done

for skill in "${removed_skills[@]}"; do
  if [ -f "$HARNESS_DIR/$skill/SKILL.md" ]; then
    printf 'stale renamed skill: %s\n' "$skill" >&2
    missing=1
  fi
done

for legacy_name in "to-issues" "to-prd"; do
  if grep -R -Fq "$legacy_name" "$HARNESS_DIR/skills"; then
    printf 'stale operational skill reference: %s\n' "$legacy_name" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

printf 'harness ok: %s skills, %s plugin files, %s agents\n' "${#expected_skills[@]}" "${#expected_plugins[@]}" "${#expected_agents[@]}"
