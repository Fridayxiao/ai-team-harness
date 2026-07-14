---
name: idea2implement
description: Turn raw product ideas, vague feature concepts, or partially scoped initiatives into implementation-ready briefs and sliced plans through explicit user alignment, selective research and design, and evidence-backed readiness. Use when moving from an idea or discussion to agreed scope, architecture or technical decisions, a spec, TODO plan, tickets, or implementation handoff. Do not use for already-scoped small implementation work or narrow bug fixes unless the user explicitly wants product-to-implementation alignment.
---

# Idea2Implement

Convert uncertainty into user-accepted decisions and verifiable implementation slices. Coordinate existing skills instead of reproducing their workflows.

## Operating Principles

- Treat alignment as a loop, not a one-time interview.
- Use the lightest process that resolves the real uncertainty.
- Separate evidence, user decisions, assumptions, and open questions.
- Create only artifacts that help the user decide, implement, verify, or hand off the work.
- Stop at the handoff the user requested. Planning is the default; if the user also requests implementation, pass the first accepted slice to `$delivery-loop`.
- Do not publish specs, tickets, or external records until the user approves the content and destination.

## Start With An Alignment Snapshot

Before choosing architecture or tools, briefly restate:

- the problem or opportunity
- the target user and desired visible outcome
- known constraints and non-goals
- the requested handoff, such as exploration, brief, plan, spec, tickets, or implementation
- current assumptions and direction-changing open questions

State the depth you intend to use and why. Ask one focused question at a time when the answer can change product direction, scope, architecture, or the requested handoff. When the context is already sufficient, state reasonable assumptions and proceed.

Do not treat silence as agreement on a material decision. Do not ask for confirmation on trivial or easily reversible choices.

## Choose Depth Adaptively

### Light

Use for bounded, low-risk ideas with clear users, outcomes, and constraints. Produce an alignment snapshot and a concise implementation brief in chat. Avoid project documents, deep research, extra skills, and sub-agents by default.

### Standard

Use as the normal path when some product, codebase, or technical uncertainty remains. Inspect relevant local context, compare meaningful options, align at decision checkpoints, and produce verifiable slices. Write durable records only for knowledge worth preserving.

### Deep

Use for high-risk, foundational, multi-system, regulated, security-sensitive, or long-lived initiatives. Add the research, prototypes, ADRs, domain work, or documented delivery controls justified by the risk. Use `$delivery-loop` Documented only when the project needs that level of governance or durable coordination.

Move up or down as uncertainty changes. Do not finish every stage merely because it exists.

## Run The Alignment Loop

### 1. Frame The Product

Establish only what the current idea needs:

- target user and job-to-be-done
- current pain or opportunity
- desired user-visible outcome and success signal
- primary workflow
- scope and non-goals
- constraints, source-of-truth concepts, and important state transitions

Before architecture work, confirm that the user agrees with the problem, outcome, and scope. If they do not, revise the frame before proceeding.

### 2. Reduce The Important Uncertainty

Inspect the codebase, project documents, installed dependencies, and current behavior when they constrain the plan. Research current official documentation or primary sources when APIs, products, versions, security guidance, or ecosystem choices may have changed.

Use a prototype or probe when it answers a consequential question more cheaply or reliably than discussion. Do not claim an integration or capability is proven until source evidence, installed types, runtime behavior, or a probe supports it.

### 3. Align On Decisions

For each material design or architecture decision:

1. Explain what must be decided and why it matters.
2. Present two or three viable options when real alternatives exist.
3. Recommend a default with benefits, downsides, and risks.
4. Ask for explicit confirmation when the choice changes scope, user experience, architecture, cost, or a hard-to-reverse commitment.
5. Record the accepted decision and update earlier assumptions or artifacts it invalidates.

Keep discussion concrete. Summarize what you heard, the decision needed, the recommended default, and what would change based on the answer. Do not use a document as a substitute for user discussion.

### 4. Build Verifiable Slices

Turn accepted decisions into dependency-ordered, user-verifiable slices. For each slice include:

- what user-visible or operational outcome it delivers
- blockers or prerequisites
- acceptance criteria
- the verification method and expected evidence
- documentation or handoff updates only when needed

Prefer vertical tracer bullets. Use horizontal prefactoring only when it creates a necessary seam or keeps later slices independently green. Do not add dates or estimates unless requested.

### 5. Check Readiness With The User

Before calling the result implementation-ready, present a compact synthesis and ask the user to confirm that it matches their intent. Reopen an earlier stage when the user changes the goal, scope, or a major decision.

If the work is not ready, say so and identify the smallest next question, research task, or probe. Do not hide unresolved blockers inside a polished plan.

## Route To Other Skills Selectively

Invoke only the smallest set needed for the current uncertainty:

- Use `$clarify-and-reuse` for material intent ambiguity or meaningful local-versus-ecosystem choices.
- Use `$grill-with-docs` when the user wants a deep stress test or high-impact product, domain, or trade-off questions need sustained interrogation and durable records. This is a user-invoked skill in this harness; follow the visibility guidance below.
- Use `$domain-modeling` when shared vocabulary or state transitions need explicit treatment without a full grilling session.
- Use `$codebase-design` when new or changed Modules, Interfaces, Seams, Adapters, or test surfaces actually need design.
- Use `$prototype` when an experiment is the cheapest way to answer a product, state, interaction, or architecture question.
- Use `$delivery-loop` when the work continues into execution or needs full delivery governance. Choose its mode from the task; do not force Documented mode.
- Use `$write-handoff` when work spans sessions or creates lasting project knowledge.
- Use `$to-spec` only after alignment when the user wants a spec published to the configured tracker. This is a user-invoked skill in this harness.
- Use `$to-tickets` only after the slice breakdown is approved and the user wants tickets created. This is a user-invoked skill in this harness.
- Use `$reuse-opportunity-review` after substantial completed work when extracting reusable lessons is worthwhile.

### Handle Explicit-Only And Invisible Skills

In this harness, treat `$grill-with-docs`, `$to-spec`, and `$to-tickets` as explicit-only unless the active context shows that the user already invoked them. They may be installed but absent from the agent's default skill catalog.

When an explicit-only skill is the best next step but is not visible:

1. Tell the user that it requires explicit invocation and why it would help.
2. Ask the user to invoke the exact `$skill-name`.
3. Do not offer or perform a substitute workflow, and do not claim the skill was activated or followed unless it is actually available in the active context.

For example: "A deeper stress test with durable ADR and glossary updates requires `$grill-with-docs`, which must be invoked explicitly here. Please invoke `$grill-with-docs` to continue that workflow."

Apply the same rule to any other routed skill missing from the current catalog. If it is not installed at all, say it is unavailable. Do not invoke skills merely because they are listed here.

## Use Sub-Agents Deliberately

Handle a normal idea-to-plan session directly. Use a sub-agent only when independent review, specialized research, parallel exploration, or risk isolation materially improves the result.

Do not use a sub-agent:

- to conduct user alignment
- to repeat analysis the main agent can do efficiently
- solely because sub-agents are available
- solely to satisfy this skill

One focused sub-agent is often enough. Follow stricter user or project requirements when they apply. Give every delegated task a self-contained brief, treat its output as advisory, and keep final synthesis, conflict resolution, and verification with the main agent.

## Keep A Compact Evidence Ledger

For Standard and Deep work, track material items with one of these states:

- **Verified**: supported by inspected code, current documentation, a probe, or other cited evidence
- **Accepted**: explicitly chosen or confirmed by the user
- **Assumed**: unverified but safe enough to proceed provisionally
- **Open**: unresolved and capable of changing or blocking the plan

Keep the ledger in chat for short work and in the project's normal planning or decision records when it has lasting value. Never convert a recommendation into an accepted decision without the user's confirmation.

## Produce The Minimum Useful Handoff

An implementation-ready brief normally contains:

1. Problem, target user, and desired outcome
2. Scope and non-goals
3. Accepted decisions and relevant trade-offs
4. Architecture or technical choices only where needed
5. Dependency-ordered implementation slices
6. Acceptance criteria and verification evidence for each slice
7. Assumptions, open risks, and explicit verification gates
8. The first executable slice and where the next person should read first

Add a PRD, glossary, ADR, research note, README update, or ticket set only when the project or user needs it. Use project conventions and avoid duplicating the same decision across artifacts.

## Readiness Standard

Call the plan implementation-ready only when:

- the user has accepted the problem framing, scope, and non-goals
- material product and architecture decisions are accepted or explicitly deferred
- technical claims that affect the first slice are verified or gated
- every slice has an observable outcome, acceptance criteria, and verification method
- no unexplained Open item blocks the first slice
- the first slice and read-first context are clear
- the user has confirmed that the final synthesis matches their intent

Otherwise report **Not ready**, the blocking items, and the smallest next step.

## Avoid

- Forcing `$delivery-loop` Documented on every idea
- Turning alignment into a long questionnaire
- Choosing frameworks before agreeing on the product outcome
- Silently treating assumptions or recommendations as user decisions
- Creating a full artifact suite for ceremony
- Requiring sub-agents for routine work
- Treating documentation or passing tests as proof of user acceptance
- Splitting ordinary feature work only by technical layer
- Claiming readiness while direction-changing questions remain open
