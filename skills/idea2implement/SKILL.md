---
name: idea2implement
description: Use when the user wants to turn a raw product idea, vague product direction, feature concept, or early project discussion into an implementation-ready plan. Orchestrates product definition, scope control, domain language, architecture design, technical research, ADRs, PRD synthesis, TODO planning, issue slicing, verification gates, and handoff. Do not use for small coding tasks, narrow bug fixes, or already-scoped implementation work unless the user explicitly wants product-to-implementation alignment.
---

# Idea2Implement

Turn a raw idea into an implementation-ready plan without jumping prematurely into code.

This is a meta-skill. It coordinates existing skills and project documents. Do not duplicate what those skills already do; use them at the right stage.

## Core Rule

Run this as `delivery-loop Documented` from the start.

The goal is not to produce code immediately. The goal is to make the idea precise enough that implementation can begin with clear product intent, explicit scope, documented architecture decisions, verified technical assumptions, and reviewable execution slices.

## Use These Skills

Use available skills as needed:

- `delivery-loop`: outer control loop for goal, scope, acceptance, verification, review, handoff, and user acceptance.
- `clarify-and-reuse`: clarify real goal, hidden constraints, reusable local patterns, and current ecosystem options.
- `grill-with-docs`: stress-test product definition, plan, domain language, and tradeoffs while updating glossary and ADR docs. This already runs `domain-modeling`.
- `codebase-design`: design Modules, Interfaces, Seams, Adapters, and test surfaces.
- `write-handoff`: record reusable project knowledge in README, AGENTS, docs, ADRs, runbooks, or plans.
- `to-prd`: synthesize already-aligned discussion into a PRD when issue tracker publishing is desired.
- `to-issues`: split an approved PRD/spec/plan into vertical-slice issues.
- `reuse-opportunity-review`: after the process, extract reusable lessons or skill improvements.

If a listed skill is unavailable, continue with the same responsibility manually and say what is missing.

## Workflow

### 1. Orient With Delivery Loop

Start by defining:

- goal
- scope
- non-goals
- expected output
- constraints
- acceptance criteria
- verification path
- review expectations
- durable records to maintain

Ask only questions whose answers can change direction. For minor choices, choose a reasonable default and proceed.

### 2. Clarify Product, Scope, And Domain Language

Use `clarify-and-reuse` and, when deeper interrogation is needed, `grill-with-docs`.

Establish:

- target user
- core job-to-be-done
- current pain
- desired user-visible outcome
- success signal
- primary workflow
- non-goals
- scope layers, such as Vision, Validation, Beta, Production
- canonical domain terms
- terms to avoid
- user-facing vs internal concepts
- source-of-truth concepts
- state transitions or gates that shape the product
- what must be true before implementation starts

Let `grill-with-docs` update glossary and ADR docs as decisions crystallize.

Do not discuss framework choices before the core product task, scope, and success criteria are clear.

### 3. Decide Architecture

Use `codebase-design`.

Identify:

- Modules
- Interfaces
- Seams
- Adapters
- source-of-truth ownership
- runtime/context/cache/UI state that is not source of truth
- external side effects that need adapters
- test surfaces
- dependency direction

Prefer deep Modules with small Interfaces. Avoid duplicate mutation paths.

Create ADRs when a decision is hard to reverse, surprising without context, and chosen from real tradeoffs.

### 4. Research Technical Choices

Use current official docs, primary sources, local package docs, or sub-agent research when APIs or ecosystem choices may have changed.

Research only decisions that affect maintainability, correctness, security, user experience, or architecture.

Produce a coverage matrix:

```text
Capability / Risk -> Default Technical Choice -> Status
```

Include verification gates for:

- fast-moving libraries
- external APIs
- provider capabilities
- framework integration points
- security-sensitive dependencies
- package/version assumptions

Do not claim an integration is proven until installed types, docs, or a probe confirm it.

### 5. Create Durable Project Records

Use `write-handoff`.

Maintain a project entrypoint such as `README.md` with:

- current status
- read-first order
- accepted architecture
- implementation guardrails
- verification gates
- documentation maintenance rules

Keep reusable research in `docs/research`, significant decisions in `docs/adr`, vocabulary in `CONTEXT.md`, and implementation plans in `docs/plans` or the project's equivalent structure.

Do not leave important decisions only in chat history.

### 6. Synthesize PRD When Useful

Use `to-prd` only after product definition and major implementation decisions are already aligned.

Do not use `to-prd` as an interview tool. It synthesizes existing context.

Before publishing a PRD, confirm the test seams and user-facing outcomes are correct.

### 7. Create Implementation TODO Plan

Create a TODO-style implementation plan with no dates or time estimates unless the user explicitly requests scheduling.

The plan should include:

- slices in dependency order
- checklist items
- acceptance criteria
- verification requirements
- review gates
- handoff/documentation updates

Prefer implementation slices that are independently verifiable. Avoid pure horizontal slices unless they are necessary prefactoring.

### 8. Split Issues When Ready

Use `to-issues` after the PRD/spec/plan is approved.

Issues should be tracer-bullet vertical slices:

- schema/data
- command or backend behavior
- API/route
- UI
- tests
- acceptance criteria

Each issue should be demoable or independently verifiable.

Do not publish issues before the user approves the slice breakdown.

### 9. Readiness Review

Before saying implementation can start, check:

- product definition is stable enough
- scope and non-goals are explicit
- domain vocabulary is captured
- architecture decisions are recorded
- coverage matrix has no unexplained gaps
- verification gates are explicit
- implementation plan exists
- handoff entrypoint is updated
- unresolved risks are named

Use a sub-agent review for complex plans when available or required by project instructions.

## Output Shape

For alignment work, prefer these artifacts:

- product spec or PRD
- `CONTEXT.md` glossary updates
- ADRs
- architecture draft
- technical research note
- coverage matrix
- README / handoff entrypoint
- implementation TODO plan
- vertical-slice issue breakdown

Use only the artifacts the situation warrants. Do not create documents for ceremony.

## Anti-Patterns

- Jumping from idea directly to code.
- Asking many low-impact questions instead of making reasonable defaults.
- Choosing frameworks before product success criteria are clear.
- Treating chat memory, frontend state, or agent memory as product source of truth without explicitly deciding so.
- Recording decisions only in conversation.
- Creating ADRs for trivial or easily reversible choices.
- Turning implementation plans into schedules when the user asked for TODOs.
- Splitting issues by technical layer instead of vertical user-verifiable slices.
- Automating or scripting a process before the workflow has stabilized.

## Completion Criteria

The process is complete when the user can reasonably say:

- what is being built
- why it matters
- what is out of scope
- what architecture will be used
- which technical choices are accepted
- which assumptions still need verification
- what the first implementation slice is
- how progress will be verified
- where the next agent or human should read first
