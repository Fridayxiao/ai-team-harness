---
name: grill-with-docs
description: Grilling session that also builds the project's domain model, sharpening terminology and updating CONTEXT.md and ADRs inline. Use when the user wants to stress-test a plan or design in a codebase while preserving shared language and architectural decisions.
---

# Grill With Docs

Run a `$grilling` session while using `$domain-modeling` to maintain the project's domain model as the conversation clarifies.

## Workflow

1. Use `$grilling` to interview the user about the plan or design one question at a time.
2. If an answer can be discovered from the codebase, inspect the codebase instead of asking.
3. Use `$domain-modeling` whenever terminology, relationships, constraints, or hard-to-reverse decisions crystallize.
4. Update `CONTEXT.md` or context-specific `CONTEXT.md` files when canonical domain terms are resolved.
5. Create or update ADRs only for decisions that are hard to reverse, surprising without context, and the result of a real tradeoff.
6. Do not implement the feature during the grilling session unless the user explicitly changes the task.

## Output

Finish with the clarified plan, unresolved questions, and a short list of domain docs or ADRs updated during the session.
