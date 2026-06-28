---
name: set-goal
description: Define, refine, and set explicit Codex goals. Use when the user asks to create, set, update, clarify, structure, inspect, complete, or block a goal, especially with /goal, goal tooling, target outcomes, done conditions, scope, constraints, completion evidence, completion rules, or blocked/complete status decisions.
---

# Set Goal

## Purpose

Turn a user's intent into a clear, bounded goal before creating or changing goal state.

A goal is not a plan, task list, PRD, test plan, or raw transcript. A goal is the current thread's intended outcome.

## Goal Model

Use this structure by default:

```markdown
Goal:
[One concrete target outcome sentence.]

Done Conditions:
- [Observable condition 1]
- [Observable condition 2]
- [Observable condition 3]

Scope:
- In:
- Out:
- Constraints:
- Context:
```

Treat `Goal`, `Done Conditions`, and `Scope` as the required parts. `Done Conditions` are the requirements that define when the goal is complete; they are not verification steps.

## Quality Bar

Before setting a goal, ensure the draft is clear, explicit, and good enough to guide execution.

- Define `Goal` as the target outcome to achieve, not the activity to perform.
- Define `Done Conditions` as observable states that must be true when the work is finished.
- Define `Scope` as what is in, what is out, what constraints apply, and what context matters.
- Keep one primary outcome per goal.
- Exclude implementation steps unless they are true constraints.
- Do not put commands, test steps, human-only checks, or evidence collection inside the goal content.
- Do not include human-only, subjective, or user-acceptance checks as ordinary `Done Conditions`.
- Avoid vague words like "better", "works", "optimized", or "normal" unless the goal defines how to judge them.
- Do not invent requirements, constraints, context, commands, checks, or evidence. Use `None known` or `Not applicable` only when that is accurate; ask the user when missing information would change the goal.

## Creation Gate

Do not create or update a goal unless the goal includes:

- A concrete target outcome in `Goal`.
- Observable `Done Conditions` that define completion without listing validation steps.
- `Scope` that defines in-scope work, out-of-scope work, constraints, and relevant context.
- Explicit user approval after presenting the drafted goal.
- The actual goal content to be stored matches the approved draft, including `Goal`, `Done Conditions`, and `Scope`.

## Workflow

1. Identify the user's intended outcome.
2. If goal state may already exist, read the current goal before drafting changes.
3. If an active unfinished goal exists, surface it and ask how to proceed unless the user or tool instruction already defines the transition.
4. Draft the goal using the Goal Model.
5. Check whether `Goal`, `Done Conditions`, and `Scope` are all specific and actionable.
6. If any required part is missing or vague, ask the smallest necessary clarifying question, or propose a tightened draft for user confirmation.
7. Present the drafted goal to the user and ask for explicit approval before creating or updating goal state.
8. If the user explicitly approves and the Creation Gate is satisfied, use the available goal tool to create or update the goal with the approved draft as the stored goal content.
9. After creating or updating the goal, check the stored goal returned by the tool. If it is missing approved sections or has been reduced to a one-sentence summary, treat that as a failed goal setup and report the mismatch instead of claiming the goal was set correctly.

## Completion Gate

Do not mark a goal complete merely because implementation work is finished.

Before marking a goal complete:

1. Read the stored goal.
2. Extract every `Done Condition`.
3. Produce concrete completion evidence for each condition using agent-accessible artifacts: command output, tests, builds, type checks, lint results, files, logs, browser automation, API responses, database queries, screenshots, or equivalent observable evidence.
4. If any `Done Condition` cannot be checked by the agent, do not mark complete. Report the work as ready for review or ask for the missing external confirmation.
5. If any condition fails, is skipped, is assumed, or lacks evidence, do not mark complete.
6. Mark complete only when every `Done Condition` has concrete evidence, or when the user explicitly changes the goal to remove or replace an unverifiable condition.

## Goal Tool Rules

Use goal tooling only when the user explicitly asks to set, create, inspect, complete, or block a goal, or when higher-priority instructions require it.

- Call the current-goal/read tool first when goal state may already exist.
- Create or update a goal only after the goal text is clear enough to guide work and only after the user has approved the drafted goal.
- Store the full user-approved draft in the actual goal. Do not replace it with only the `Goal` line, a summary, or a shorter paraphrase unless the user explicitly approved that shorter text.
- If the goal tool exposes only a single `objective` string field, put the full approved Markdown goal draft in that field.
- Before calling the goal tool with `status: complete`, apply the Completion Gate and report the evidence for each `Done Condition`.
- Do not use "user can verify later" or "external confirmation pending" as completion evidence. If user confirmation is required, leave the goal active and report ready for review.
- Mark a goal `blocked` only when the same blocking condition has repeated for at least three consecutive goal turns and meaningful progress is impossible without user input or an external state change.
- When reporting a completed budgeted goal, include the final token and time usage if the goal tool returns it.

## Examples

Vague:

```markdown
Goal:
Make login better.
```

Better:

```markdown
Goal:
Fix the Safari login submit failure so valid users can sign in without changing the existing authentication API contract.

Done Conditions:
- Valid Safari login reaches the authenticated state.
- Existing login API request and response contract remain unchanged.
- Existing login regression coverage still passes.

Scope:
- In: Login form submission behavior on Safari.
- Out: Registration, logout, permissions, or authentication architecture changes.
- Constraints: Use the existing authentication flow.
- Context: User reports that clicking submit does not complete login in Safari.
```

If the user says "set a goal to improve performance", ask for the target surface and observable done conditions before creating the goal.
