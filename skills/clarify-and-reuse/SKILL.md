---
name: clarify-and-reuse
description: Use when an implementation, design, debugging, integration, or refactoring task may have unclear intent, hidden constraints, or existing project/platform solutions worth reusing. Clarify just enough to avoid wrong work, inspect local context, and prefer established or currently mainstream solutions before custom code. Do not use for tiny mechanical edits where the intent and implementation path are already obvious.
---

# Clarify and Reuse

## Core Rule

Clarify enough to avoid doing the wrong work. Reuse before inventing.

Do not turn every task into a process. Match the depth of clarification and research to the risk, ambiguity, and cost of being wrong.

## When To Apply

Use this skill for non-trivial work, especially when:

- The request could be interpreted more than one way.
- The work may duplicate existing code, components, helpers, workflows, dependencies, or platform features.
- A design choice, package choice, abstraction, integration, or refactor would be hard to reverse.
- The user asks for a solution but the real goal or success condition is not yet clear.

Keep it lightweight or skip it for tiny mechanical edits where the goal, target files, and implementation path are obvious.

## Working Loop

1. Identify the real goal, success condition, constraints, and any ambiguity that would change the approach.
2. Inspect existing context first: docs, code, tests, package manifests, conventions, utilities, components, services, schemas, commands, and prior patterns.
3. Check available capabilities in this order:
   - Existing project code or patterns
   - Installed dependencies
   - Framework, platform, or standard library features
   - Researched current mainstream, modern, and well-maintained external solutions or documented ecosystem patterns
   - Focused custom implementation
4. If no local or installed option fits, investigate the current ecosystem before custom work. Check official docs, package or framework guidance, maintenance status, compatibility, adoption, and deprecation or migration notes when relevant.
5. Choose the smallest suitable path.
6. If custom work is needed, state why local, installed, platform, and researched external options were not a good fit.

## Decision Rules

- Ask the user only when the answer would materially change the path. Otherwise state the assumption and proceed.
- Prefer adapting an existing primitive over adding a parallel one.
- Prefer an installed dependency or platform feature over adding a new dependency.
- When local and installed options do not fit, research before inventing. Do not rely on memory for fast-moving ecosystems, current best practices, or package choices.
- Prefer the solution that is suitable, current, mainstream enough to be supportable, actively maintained, compatible with the project, and appropriately scoped.
- Add a new dependency only when the researched option is clearly better than local code.
- Build custom code when existing options are too heavy, incompatible, risky, poorly maintained, licensing-problematic, or do not fit the domain.
- Avoid general abstractions until repeated need is visible.

## What To Report

Before committing to a path, briefly say what was checked and why the chosen path fits. Examples:

- "The project already has a helper for this, so I will extend it."
- "The installed dependency already covers this; no new package is needed."
- "There is no suitable local or installed option, so I checked the current ecosystem before choosing this library."
- "The current mainstream options are too heavy for this case, so a small custom implementation is clearer than adding a dependency."
- "There are two viable paths; here is the tradeoff and my recommended default."

Keep the report proportional. For small tasks, one sentence is enough.

## Avoid

- Solving the literal request while missing the real user need.
- Rebuilding a helper, component, wrapper, workflow, or utility that already exists.
- Adding overlapping libraries.
- Creating broad infrastructure for a one-off.
- Blocking progress with excessive clarification when a safe assumption is available.
- Choosing custom code because it feels faster without first checking obvious reuse paths.
