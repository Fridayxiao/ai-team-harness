---
name: clarify-and-reuse
description: Use when an implementation, design, debugging, integration, or refactoring task may have unclear intent, hidden constraints, or existing project, dependency, framework, platform, or current ecosystem solutions worth reusing. Clarify the real goal and prefer reuse before custom code. Do not use for tiny mechanical edits where intent and implementation path are already obvious.
---

# Clarify and Reuse

## Philosophy

**Core principle**: Do not solve the wrong problem, and do not rebuild something the project or ecosystem already gives you.

Good clarification is targeted. It asks only the questions that can change the path. Good reuse starts local, respects project vocabulary and patterns, checks installed capabilities, and researches current mainstream options before inventing custom work when local options do not fit.

Bad clarification turns every request into an interview. Bad reuse blindly forces existing code into the wrong shape. Bad custom work starts from memory, adds parallel abstractions, or chooses a new dependency before checking what already exists.

## Anti-Pattern: Custom-First Work

**DO NOT start by designing new code, abstractions, dependencies, or workflows before checking for a suitable existing path.**

This produces bad work:

- The literal request gets implemented while the real goal remains unclear
- Existing helpers, components, services, schemas, commands, or conventions are duplicated
- New dependencies overlap with installed ones
- Fast-moving ecosystem choices are made from stale memory
- One-off needs become broad infrastructure

**Correct approach**: clarify only the ambiguity that matters, then climb the reuse ladder until a suitable path appears.

## Reuse Ladder

The reuse ladder is the preferred search order for a solution. It is not bureaucracy. Stop when a level gives you a suitable path.

1. Existing project code, docs, tests, conventions, utilities, components, services, schemas, commands, or prior patterns
2. Installed dependencies or existing configuration
3. Framework, platform, runtime, or standard library features
4. Current mainstream external libraries, tools, services, or documented ecosystem patterns
5. Focused custom implementation

If the local project and installed dependencies do not fit, investigate the current ecosystem before inventing. Check official docs or primary sources when APIs, package choices, framework guidance, product behavior, deprecations, or best practices may have changed.

## Workflow

### 1. Orient

Identify the real goal, success condition, constraints, and the ambiguity that could change the approach. Ask the user only when the answer materially changes the path; otherwise state the assumption and proceed.

### 2. Inspect Local Context

Read the relevant project context before designing: docs, code, tests, package manifests, commands, conventions, helpers, components, services, schemas, and nearby patterns.

### 3. Check The Reuse Ladder

Prefer adapting an existing primitive over adding a parallel one. Prefer installed, platform, or framework capabilities over adding a new dependency. Add a dependency only when it is clearly better than local or platform code for this task.

### 4. Research When Local Options Do Not Fit

When no local, installed, framework, platform, or standard-library option fits, research the current mainstream path before custom work. Consider maintenance, compatibility, adoption, licensing, deprecation or migration notes, and fit to the project's constraints.

### 5. Choose The Best-Fitting Path

Pick the path that fits the goal, project shape, maintenance burden, and reversibility. Reuse is not a goal by itself: if an existing option would contort the codebase, hide important domain behavior, or add more long-term cost than it removes, choose a focused custom path and explain why.

Keep the chosen path narrow at first. Expand an abstraction only when a second real use makes the shape clearer.

## What To Say

Before committing to the path, briefly say what mattered:

- "The project already has a helper for this, so I will extend it."
- "The installed dependency already covers this; no new package is needed."
- "There is no suitable local or installed option, so I checked the current ecosystem before choosing this library."
- "The mainstream options are too heavy for this case, so a small custom implementation is clearer than adding a dependency."
- "There are two viable paths; here is the tradeoff and my recommended default."

Keep the report proportional. For small tasks, one sentence is enough.

## Checklist Per Use

```text
[ ] Real goal and success condition are clear enough
[ ] Local docs, code, tests, packages, and patterns were checked when relevant
[ ] Installed, framework, platform, or standard-library options were considered before new dependencies
[ ] Current ecosystem was researched when local options did not fit or facts may be stale
[ ] Chosen path fits the goal, project shape, maintenance burden, and reversibility
[ ] Custom code or new dependencies have a concrete reason
```
