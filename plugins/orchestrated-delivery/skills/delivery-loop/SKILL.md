---
name: delivery-loop
description: Lightweight delivery loop for complex goals. Use when a goal needs alignment, scope, approach, acceptance, execution planning, verification, review, and user acceptance without heavyweight workflow paperwork. Use with grill-with-docs when the goal, design, domain language, or tradeoffs need deeper questioning. Do not use for simple tasks.
---

# Delivery Loop

## Philosophy

**Core principle**: Drive complex work to user acceptance, not to workflow completion.

Good delivery loops keep goal, scope, approach, acceptance, execution, verification, review, and outcome connected. Records exist to preserve decisions and evidence, not to satisfy a process.

Bad delivery loops create paperwork, rush into implementation before acceptance is clear, or treat "tests passed" as delivery when the user still cannot judge the outcome.

Use `$grill-with-docs` when the goal, design, domain language, or tradeoffs need sharper questioning. Let it update `CONTEXT.md` and ADRs when useful. Delivery Loop still owns the current goal, acceptance, execution, verification, review, and outcome.

## Anti-Pattern: Workflow Paperwork

**DO NOT create documents just because the loop has steps.**

This produces bad delivery:

- The agent optimizes for filling templates instead of understanding the goal
- Existing README, CONTEXT.md, ADRs, issues, and plans get duplicated
- The user is asked to approve process artifacts instead of meaningful decisions
- Execution drifts because acceptance was written as ceremony, not as a testable target

**Correct approach**: keep the smallest useful record. If existing docs carry the context, reference them. If something important would be lost after the session, record it where it belongs.

## Workflow

### 1. Orient

Read enough context to avoid guessing: user request, AGENTS.md, README, CONTEXT.md, ADRs, issues, plans, code, tests, runtime behavior, or current external docs when facts may have changed.

### 2. Align

Define the current goal, scope, non-goals, expected output, constraints, and open questions. Ask targeted questions only when the answer changes the work.

Use `$grill-with-docs` when domain language is fuzzy, the plan needs stress-testing, or a design decision deserves sharper questioning.

### 3. Decide

Research enough for the risk level. Reuse existing solutions and project patterns before inventing new ones. Compare options when there is a real choice, then recommend a default with the tradeoffs that matter.

Record durable project knowledge in the project's normal docs. Record goal-specific choices only as much as future work needs.

### 4. Define Acceptance

Before execution, know how the result will be judged:

- user-visible outcome or final deliverable
- validation method
- unacceptable outcomes
- review expectations
- residual risks worth reporting

Do not create or adopt a persistent runtime goal until goal, approach, and acceptance are clear and the user explicitly agrees.

### 5. Deliver In Slices

Work in reviewable slices. For each slice, choose the next move, execute, verify, and review when needed.

Delegate only when it improves coverage, isolation, speed, or judgment. Treat delegate output as advisory until you check it. Use `$codex-thread-manager` for user-visible Codex thread coordination; use ordinary subagents for internal parallel work.

### 6. Close The Loop

Report what changed, how it was verified, what was reviewed, what remains risky or unverified, and how the user can accept the result. Update durable docs when the work produced reusable project knowledge.

## Records

Prefer the smallest useful record.

If existing docs already carry the context, reference them. If the information belongs to the project long-term, put it in project docs. If it belongs only to the current goal, keep it in a lightweight delivery note, issue comment, PR note, execution log, or final report.

Do not duplicate project docs into delivery notes. Do not leave important decisions, validation evidence, review outcomes, or acceptance steps only in memory.

## Checklist Per Loop

```text
[ ] Goal, scope, non-goals, and expected output are clear
[ ] Existing docs were reused instead of duplicated
[ ] Approach was researched enough for the risk level
[ ] Acceptance and validation are known before execution
[ ] Work was delivered in reviewable slices
[ ] Verification and review evidence are captured
[ ] Durable knowledge went into project docs, not temporary notes
[ ] Final outcome is mapped to user acceptance
```
