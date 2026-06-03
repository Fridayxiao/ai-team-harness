# AI Team Harness

Portable harness for sharing one curated skill set and one Codex sub-agent team across machines, projects, and agent environments.

## Contents

- `skills/`: portable copies of selected reusable skills (currently in a flat namespace).
- `agents/`: the 8 Codex sub-agent TOML files.
- `docs/manifest.md`: source paths and intended use.
- `scripts/install-global-skills.sh`: copy skills into a user-level skills directory.
- `scripts/verify-harness.sh`: check that the expected skills and agents exist.

## Core Skills

This harness intentionally includes only broadly reusable skills:

- `diagnose`
- `tdd`
- `prototype`
- `zoom-out`
- `grill-with-docs`
- `improve-codebase-architecture`
- `to-prd`
- `brainstorming`
- `executing-plans`
- `finishing-a-development-branch`
- `receiving-code-review`
- `using-superpowers`
- `verification-before-completion`
- `write-handoff`
- `writing-plans`
- `automation-opportunity-review`
- `clarify-and-reuse`
- `musk-5-step`

## Agent Team

The `agents/` directory contains:

- `architect`
- `bug-reproducer`
- `code-reviewer`
- `docs-maintainer`
- `docs-researcher`
- `product-designer`
- `security-auditor`
- `test-engineer`

## Install

From this directory:

```bash
./scripts/verify-harness.sh
./scripts/install-global-skills.sh
```

By default, the install script copies all skills to:

```text
~/.agents/skills
```

Override the target:

```bash
SKILLS_HOME="$HOME/.codex/skills" ./scripts/install-global-skills.sh
```

The script copies files rather than symlinking them, so the installed skills remain usable after moving the harness.

Install script behavior:

- Skips entries in `skills/` that are not actual skill directories (must contain `SKILL.md`).
- Replaces any existing target directory with the freshly copied one.
- Prints an `installed N skills...` summary after completion.
