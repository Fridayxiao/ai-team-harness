# Issue tracker: Local Markdown

Specs and ticket sets for this repo live as Markdown under `.scratch/`.

## Conventions

- Use one directory per feature: `.scratch/<feature-slug>/`.
- Store the spec at `.scratch/<feature-slug>/spec.md`.
- Store the complete ticket set at `.scratch/<feature-slug>/tickets.md`; each `##` ticket heading is one addressable ticket and carries its own blocking edges.
- Record the tracker-label equivalent as a `Status:` line near the top of a spec or directly below each ticket heading. Use the configured workflow label string, normally `ready-for-agent` for approved artifacts.
- Append comments or decisions beneath the relevant spec section or ticket heading under `### Comments`.

## When a skill says "publish a spec"

Write `.scratch/<feature-slug>/spec.md`, creating the feature directory when needed. Prepend a short title and `Status: ready-for-agent` (or the configured equivalent).

## When a skill says "publish tickets"

Write the approved set to `.scratch/<feature-slug>/tickets.md`. Keep blockers before dependents, preserve every `Blocked by` edge, and give each ticket its own `Status: ready-for-agent` line.

## When a skill says "publish to the issue tracker"

Use the artifact-specific location above. For a standalone issue that belongs to neither a spec nor a ticket set, ask for a path rather than inventing another storage convention.

## When a skill says "fetch the relevant ticket"

Read the referenced feature's `tickets.md` and the named ticket heading. If the user supplies a direct path, read that file.
