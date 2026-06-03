# Harness Manifest

Date captured: 2026-06-03

## Skills (Flat Namespace)

| Skill | Source Path |
|---|---|
| `automation-opportunity-review` | `/Users/david/.codex/skills/automation-opportunity-review` |
| `brainstorming` | `/Users/david/.gemini/antigravity/skills/brainstorming` |
| `clarify-and-reuse` | `/Users/david/.codex/skills/clarify-and-reuse` |
| `diagnose` | `/Users/david/.agents/skills/diagnose` |
| `executing-plans` | `/Users/david/.gemini/antigravity/skills/executing-plans` |
| `finishing-a-development-branch` | `/Users/david/.gemini/antigravity/skills/finishing-a-development-branch` |
| `grill-with-docs` | `/Users/david/.agents/skills/grill-with-docs` |
| `improve-codebase-architecture` | `/Users/david/.agents/skills/improve-codebase-architecture` |
| `musk-5-step` | `/Users/david/.codex/skills/musk-5-step` |
| `prototype` | `/Users/david/.agents/skills/prototype` |
| `receiving-code-review` | `/Users/david/.gemini/antigravity/skills/receiving-code-review` |
| `tdd` | `/Users/david/.agents/skills/tdd` |
| `to-prd` | `/Users/david/.agents/skills/to-prd` |
| `using-superpowers` | `/Users/david/.gemini/antigravity/skills/using-superpowers` |
| `verification-before-completion` | `/Users/david/.gemini/antigravity/skills/verification-before-completion` |
| `write-handoff` | `/Users/david/.codex/skills/write-handoff` |
| `writing-plans` | `/Users/david/.gemini/antigravity/skills/writing-plans` |
| `zoom-out` | `/Users/david/.agents/skills/zoom-out` |

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
- The harness does not depend on the original source paths after copying.
- The install script defaults to `~/.agents/skills` so multiple agent tools can consume the same skill directory.
- Agent TOML files are Codex-specific and should be copied to a Codex agents directory when used.
