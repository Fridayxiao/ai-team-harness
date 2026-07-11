# AI Team Harness

Portable harness for sharing David's custom skills, selected and adapted upstream skills, Codex plugins, and one Codex sub-agent team across machines and projects.

## Contents

- `skills/`: portable skill copies in a flat namespace.
- `agents/`: the 8 Codex sub-agent TOML files.
- `plugins/`: portable Codex plugins that bundle related skills and metadata.
- `docs/manifest.md`: exact source lineage, upstream snapshot, and adaptation notes.
- `licenses/`: third-party license notices for adapted skill sources.
- `scripts/install-global-skills.sh`: copy skills into a user-level skills directory.
- `scripts/verify-harness.sh`: check that the expected skills, plugins, and agents exist.

## Skill Catalog

### Local and retained skills

- `animation-vocabulary`
- `clarify-and-reuse`
- `delivery-loop`
- `design-taste-frontend`
- `emil-design-eng`
- `idea2implement`
- `musk-5-step`
- `receiving-code-review`
- `redesign-existing-projects`
- `reuse-opportunity-review`
- `review-animations`
- `set-goal`
- `verification-before-completion`
- `web-design-guidelines`
- `write-handoff`

### Matt Pocock adaptations

The following skills are reconciled with [`mattpocock/skills` v1.1.0](https://github.com/mattpocock/skills/releases/tag/v1.1.0) at commit `d574778f94cf620fcc8ce741584093bc650a61d3`:

- `code-review`
- `codebase-design`
- `diagnosing-bugs`
- `domain-modeling`
- `grill-with-docs`
- `grilling`
- `improve-codebase-architecture`
- `prototype`
- `setup-matt-pocock-skills`
- `tdd`
- `to-spec`
- `to-tickets`

These are semantic adaptations, not a whole-repository mirror. They preserve Codex conventions such as `$skill-name`, `agents/openai.yaml`, local sub-agent review rules, and `$delivery-loop`. The deprecated local names `to-prd` and `to-issues` were removed instead of retained as aliases so invocation remains unambiguous.

See [docs/manifest.md](docs/manifest.md) for per-skill provenance and [the MIT notice](licenses/mattpocock-skills-MIT.txt) for licensing.

Cloudflare-published skills that may exist under `~/.codex/skills` are intentionally excluded.

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

By default, the install script copies every skill to:

```text
~/.agents/skills
```

Override the target when needed:

```bash
SKILLS_HOME="$HOME/.codex/skills" ./scripts/install-global-skills.sh
```

The installer copies files rather than creating symlinks, so installed skills keep working if the harness moves. It replaces an existing target skill with the current harness copy and skips directories without a `SKILL.md`.

Plugins remain source bundles under `plugins/`; install or refresh them through Codex plugin tooling from the cloned path.
