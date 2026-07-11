---
name: code-review
description: "Review one explicit Git scope along two independent axes: repository standards and fidelity to the originating spec. Use for branch, PR, commit-range, or work-in-progress reviews where both code quality and requested behavior matter."
---

# Code Review

Review one explicit Git scope along two axes:

- **Standards** — does the change follow the repository's documented standards and the smell baseline below?
- **Spec** — does the change faithfully implement the originating issue, PRD, or spec?

Run the axes as independent sub-agent passes so one does not steer the other. Treat their findings as advisory until you verify them against the diff and sources.

Run `$setup-matt-pocock-skills` first if the review needs an issue-tracker workflow and `docs/agents/issue-tracker.md` is missing.

## Process

### 1. Resolve the review scope

Choose exactly one scope from the user's request. Ask only when the scope cannot be inferred safely.

- **Branch or PR against a base** — resolve the base commit, then use `git diff <base>...HEAD` and `git log <base>..HEAD --oneline`.
- **Explicit commit range `A..B`** — resolve both endpoints, then use `git diff A..B` and `git log A..B --oneline`. Do not append another range operator.
- **Work in progress** — use `git diff HEAD` for staged and unstaged tracked changes, `git status --short` for the full inventory, and `git ls-files --others --exclude-standard` for untracked files. Read every untracked file in scope because it has no diff hunk yet.

Record the exact commands and scope once so both review axes inspect the same change set. Stop when references are invalid or when the tracked diff and in-scope untracked file list are both empty.

### 2. Find the spec source

Look in this order:

1. Issue references in in-scope commit messages; fetch them through the configured issue-tracker workflow.
2. A path or URL supplied by the user.
3. A matching file under `docs/`, `specs/`, or `.scratch/`.
4. Ask the user. If no spec exists, skip that axis and report the gap.

### 3. Find the standards sources

Read the repository's coding rules, including relevant `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `CODING_STANDARDS.md`, language guides, and scoped instructions.

Apply the smell baseline below in addition to documented rules:

- **Repository rules override.** Suppress a baseline smell when a documented standard explicitly endorses the pattern.
- **Smells are judgment calls.** Label them as possible smells, never hard violations.
- **Tooling owns mechanical rules.** Skip findings that formatting, linting, typechecking, or other configured tooling already enforces.

Check every changed hunk against these high-signal smells:

- **Mysterious Name** — a name does not reveal what it represents. Rename it; if no honest name appears, clarify the design.
- **Duplicated Code** — the same logic shape appears in multiple hunks. Extract one shared implementation.
- **Feature Envy** — code reaches into another object's data more than its own. Move behavior toward the data it uses.
- **Data Clumps** — the same fields or parameters travel together. Give the group one type.
- **Primitive Obsession** — a primitive stands in for a domain concept. Introduce a focused domain type when it reduces ambiguity.
- **Repeated Switches** — the same branch cascade recurs. Centralize the mapping or use polymorphism when it fits.
- **Shotgun Surgery** — one logical change requires scattered edits. Gather the changing behavior behind one module interface.
- **Divergent Change** — one module changes for unrelated reasons. Split responsibilities along a stable seam.
- **Speculative Generality** — abstractions or hooks exist for needs absent from the spec. Collapse them until a real second use appears.
- **Message Chains** — callers navigate long object chains. Hide the traversal behind a meaningful interface.
- **Middle Man** — a type or function mostly delegates. Remove the layer when it adds no policy or leverage.
- **Refused Bequest** — an implementation ignores most inherited behavior. Prefer composition or a narrower interface.

### 4. Run independent review passes

Spawn Standards and Spec sub-agents in parallel when sub-agents are available. Each delegation must be self-contained: include the user goal, resolved scope, exact diff/status/log commands, every in-scope untracked path, relevant source paths or contents, constraints, what has already been checked, read-only boundaries, and the requested report shape.

**Standards brief**

Ask for every documented-standard violation and every plausible baseline smell, each tied to a file and tight hunk. Require the exact documented rule for hard violations, the smell name for heuristic findings, and a concise explanation of impact. Keep the report under 400 words.

**Spec brief**

Ask for missing or partial requirements, unrequested scope, and behavior that appears implemented incorrectly. Require a quoted or precisely cited spec requirement for every finding. Keep the report under 400 words.

If sub-agents are unavailable, run the same passes sequentially with separate notes so the axes remain independent.

### 5. Verify and report

Check every proposed finding against the source line and changed code. Remove unsupported findings; preserve the axis that produced each valid one.

Present the result under `## Standards` and `## Spec`. Do not merge or rerank across axes. End with the count and worst issue within each axis; do not choose one overall winner.

When there are actionable findings, use tight file and line references. When an axis passes, say what was checked rather than only saying "looks good."

## Why the axes stay separate

A change can follow every standard while implementing the wrong behavior, or match the spec while violating repository conventions. Separate reports prevent either success from masking the other failure.
