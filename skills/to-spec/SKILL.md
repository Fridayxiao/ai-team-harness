---
name: to-spec
description: Turn the current conversation into a spec and publish it to the project issue tracker — no interview, just synthesis of what you've already discussed.
---

# To Spec

Turn the current conversation context and codebase understanding into a spec (sometimes called a PRD). Synthesize what is already known; this skill is not an interview.

The issue tracker and workflow label vocabulary should already be configured. Run `$setup-matt-pocock-skills` if they are not.

## Process

1. Explore the repo to understand the current state of the codebase, if you have not already. Use the project's domain glossary vocabulary throughout the spec, and respect ADRs in the area you are touching.

2. Sketch the seams at which the feature will be tested. Prefer existing seams to new ones and use the highest seam possible. If new seams are needed, propose them at the highest point you can. Fewer seams are better; one seam is ideal when it still gives meaningful coverage.

   Confirm with the user that the seams match their expectations.

3. Write the spec with the template below, publish it to the configured issue tracker, and apply the configured `ready-for-agent` workflow label. No additional state transition is required.

<spec-template>

## Problem Statement

The problem the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A thorough, numbered list of user stories. Use this format:

1. As an <actor>, I want a <feature>, so that <benefit>.

Cover the meaningful user-visible behavior without inventing scope that the conversation did not establish.

## Implementation Decisions

The implementation decisions already made, including whichever are relevant:

- Modules and interfaces to build or modify
- Technical clarifications
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Avoid specific file paths or code snippets because they go stale quickly. Exception: when a prototype produced a state machine, reducer, schema, or type shape that captures a decision more precisely than prose, include only the decision-rich excerpt and identify it as prototype-derived.

## Testing Decisions

Include:

- The agreed public seams and behavior-level tests
- The modules covered at those seams
- Similar tests already present in the codebase

## Out of Scope

The work explicitly outside this spec.

## Further Notes

Any remaining context needed to implement or review the work.

</spec-template>
