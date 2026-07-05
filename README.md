# AI Team Harness

Portable harness for sharing David's custom skills, selected retained upstream skills, and one Codex sub-agent team across machines, projects, and agent environments.

## Contents

- `skills/`: portable copies of custom and retained skills (currently in a flat namespace).
- `agents/`: the 8 Codex sub-agent TOML files.
- `plugins/`: portable Codex plugins that bundle related skills and plugin metadata.
- `docs/manifest.md`: source paths and intended use.
- `scripts/install-global-skills.sh`: copy skills into a user-level skills directory.
- `scripts/verify-harness.sh`: check that the expected skills and agents exist.

## Custom Skills

The custom skill source is the local user-level directory:

- `/Users/david/.agents/skills`

Current custom skills:

- `clarify-and-reuse`
- `codebase-design`
- `delivery-loop`
- `diagnosing-bugs`
- `domain-modeling`
- `grill-with-docs`
- `grilling`
- `idea2implement`
- `improve-codebase-architecture`
- `musk-5-step`
- `prototype`
- `reuse-opportunity-review`
- `set-goal`
- `setup-matt-pocock-skills`
- `tdd`
- `to-issues`
- `to-prd`
- `write-handoff`

Cloudflare-published skills that may exist under `~/.codex/skills` are intentionally excluded from this harness.

## Retained Skills

The harness also retains selected upstream or legacy skills for portability:

- `delivery-loop`
- `receiving-code-review`
- `verification-before-completion`

## Plugins

- `orchestrated-delivery`: Codex plugin containing `$delivery-loop` and `$codex-thread-manager`.

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

Plugins are stored under `plugins/` as source bundles. Install or refresh them through Codex plugin tooling from the cloned path.

Install script behavior:

- Skips entries in `skills/` that are not actual skill directories (must contain `SKILL.md`).
- Replaces any existing target directory with the freshly copied one.
- Prints an `installed N skills...` summary after completion.
