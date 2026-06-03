#!/usr/bin/env bash
set -euo pipefail

HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

expected_skills=(
  "skills/diagnose"
  "skills/tdd"
  "skills/prototype"
  "skills/zoom-out"
  "skills/grill-with-docs"
  "skills/improve-codebase-architecture"
  "skills/to-prd"
  "skills/brainstorming"
  "skills/executing-plans"
  "skills/finishing-a-development-branch"
  "skills/receiving-code-review"
  "skills/using-superpowers"
  "skills/verification-before-completion"
  "skills/writing-plans"
  "skills/automation-opportunity-review"
  "skills/clarify-and-reuse"
  "skills/musk-5-step"
  "skills/write-handoff"
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

for agent in "${expected_agents[@]}"; do
  if [ ! -f "$HARNESS_DIR/$agent" ]; then
    printf 'missing agent: %s\n' "$agent" >&2
    missing=1
  fi
done

if [ "$missing" -ne 0 ]; then
  exit 1
fi

printf 'harness ok: %s skills, %s agents\n' "${#expected_skills[@]}" "${#expected_agents[@]}"
