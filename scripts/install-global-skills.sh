#!/usr/bin/env bash
set -euo pipefail

HARNESS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILLS_HOME="${SKILLS_HOME:-$HOME/.agents/skills}"

mkdir -p "$SKILLS_HOME"

count=0
for skill_dir in "$HARNESS_DIR/skills"/*; do
  [ -d "$skill_dir" ] || continue
  [ -f "$skill_dir/SKILL.md" ] || continue
  skill_name="$(basename "$skill_dir")"
  target="$SKILLS_HOME/$skill_name"
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
  printf 'installed %s -> %s\n' "$skill_name" "$target"
  count=$((count + 1))
done

printf 'installed %s skills to %s\n' "$count" "$SKILLS_HOME"
