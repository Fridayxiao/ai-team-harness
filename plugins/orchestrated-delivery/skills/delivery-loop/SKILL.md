---
name: delivery-loop
description: Use for Delivery Loop, delivery-loop, or orchestrated-delivery requests, or complex goals needing scope, verification/testing, review, handoff, thread coordination, or user acceptance. Pair with $grill-with-docs for unclear design, domain language, or tradeoffs. Skip tiny mechanical edits unless requested.
---

# Delivery Loop

## Core Principle

Drive complex work to user acceptance.

Keep goal, scope, approach, acceptance, execution, verification, review, and outcome connected. Records preserve decisions, evidence, and handoff context so the next person can understand what was decided, what changed, what was verified, and what still needs judgment.

Do not rush into implementation before acceptance is clear. Do not treat "tests passed" as delivery when the user still cannot judge the outcome.

Use `$grill-with-docs` when the goal, design, domain language, or tradeoffs need sharper questioning. Let it update `CONTEXT.md` and ADRs when useful. Delivery Loop still owns the current goal, acceptance, execution, verification, review, and outcome.

## Required Start

Whenever this skill is used, start by saying Delivery Loop is active and choose the operating mode. If the task is small but the user explicitly requested Delivery Loop, use Lite mode instead of declining the skill.

Choose the operating mode:

- **Lite**: goal, acceptance, verification, and final acceptance path for a bounded task.
- **Standard**: alignment, approach, acceptance, sliced execution, verification, review, and final report for a complex local task.
- **Threaded**: Standard plus `$codex-thread-manager` for user-visible Codex thread coordination, existing thread continuation, independent worktrees, long-running lanes, or risk isolation.
- **Documented**: Standard plus explicit project documents when the user asks for durable workflow records or the task produces reusable project knowledge.

Before implementation, define:

- goal, scope, non-goals, expected output, and constraints
- open questions whose answers would change the work
- acceptance criteria and verification/test plan
- review expectations and residual risks worth reporting

Ask targeted questions only when the answer changes the work. Otherwise state assumptions and proceed.

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
- acceptance criteria
- verification/test plan: relevant commands, manual checks, evidence to capture, and known gaps
- unacceptable outcomes
- review expectations
- residual risks worth reporting

Choose checks that match the risk: unit, integration, end-to-end, typecheck, lint, build, browser/API smoke test, artifact inspection, or manual verification. If no meaningful automated test exists, say why and use the strongest manual check available.

Do not create or adopt a persistent runtime goal until goal, approach, and acceptance are clear and the user explicitly agrees.

### 5. Deliver In Slices

Work in reviewable slices. For each slice, choose the next move, execute, run the relevant check when feasible, and review when needed. Fix failing checks before moving on, or record the failure, reason, and residual risk when the task must stop or proceed.

Delegate when it improves coverage, isolation, speed, or judgment. Treat delegate output as advisory until you check it. If user or repo instructions require subagent review, handoff documentation, or specific verification, those stricter instructions apply.

Use `$codex-thread-manager` when the work involves user-visible Codex threads: continuing existing threads, coordinating multiple thread lanes, creating or briefing independent worktrees, collecting thread results, handing off work, archiving completed threads, or isolating long-running or risky execution. Use ordinary subagents for internal parallel work that does not need user-visible thread state.

### 6. Close The Loop

Report what changed, exact verification commands or manual checks and results, what was reviewed, what remains risky or unverified, and how the user can accept the result. Do not replace evidence with a generic "verified" claim. Update durable docs when the work produced reusable project knowledge or when future work would lose important decisions without a written record.

## Records

Keep records tied to decisions, evidence, review, and handoff.

Create or update durable records when the work spans multiple sessions, changes architecture or domain language, uses subagents or Codex threads, leaves residual risk, depends on acceptance evidence, or creates reusable project knowledge.

Use the project's normal docs for long-lived knowledge. Use a delivery note, issue comment, PR note, execution log, or final report for goal-specific decisions and evidence. Do not duplicate project docs into delivery notes. Do not leave important decisions, validation evidence, review outcomes, or acceptance steps only in memory.

## Checklist Per Loop

```text
[ ] Goal, scope, non-goals, and expected output are clear
[ ] Existing docs were reused instead of duplicated
[ ] Approach was researched enough for the risk level
[ ] Acceptance and verification/test plan are known before execution
[ ] Work was delivered in reviewable slices
[ ] Relevant checks were run, or explicit gaps and residual risks were captured
[ ] Verification and review evidence are captured
[ ] Durable knowledge went into project docs, not temporary notes
[ ] Final outcome is mapped to user acceptance
```
