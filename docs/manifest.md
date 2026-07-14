# Harness Manifest

Date captured: 2026-07-09

## Local Source Snapshots

These harness copies originate from local user-level sources or retained local bundles.

| Skill | Source Path |
|---|---|
| `animation-vocabulary` | `/Users/david/.agents/skills/animation-vocabulary` |
| `clarify-and-reuse` | `/Users/david/.agents/skills/clarify-and-reuse` |
| `delivery-loop` | `plugins/orchestrated-delivery/skills/delivery-loop` |
| `design-taste-frontend` | `/Users/david/.agents/skills/design-taste-frontend` |
| `emil-design-eng` | `/Users/david/.agents/skills/emil-design-eng` |
| `idea2implement` | `/Users/david/.agents/skills/idea2implement`, then redesigned for adaptive depth, repeated user-alignment checkpoints, evidence-backed readiness, visibility-aware skill routing, and conditional sub-agent use |
| `musk-5-step` | `/Users/david/.agents/skills/musk-5-step` |
| `redesign-existing-projects` | `/Users/david/.agents/skills/redesign-existing-projects` |
| `reuse-opportunity-review` | `/Users/david/.agents/skills/reuse-opportunity-review` |
| `review-animations` | `/Users/david/.agents/skills/review-animations` |
| `set-goal` | `/Users/david/.agents/skills/set-goal` |
| `web-design-guidelines` | `/Users/david/.agents/skills/web-design-guidelines` |
| `write-handoff` | `/Users/david/.agents/skills/write-handoff` |

## Matt Pocock Upstream Adaptations

Upstream repository: [`mattpocock/skills`](https://github.com/mattpocock/skills)

- Release: [`v1.1.0`](https://github.com/mattpocock/skills/releases/tag/v1.1.0)
- Commit: [`d574778f94cf620fcc8ce741584093bc650a61d3`](https://github.com/mattpocock/skills/commit/d574778f94cf620fcc8ce741584093bc650a61d3)
- License: MIT; retained at `licenses/mattpocock-skills-MIT.txt`

| Harness Skill | Upstream Path | Adaptation Status |
|---|---|---|
| `code-review` | `skills/engineering/code-review` | Added from v1.1.0; adapted to Codex sub-agents, local review verification, and `$setup-matt-pocock-skills`. |
| `codebase-design` | `skills/engineering/codebase-design` | Semantically aligned; Codex UI metadata retained. |
| `diagnosing-bugs` | `skills/engineering/diagnosing-bugs` | Semantically aligned; `$skill` invocation retained. |
| `domain-modeling` | `skills/engineering/domain-modeling` | Semantically aligned; Codex UI metadata retained. |
| `grill-with-docs` | `skills/engineering/grill-with-docs` | Semantically aligned; user-only invocation is represented in `agents/openai.yaml`. |
| `grilling` | `skills/productivity/grilling` | Synced facts-versus-decisions rule and explicit user confirmation gate. |
| `improve-codebase-architecture` | `skills/engineering/improve-codebase-architecture` | Semantically aligned; `$skill` invocation and Codex UI metadata retained. |
| `prototype` | `skills/engineering/prototype` | Synced model-invocation triggers for logic and UI design questions. |
| `setup-matt-pocock-skills` | `skills/engineering/setup-matt-pocock-skills` | Updated renamed skill references and local spec/ticket paths; PR triage and wayfinding operations omitted because those skills are not installed. |
| `tdd` | `skills/engineering/tdd` | Synced red→green reference model, explicit seams, tautological-test rule, and a hard stop-at-green handoff to review; unambiguous existing seams may proceed without a redundant prompt. |
| `to-spec` | `skills/engineering/to-spec` | Renamed from local `to-prd`; adapted to Codex metadata and concise synthesis rules. |
| `to-tickets` | `skills/engineering/to-tickets` | Renamed from local `to-issues`; synced blocking edges, frontier, one-context sizing, and expand–contract wide refactors; delegates execution to `$delivery-loop`. |

### Adaptation Policy

- Keep skill frontmatter portable with only `name` and `description`; represent user-only invocation with `policy.allow_implicit_invocation: false` in `agents/openai.yaml`.
- Use Codex `$skill-name` references instead of upstream Claude `/skill-name` commands.
- Preserve local workflow ownership: `$delivery-loop` replaces upstream `implement`, and no skill commits automatically without authority from the active task.
- Keep upstream behavior only when the corresponding skill is present. `wayfinder`-specific tracker templates were not imported.
- Do not mirror `in-progress`, `deprecated`, `misc`, or `personal` upstream buckets automatically.
- Reconcile upstream changes semantically before copying; local authority, verification, and documentation rules take precedence.

### Rename Migration

The v1.1.0 planning rename was applied atomically:

- `to-prd` → `to-spec`
- `to-issues` → `to-tickets`

No aliases are retained. Keeping both names would duplicate trigger surfaces and let old planning behavior continue drifting.

## Other Retained Upstream Skills

| Skill | Source Path |
|---|---|
| `receiving-code-review` | `/Users/david/.codex/plugins/cache/openai-curated/superpowers/3fdeeb49/skills/receiving-code-review` |
| `verification-before-completion` | `/Users/david/.codex/plugins/cache/openai-curated/superpowers/3fdeeb49/skills/verification-before-completion` |

## Personal Plugins

| Plugin | Source Path |
|---|---|
| `orchestrated-delivery` | `/Users/david/plugins/orchestrated-delivery` |

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

- Skill directories are self-contained copies; the harness does not depend on the original source paths at runtime.
- Local sync excludes `.system`, `_archive`, plugin caches, and Cloudflare-published skills unless explicitly retained.
- The install script defaults to `~/.agents/skills` so multiple agent tools can consume the same skill directory.
- Agent TOML files are Codex-specific and should be copied to a Codex agents directory when used.
