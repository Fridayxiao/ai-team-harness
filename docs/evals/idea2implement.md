# Idea2Implement Evaluation Scenarios

Use these scenarios to check whether `idea2implement` stays lightweight, adapts to risk, aligns with the user throughout the process, and produces evidence-backed plans.

## How To Run

Run each prompt in a fresh task with the current `skills/idea2implement/SKILL.md` and only the fixture files explicitly named by that prompt. Do not add hidden context or expected answers. Capture the response, tool and skill usage, questions asked, artifacts created, and final readiness claim.

Grade observable behavior rather than exact wording. A scenario passes when every Critical item and every scenario-specific Assertion passes and no Failure Signal appears. Expected items are advisory across the suite; record misses, but fail a scenario only when the behavior is also required by its Assertions.

## General Rubric

### Critical

- Restate the user, outcome, scope, and requested handoff before committing to architecture.
- Ask only direction-changing questions and obtain explicit confirmation for material product or architecture decisions.
- Choose a proportionate depth and revise it when the discovered risk changes.
- Distinguish Verified, Accepted, Assumed, and Open material items for Standard or Deep work.
- Give every implementation slice an observable outcome, acceptance criteria, and verification method.
- Do not claim implementation readiness while an Open item blocks the first slice.

### Expected

- Invoke only downstream skills that resolve a current uncertainty.
- Avoid project documents in Light work unless the user requests them.
- Use sub-agents only with a concrete benefit such as independent review, specialized research, parallel exploration, or isolation.
- For an explicit-only companion skill that is not active, explain the benefit and ask the user to invoke the exact `$skill-name`.
- Keep the user-facing discussion concise and revisit earlier decisions when the user changes direction.
- Avoid publishing specs, tickets, or external records before approval.

### Failure Signals

- Force `$delivery-loop` Documented without a task-specific reason.
- Ask a batch of low-impact questions before providing any useful synthesis.
- Select a framework before product outcome and scope are aligned.
- Create a PRD, ADR, glossary, research note, and ticket set by default.
- Delegate user alignment or require multiple sub-agents for ordinary planning.
- Claim to have invoked a user-only skill that is absent from the active skill catalog.
- Continue with a substitute workflow after identifying an explicit-only skill as the required next step.
- Present recommendations as accepted decisions.
- Produce horizontal task lists with no user-visible verification.

## Scenario 1: Small, Clear Idea

### Prompt

> Use $idea2implement to plan a local CLI command that converts one Markdown file to HTML. Use the project's existing Markdown parser. I only need a concise TODO plan in chat; no tickets or project documents.

### Assertions

- Select Light depth.
- Reuse the stated parser and avoid ecosystem research unless local inspection contradicts the prompt.
- Ask at most one question, and only if it changes the command contract or acceptance criteria.
- Produce a concise brief and verifiable slices in chat.
- Do not use a sub-agent or create files.

## Scenario 2: Ambiguous Product Idea

### Prompt

> Use $idea2implement. I want to build something that helps small teams remember important decisions.

### Assertions

- Start with an alignment snapshot and identify the missing target workflow or outcome.
- Ask one focused question at a time instead of choosing a product shape.
- Do not discuss frameworks before the user agrees on the problem, outcome, and initial scope.
- Keep recommendations separate from Accepted decisions.
- Do not claim implementation readiness in the first response.

## Scenario 3: High-Risk Integration

### Prompt

> Use $idea2implement to prepare an implementation plan for adding passkey authentication to our existing account system. Read the synthetic repository context at `docs/evals/fixtures/idea2implement-passkey-context.md`. We need migration, recovery, and auditability, and this will affect production users.

### Assertions

- Select Deep depth and explain the risk-based reason.
- Inspect the named authentication fixture before proposing architecture.
- Research current primary or official sources for security-sensitive technical claims.
- Align on recovery, rollout, and user-visible migration decisions before finalizing slices.
- Use a specialist or independent sub-agent only if it adds a named benefit; do not delegate final decisions or user alignment.
- Mark unproven integration assumptions as Assumed or Open and attach verification gates.

## Scenario 4: Premature Ticket Request

### Prompt

> Use $idea2implement and create implementation tickets for an AI assistant that handles our customer support.

### Assertions

- Do not publish tickets immediately.
- Identify the missing user outcome, authority boundaries, data constraints, and success signal.
- Align on scope and meaningful design decisions before proposing a ticket breakdown.
- Ask for approval of the slice breakdown and destination before invoking `$to-tickets`.

## Scenario 5: Existing Approved Spec

### Prompt

> Use $idea2implement. The spec at `docs/evals/fixtures/idea2implement-approved-spec.md` is already approved and contains the complete synthetic repository context for this evaluation. Check whether it is implementation-ready and give me the first executable slice; do not reopen settled product decisions unless the fixture contradicts them.

### Assertions

- Skip a generic product interview and treat approved decisions as Accepted.
- Inspect the named fixture for gaps or contradictions.
- Ask only about blockers that affect the first slice.
- Report Ready or Not ready with evidence and the first executable slice.
- Avoid new durable artifacts unless a discovered gap has lasting value.

## Scenario 6: Risk Changes Mid-Discussion

Run both turns in the same task.

### Turn 1

> Use $idea2implement to plan a throwaway internal dashboard for five teammates to view synthetic demo data. It will run locally for one week, has no sensitive data, and I only want a concise plan in chat.

### Turn 2

> I need to correct the brief: this will be a production service used by hospitals, store protected health information, and integrate with their identity providers. The plan still needs to be implementation-ready.

### Assertions

- Select Light depth for Turn 1 and avoid unnecessary documents, research, and sub-agents.
- Escalate to Deep after Turn 2 and explain which new risks caused the change.
- Reopen the scope, security, compliance, identity, evidence, and verification assumptions invalidated by the new context.
- Ask the smallest direction-changing question rather than continuing the original plan unchanged.
- Do not claim readiness until the new Open items are resolved or explicitly gated.

## Scenario 7: Explicit-Only Companion Skill

Run this scenario in a fresh task with `$idea2implement` active but `$grill-with-docs` not explicitly invoked.

### Prompt

> Use $idea2implement to shape a cross-team billing platform. The ownership model and domain language are disputed, the architecture will be difficult to reverse, and I want a deep stress test with ADR and glossary updates before planning implementation.

### Assertions

- Identify `$grill-with-docs` as the best-fit deeper workflow.
- Explain that it requires explicit user invocation and ask the user to invoke exactly `$grill-with-docs`.
- Explain the concrete benefit instead of merely naming the missing skill.
- Do not offer or perform a lighter substitute workflow.
- Do not claim that `$grill-with-docs` was activated, loaded, or followed.
