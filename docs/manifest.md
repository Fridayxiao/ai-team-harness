# Harness Manifest

Date captured: 2026-06-29

## Custom Skills From `/Users/david/.codex/skills`

| Skill | Source Path |
|---|---|
| `clarify-and-reuse` | `/Users/david/.codex/skills/clarify-and-reuse` |
| `musk-5-step` | `/Users/david/.codex/skills/musk-5-step` |
| `reuse-opportunity-review` | `/Users/david/.codex/skills/reuse-opportunity-review` |
| `set-goal` | `/Users/david/.codex/skills/set-goal` |
| `write-handoff` | `/Users/david/.codex/skills/write-handoff` |

## Custom Skills From `/Users/david/.agents/skills`

| Skill | Source Path |
|---|---|
| `codebase-design` | `/Users/david/.agents/skills/codebase-design` |
| `diagnosing-bugs` | `/Users/david/.agents/skills/diagnosing-bugs` |
| `domain-modeling` | `/Users/david/.agents/skills/domain-modeling` |
| `grill-with-docs` | `/Users/david/.agents/skills/grill-with-docs` |
| `grilling` | `/Users/david/.agents/skills/grilling` |
| `improve-codebase-architecture` | `/Users/david/.agents/skills/improve-codebase-architecture` |
| `prototype` | `/Users/david/.agents/skills/prototype` |
| `setup-matt-pocock-skills` | `/Users/david/.agents/skills/setup-matt-pocock-skills` |
| `tdd` | `/Users/david/.agents/skills/tdd` |
| `to-issues` | `/Users/david/.agents/skills/to-issues` |
| `to-prd` | `/Users/david/.agents/skills/to-prd` |

## Retained Upstream And Legacy Skills

| Skill | Source Path |
|---|---|
| `brainstorming` | `/Users/david/.codex/plugins/cache/openai-curated/superpowers/3fdeeb49/skills/brainstorming` |
| `receiving-code-review` | `/Users/david/.codex/plugins/cache/openai-curated/superpowers/3fdeeb49/skills/receiving-code-review` |
| `verification-before-completion` | `/Users/david/.codex/plugins/cache/openai-curated/superpowers/3fdeeb49/skills/verification-before-completion` |

## Personal Plugins

| Plugin | Source Path |
|---|---|
| `orchestrated-delivery` | `/Users/david/.codex/plugins/cache/personal/orchestrated-delivery/0.4.0` |

## Agents

| Agent | File |
|---|---|
| `architect` | `agents/architect.toml` |
| `bug-reproducer` | `agents/bug-reproducer.toml` |
| `code-reviewer` | `agents/code-reviewer.toml` |
| `docs-maintainer` | `agents/docs-maintainer.toml` |
| `docs-researcher` | `agents/docs-researcher.toml` |
| `product-designer` | `agents/product-designer.toml` |
| `security-auditor` | `agents/security-auditor.toml` |
| `test-engineer` | `agents/test-engineer.toml` |

## Portability Notes

- The copied skills are self-contained directories.
- Custom skill sync excludes `.system`, `_archive`, upstream plugin cache directories, and Cloudflare-published skills unless explicitly listed as retained.
- The harness does not depend on the original source paths after copying.
- The install script defaults to `~/.agents/skills` so multiple agent tools can consume the same skill directory.
- Agent TOML files are Codex-specific and should be copied to a Codex agents directory when used.
