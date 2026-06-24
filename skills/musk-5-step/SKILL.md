---
name: musk-5-step
description: >
  Use this skill when the user explicitly asks to apply the Musk 5-step method,
  asks to challenge or simplify requirements before optimizing, or wants a structured
  first-principles review of a system, product feature, workflow, team process,
  architecture plan, incident, or operational setup. Also use when the user specifically
  mentions clarify/delete/simplify/accelerate/automate, removing unnecessary requirements,
  or questioning whether work should exist before building it. Do not trigger for ordinary
  planning, debugging, implementation, architecture review, or "make this better" requests
  unless the user wants this five-step lens or a deliberate requirement-challenge pass.
---

# Musk 5-Step Method

## Core Rule

**Do not optimize what should not exist.**
**Do not automate what has not been simplified.**

The order of the five steps is mandatory. Starting from Step 3 or later without completing
the earlier steps is the most common failure mode. If a step reveals that a prior step was
incomplete, return to it before moving forward.

---

## Step 1 — Question and Clarify Requirements

The goal of this step is not merely to understand requirements — it is to **challenge their
legitimacy**. Every requirement must justify its existence. Requirements without a clear
owner and a clear reason are candidates for deletion.

For each requirement, ask:

1. What exact outcome does this requirement produce, and how would we know if it failed?
2. Who owns this requirement, and can that person be named specifically?
3. Why does this requirement exist? What breaks if we remove it?
4. Is this constraint real, or is it inherited from habit, fear, or an assumption no one has tested?
5. What uncertainty remains that could invalidate this requirement later?

**Rewrite all surviving requirements as testable hypotheses before proceeding.**
If a requirement cannot be made testable, it is not yet understood well enough to act on.

**Output expectation:**
1. Restated goal as a single testable hypothesis: "We will know this succeeded when ___."
2. Constraint list: what is genuinely fixed and non-negotiable, and why.
3. Challenged requirement log: requirements that were questioned, and whether they survived or were flagged for deletion in Step 2.
4. Open questions list: what remains unknown and what is needed to resolve it.
5. Explicit stop condition: if the goal cannot be stated as a testable hypothesis, stop here and return to the user before proceeding.

---

## Step 2 — Delete

Remove anything that does not directly produce the target outcome established in Step 1.
Deletion is the highest-leverage action in this process. Additions add complexity; deletions
remove it permanently.

Candidates for deletion:

- Requirements, parts, or processes that exist by convention rather than demonstrated need
- Speculative or "just in case" features
- Duplicate logic or redundant checks
- Abstraction layers that add indirection without reducing coupling
- Approval gates or handoffs that do not change the outcome
- Monitoring, logging, or documentation of things that should not exist

**Rule:** If a deletion improves clarity or speed and does not increase core risk, keep it deleted.
If uncertain, mark it as provisional deletion and carry a risk statement.

**Output expectation:**
1. Deletion list: each removed item named explicitly.
2. Reason for each deletion: one sentence.
3. Risk statement for each deletion: what could go wrong, and what would trigger reverting it.
4. Items marked for provisional deletion: things that might be removable but need validation first.

---

## Step 3 — Simplify or Optimize

Only after deletion is complete does simplification begin. Simplifying something that
should not exist is wasted effort.

Apply simplification to:

- Architecture: reduce layers, flatten structure, remove unnecessary indirection
- API shape: fewer parameters, fewer states, fewer required decisions by the caller
- UX path: fewer steps, fewer choices, fewer error states the user must handle
- Process handoff: fewer transitions, clearer ownership at each stage
- State flow: reduce the number of states a system or user can be in

Optimization (performance, reliability, cost) is appropriate only where it materially
changes the target outcome. Optimize last within this step, not first.

**Output expectation:**
1. Simplifications made: named and described.
2. Optimizations applied: named, with the specific bottleneck or constraint they address.
3. Measurable effect or acceptance criterion for each change: how will we know this worked?

---

## Step 4 — Accelerate

Increase the speed of the critical path. This is not about working harder — it is about
identifying and removing the friction that slows iteration, feedback, and delivery.

Focus on:

- Blocking dependencies on the critical path
- Cycle time of the build–test–review–feedback loop
- Handoff and approval latency where the delay does not add assurance
- Waiting time that is structural rather than necessary

Do not accelerate steps that were candidates for deletion and survived only provisionally.
Accelerating uncertain steps locks them in.

**Output expectation:**
1. Concrete cycle-time target: current time → target time, for the critical path or key loop.
2. Identified friction points: what is causing the delay.
3. Minimum safe scope for faster iteration: the smallest increment that can be tested independently.
4. What must remain slow: steps where speed would increase risk.

---

## Step 5 — Automate

Automation is the final step. Automating a process before it is stable, simplified, and
validated locks in its flaws at scale. Validate Steps 1–4 with a thin manual or semi-manual
implementation before automating.

Automation is appropriate when:

- The action is high-repetition and low-variance
- The inputs and outputs are well-defined and stable
- The failure modes are known and recoverable
- A human operator has successfully run the process manually at least once

**Output expectation:**
1. Automation scope: exactly what is automated, and what remains manual.
2. Trigger definition: what event or condition initiates the automation.
3. Rollback and override path: how a human stops, reverts, or overrides the automation.
4. Verification checks: what confirms the automation ran correctly after each execution.
5. Deferred automation log: things that were considered for automation but deferred, and why.

---

## Required Output Sequence

Always produce outputs in this order:

1. **Clarified goal and constraints** — testable hypothesis, constraint list, open questions
2. **Deletion list** — with rationale and risk per item
3. **Simplify/optimize plan** — with expected measurable effect
4. **Acceleration plan** — with explicit cycle-time target
5. **Automation plan** — with scope, trigger, rollback, and verification
6. **Trade-off note** *(only when genuine alternatives exist)* — if Step 1 or Step 2 surfaces a real fork in approach, present 2 options with explicit trade-offs. Do not manufacture alternatives when the method points clearly to one direction.

---

## Anti-Patterns

- Optimizing or automating something that should have been deleted
- Adding automation before complexity has been reduced
- Patching symptoms rather than questioning the requirement that causes them
- Treating "we've always done it this way" as a reason a requirement is valid
- Presenting a single path without acknowledging where genuine alternatives exist
- Presenting multiple alternatives to avoid taking a position when the method points to one answer
- Accelerating steps that are still candidates for deletion

---

## Decision Boundary

**Stop at the first point where uncertainty is too high to proceed safely.**

Specifically:

- If the goal cannot be written as a testable hypothesis → stop, return to the user
- If a requirement's owner cannot be named → flag it; do not build on it
- If deletion risk cannot be assessed → mark as provisional, not confirmed
- If the system being changed has no rollback path → stop before Step 5

Ask for the missing constraint before implementing at scale. A small experiment that
fails fast is always preferable to a large implementation that fails slowly.

---

## Default Behavior

- Prioritize correctness of understanding over speed of output
- Keep decisions minimal, reversible, and explicitly documented
- Surface assumptions rather than silently acting on them
- When in doubt about a requirement's validity, question it rather than implement it
