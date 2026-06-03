---
name: clarify-and-reuse
description: Use when solving implementation or design tasks. Clarify the real need, inspect existing context, and prefer proven existing solutions before custom work.
---

# Clarify and Reuse

## Core Rule

Start by clarifying the real need before choosing an implementation path.

Do not jump directly into custom work. First understand the user's goal, success criteria, constraints, existing context, and likely hidden assumptions. Then prefer suitable existing solutions over building new ones.

## Working Order

Follow this order for non-trivial design, implementation, modification, debugging, or integration tasks:

1. Restate the actual goal and identify ambiguity.
2. Inspect the current context: repository structure, docs, existing code, conventions, utilities, components, workflows, and prior patterns.
3. Check already-available capabilities: installed packages, framework features, platform APIs, standard libraries, internal tools, and existing integrations.
4. Evaluate proven external solutions when the current project does not already provide a good fit. Prefer mature, maintained, documented, compatible, and widely adopted options.
5. Build custom only when existing options are unsuitable, unnecessarily heavy, incompatible, risky, poorly maintained, or less efficient than a focused implementation.

## Before Recommending a Path

State what was checked before proposing the solution.

Use concrete statements such as:

- The project already has a suitable helper, so reuse it.
- The installed dependency already covers this need, so use it instead of adding another package.
- A mature ecosystem library fits better than custom logic.
- Existing options do not fit because of compatibility, size, licensing, maintenance, or domain-specific constraints.

When multiple reasonable options exist, compare tradeoffs briefly and recommend a default.

## Reuse Standards

Prefer composition over reinvention.

Reuse and extend existing primitives, patterns, abstractions, components, utilities, hooks, services, schemas, templates, configuration, and conventions whenever they fit the need.

Avoid adding a new dependency when an existing dependency or platform feature already solves the problem well.

## Custom Implementation Rules

Write custom code only when there is a clear reason.

When custom work is necessary:

1. Explain why existing options are insufficient.
2. Keep the design minimal and focused.
3. Make the result reusable when the need is likely to recur.
4. Avoid building generic infrastructure for a one-off requirement.
5. Document the boundary between domain-specific logic and reusable primitives when useful.

## Anti-Patterns

Avoid these behaviors:

- Solving the literal request without rethinking the actual user need.
- Implementing before checking existing project code and dependencies.
- Duplicating helpers, wrappers, components, workflows, or utilities.
- Adding overlapping libraries.
- Rebuilding common functionality that mature tools already handle.
- Creating broad abstractions before repeated need is proven.
- Choosing custom code because it feels faster without checking reuse options first.

## Default Mindset

Clarify first. Reuse second. Customize last.

Use proven building blocks where they fit. Build new solutions only when the need is specific, valuable, and clearly justified.
