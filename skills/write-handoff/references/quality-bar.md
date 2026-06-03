# Quality Bar

Use this reference when the handoff is important, complex, or likely to be picked up by someone with limited prior context.

## Standard

A strong handoff lets the next person continue work without re-discovering the key facts, key decisions, or key risks.

"Complete" does not mean "long." It means the handoff preserves the information required for correct next decisions.

## Required Checks

Confirm each item before finalizing:

1. Can a new reader understand the background, goal, and current state within about 1 minute?
2. Can a new reader understand the problem and its importance without already knowing project-specific terminology?
3. Are internal terms, acronyms, and subsystem names defined in plain English on first use?
4. Does the handoff distinguish facts from judgments, assumptions, and recommendations?
5. Does the handoff clearly separate completed work from remaining work?
6. Does the handoff clearly separate verified findings from unverified findings?
7. Do key decisions include the reason they were made?
8. Does the handoff capture the risks, blockers, and hidden assumptions that could affect the next step?
9. Are the next actions concrete enough that someone can begin immediately?
10. Does the handoff preserve enough business and process context that the next person does not need to reconstruct the story from scratch?

## Common Failure Patterns

Watch for these:

- Assuming the reader already knows the project, subsystem names, or internal shorthand
- Using product or codebase terms without translating them into plain English
- Opening with implementation detail before explaining what the work is and why it matters
- Blending confirmed state with guesses or hoped-for outcomes
- Listing actions without recording the decisions that shaped them
- Writing a long chronology that hides the few facts the next person actually needs
- Saying "continue from here" without giving a first concrete action
- Omitting dead ends, rejected approaches, or known traps that the next person is likely to repeat

## Compression Rules

Shorten the handoff by removing:

- Repetitive chronology that does not affect future choices
- Minor implementation detail that is already obvious from the artifact itself
- General commentary that does not change the next person's understanding or actions

Do not shorten away:

- Plain-English explanation of the system area and the user-visible problem
- Context needed to explain why the work matters
- Boundaries of what is and is not covered
- Evidence status
- Rationale behind non-obvious choices
- Risks that could cause rework or wrong assumptions
- Immediate next actions
