---
name: clarify-and-reuse
description: Use when an implementation, design, debugging, integration, feature, behavior change, or refactoring task may have unclear intent, hidden constraints, meaningful design choices, or existing project, dependency, framework, platform, current ecosystem, library, component, module, or reference-project solutions worth evaluating. Clarify the real goal, compare local and modern external approaches when the choice matters, dispatch a research sub-agent for non-trivial ecosystem research when available, and prefer the best-fitting path over custom code. Do not use for tiny mechanical edits where intent and implementation path are already obvious.
---

# Clarify and Reuse

## Philosophy

**Core principle**: Do not solve the wrong problem, and do not rebuild something the project or ecosystem already gives you.

Good clarification is targeted. It asks only the questions that can change the path. Good design work explores the smallest useful set of viable approaches before committing to one. Good reuse treats local context as constraint input, not as an automatic default. It compares existing project options, installed capabilities, framework/platform features, and current ecosystem options before choosing a path.

Bad clarification turns every request into an interview. Bad design work blocks straightforward execution behind ceremony. Bad reuse blindly forces existing code into the wrong shape. Bad custom work starts from memory, adds parallel abstractions, or chooses a new dependency before checking what already exists.

## Anti-Pattern: Custom-First Work

**DO NOT start by designing new code, abstractions, dependencies, or workflows before checking for a suitable existing path.**

This produces bad work:

- The literal request gets implemented while the real goal remains unclear
- Existing helpers, components, services, schemas, commands, or conventions are duplicated
- New dependencies overlap with installed ones
- Fast-moving ecosystem choices are made from stale memory
- One-off needs become broad infrastructure

**Correct approach**: clarify only the ambiguity that matters, inspect the local constraints, research the ecosystem when the decision is non-trivial, then choose the best-fitting path.

## Lightweight Design Check

For non-trivial features, behavior changes, product decisions, or architecture work, do a compact design check before implementation:

- Understand the purpose, constraints, success condition, and user-visible outcome.
- Read enough project context to avoid proposing changes that fight the existing system.
- Ask one focused question at a time when an answer would materially change the path. If the answer would not change the path, state the assumption and proceed.
- If there are multiple viable approaches, present 2-3 options with trade-offs and a recommended default.
- Split oversized requests into smaller deliverable pieces before trying to design every detail.
- Prefer simple, isolated modules with clear responsibilities and interfaces when new structure is needed.
- Include targeted cleanup only when it directly supports the requested work.

This is not a hard gate. Do not force a design document, commit, staged approval loop, or separate planning skill unless the user asks for that workflow or the task genuinely needs it. Keep the design check proportional: a sentence is enough for small work, while larger changes may need a short plan.

## Option Scan

Do not treat local code as the default answer. Use local inspection to understand constraints, then compare local and external options on fit.

Evaluate whichever of these are relevant:

- Existing project code, docs, tests, conventions, utilities, components, services, schemas, commands, or prior patterns
- Installed dependencies or existing configuration
- Framework, platform, runtime, or standard library features
- Current mainstream external libraries, tools, services, components, templates, starter kits, or documented ecosystem patterns
- Mature open-source projects or reference implementations that reveal good module boundaries, integration patterns, or UX behavior
- Focused custom implementation

Research the current ecosystem proactively when the decision affects maintainability, user-facing behavior, security, performance, architecture, or dependency choice. This is especially important for fast-moving APIs, UI components, editors, tables, charts, auth, payments, parsing, workflow engines, AI SDKs, browser automation, Cloudflare, Supabase, or other platform integrations.

Use official docs, primary sources, package docs, release notes, maintenance signals, and credible reference projects. Compare maintenance, API stability, compatibility, adoption, licensing, bundle/runtime cost, security posture, integration effort, and fit to the project's constraints.

## Research Sub-agent

For non-trivial ecosystem research, dispatch a research sub-agent when subagents are available and permitted by the current environment. Keep local code exploration in the main thread unless it can be cleanly separated.

Give the research sub-agent a self-contained read-only brief:

- The real goal and success condition
- Relevant framework/runtime/package versions and constraints found locally
- The decision to research, such as library choice, component strategy, API shape, or reference-project pattern
- Required sources, preferring official docs, primary repositories, release notes, and mature examples
- Comparison criteria: fit, maintenance, compatibility, licensing, integration cost, risk, and migration path
- Expected deliverable: 2-4 viable options, a recommended default, trade-offs, and links or source names

Do not outsource the final decision. Use the sub-agent's research as input, then synthesize it with local constraints and own the recommendation.

## Workflow

### 1. Orient

Identify the real goal, success condition, constraints, and the ambiguity that could change the approach. Ask the user only when the answer materially changes the path; otherwise state the assumption and proceed.

### 2. Inspect Local Context

Read the relevant project context before designing: docs, code, tests, package manifests, commands, conventions, helpers, components, services, schemas, and nearby patterns.

### 3. Scan Local And Ecosystem Options

Prefer a proven, well-fitting option over a familiar local one. Adapt an existing local primitive when it is genuinely a good fit. Prefer installed, platform, or framework capabilities when they meet the need cleanly. Research current ecosystem options when the choice matters or facts may be stale. Add a dependency only when it is clearly better than local, installed, framework, platform, or focused custom code for this task.

### 4. Dispatch Research When It Matters

When ecosystem fit is material, dispatch a research sub-agent when available and permitted. If subagents are unavailable or not permitted, do the research directly. Do not rely on memory for APIs, package choices, framework guidance, product behavior, deprecations, or best practices that may have changed.

### 5. Choose The Best-Fitting Path

Pick the path that fits the goal, project shape, maintenance burden, and reversibility. Reuse is not a goal by itself: if an existing option would contort the codebase, hide important domain behavior, or add more long-term cost than it removes, choose a focused custom path and explain why.

Keep the chosen path narrow at first. Expand an abstraction only when a second real use makes the shape clearer.

### 6. Implement Without Ceremony

Once the path is clear enough, proceed. Do not keep interviewing the user, write a spec, or wait for approval unless the remaining uncertainty can change the solution or the user explicitly asked for a design-review workflow.

## What To Say

Before committing to the path, briefly say what mattered:

- "The project already has a helper for this, so I will extend it."
- "The installed dependency already covers this; no new package is needed."
- "This decision depends on current ecosystem options, so I dispatched research and compared it with the local constraints."
- "A modern library fits better than the existing local helper because it reduces long-term maintenance and matches the platform guidance."
- "The mainstream options are too heavy for this case, so a small custom implementation is clearer than adding a dependency."
- "There are two viable paths; here is the tradeoff and my recommended default."

Keep the report proportional. For small tasks, one sentence is enough.

## Checklist Per Use

```text
[ ] Real goal and success condition are clear enough
[ ] Local docs, code, tests, packages, and patterns were checked when relevant
[ ] Meaningful design or architecture choices were compared when they affect the path
[ ] Installed, framework, platform, or standard-library options were considered
[ ] Current ecosystem options were researched when the choice is non-trivial or facts may be stale
[ ] Research sub-agent was dispatched for non-trivial ecosystem research when available and permitted
[ ] Chosen path fits the goal, project shape, maintenance burden, and reversibility
[ ] Custom code or new dependencies have a concrete reason
```
