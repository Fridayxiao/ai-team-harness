---
name: to-tickets
description: Break a plan, spec, or current conversation into tracer-bullet tickets with explicit blocking edges, published as local Markdown or native tracker relationships.
---

# To Tickets

Break a plan, spec, or conversation into **tickets** — tracer-bullet vertical slices, each declaring the tickets that **block** it.

The issue tracker and workflow label vocabulary should already be configured. Run `$setup-matt-pocock-skills` if they are not.

## Process

### 1. Gather context

Work from the context already in the conversation. If the user passes a spec path, issue number, or URL, fetch it and read its full body and comments.

### 2. Explore the codebase when needed

Understand enough of the current code to draft realistic slices. Use the project's domain glossary vocabulary in ticket titles and descriptions, and respect ADRs in the area being changed.

Look for prefactoring that makes the feature easier: make the change easy, then make the easy change.

### 3. Draft tracer bullets

For ordinary work, every ticket must:

- Cut a narrow but complete path through the layers it actually touches — vertical, not one horizontal layer
- Be demoable or independently verifiable
- Fit in one fresh context window
- Declare every blocking edge; no blockers means it can start immediately

Prefactoring may come first when it creates the seam needed by later tracer bullets.

#### Wide refactors

A **wide refactor** is the exception to vertical slicing: one mechanical change, such as renaming a shared column or retyping a common symbol, whose **blast radius** fans across the codebase so no narrow vertical slice can land green.

Sequence a wide refactor as **expand–contract**:

1. **Expand** — add the new form beside the old without breaking callers.
2. **Migrate** — move callers in batches sized by blast radius, such as one package or directory per ticket. Every batch is blocked by expand.
3. **Contract** — remove the old form only after every migration ticket is complete.

Keep CI green after each ticket. If individual migration batches cannot stay green, use an integration branch and make them all block one final integrate-and-verify ticket. Treat this as an explicit exception, not a reason to turn ordinary feature work into horizontal slices.

### 4. Confirm the breakdown

Present a numbered list. For every ticket show:

- **Title**
- **Blocked by**
- **What it delivers**

Ask the user whether the granularity and blocking edges are correct and whether tickets should be merged or split. Iterate until the user approves the breakdown.

### 5. Publish to the configured tracker

Publish blockers before dependents.

- **Local files** → write one ticket-set file at the location configured in `docs/agents/issue-tracker.md` (default `.scratch/<feature-slug>/tickets.md`). List tickets in dependency order, represent blocking edges by title, and record the configured ready state on each ticket.
- **Real issue tracker** → publish one issue per ticket. Prefer native parent/sub-issue and blocking relationships; use body references as the fallback. Apply the `ready-for-agent` label unless instructed otherwise.

Do not close or modify the parent issue.

<tickets-file-template>

# Tickets: <short name of the work>

A one-line summary of what these tickets build, with a reference to the source spec when one exists.

Work the **frontier**: any ticket whose blockers are complete. A purely linear chain is worked top to bottom.

## <Ticket title>

**Status:** ready-for-agent (or the configured equivalent)

**What to build:** The end-to-end behavior this ticket makes work, from the user's perspective.

**Blocked by:** The titles of the tickets that gate this one, or "None — can start immediately".

- [ ] Acceptance criterion 1
- [ ] Acceptance criterion 2

</tickets-file-template>

<issue-template>

## Parent

A reference to the parent issue, when one exists.

## What to build

The end-to-end behavior this ticket makes work, from the user's perspective.

## Acceptance criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Blocked by

- A reference to every blocking ticket, or "None — can start immediately".

</issue-template>

In either form, avoid file paths and implementation snippets that will go stale. A concise prototype-derived state machine, reducer, schema, or type shape is acceptable when it is the clearest record of an agreed decision.

Work the frontier one ticket at a time through `$delivery-loop`, clearing task-specific context between independent tickets when practical.
