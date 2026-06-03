---
name: write-handoff
description: Write high-quality, complete handoffs for ongoing or paused work. Use when an agent needs to transfer project background, current state, completed and remaining work, verified and unverified findings, key decisions, risks, blockers, assumptions, and next actions to another agent or human. Trigger for project handoffs, implementation handoffs, debugging progress summaries, agent relay notes, and pause/resume transitions.
---

# Write Handoff

## Overview

Write a balanced, complete handoff in Markdown that lets another agent or human resume work without rediscovering the important context. Optimize for transfer of decision quality, execution readiness, and risk awareness rather than for exhaustive transcripts.

## Core Workflow

### 1. Reconstruct the context before writing

- Gather enough background to explain why the work exists, why it matters, and how it reached the current state.
- Separate facts from inferences. If key context is missing, say so explicitly instead of filling gaps with guesses.
- Prefer the smallest set of details that preserves correct pickup decisions.

### 2. Start with a zero-context primer

Assume the next reader does not know the project, the subsystem names, or the team vocabulary.

Before the main handoff sections, briefly explain:

- what this part of the system does in plain English
- what is going wrong or what work is in progress
- why it matters to users, the project, or the next milestone
- any project-specific terms the reader must understand

If a project term, internal component name, or acronym appears for the first time, define it immediately in plain English before relying on it.

### 3. Use the core handoff structure every time

Write these sections in order. Keep them short for simple work and expand only where the extra detail helps the next person act correctly.

#### Background

Explain the project or task context, what triggered the work, and any relevant process history.

#### Goal and Scope

State the intended outcome of this work and the boundary of what this handoff covers.

#### Current State

Describe the present situation as directly as possible. Prioritize observable state, existing artifacts, and the latest known results.

#### Completed / Remaining

Split finished work from unfinished work so the handoff boundary is obvious.

#### Verified / Unverified

Separate confirmed facts from expectations, partial checks, or untested assumptions.

#### Key Decisions and Rationale

Record the decisions that affect future work, including important alternatives that were rejected and why.

#### Risks / Blockers / Assumptions

Surface uncertainty, external dependencies, hidden constraints, and likely failure points.

#### Next Actions

Give concrete next steps. Prefer actionable instructions over broad direction.

### 4. Add scenario-specific modules only when they add real pickup value

Read [references/optional-modules.md](references/optional-modules.md) when the work includes engineering changes, debugging or investigation, or agent-to-agent relay. Append only the modules that materially reduce re-discovery for the next person.

### 5. Keep the handoff honest and decision-useful

- Distinguish fact, judgment, assumption, and recommendation.
- Mark missing evidence instead of implying confidence.
- Preserve the reasoning behind non-obvious choices.
- Compress low-value chronology. Keep only the history that changes what the next person should do.
- Explain user-visible impact before diving into internal architecture.
- Translate project-specific language into general language before using it as shorthand.

### 6. Run the quality gate before finishing

Use [references/quality-bar.md](references/quality-bar.md) for the full standard. At minimum, confirm that:

- A new reader can understand the background, goal, and current state within about 1 minute.
- A new reader can understand the problem and why it matters without already knowing the project vocabulary.
- The handoff clearly separates completed from remaining work.
- The handoff clearly separates verified from unverified information.
- The handoff preserves the reasons behind key decisions.
- The handoff exposes the risks, blockers, and assumptions that could change the next move.
- The next actions are concrete enough to start immediately.

### 7. Use the standard handoff format and filename when creating an artifact

- Write the handoff in Markdown.
- If the handoff is delivered in chat, keep it Markdown-structured with headings.
- If the handoff is written to disk, save it as `YYYY-MM-DD-<current-goal>-handoff.md`.
- Derive `<current-goal>` from the immediate handoff objective, not the broad project name.
- Convert `<current-goal>` to short kebab-case.
- Prefer adding a short metadata block near the top with date, current goal, and current status. Include audience only if it is known and useful.

## Output Rules

- Use direct headings and concise paragraphs or bullets.
- Output the handoff in Markdown by default.
- When writing a file, use the filename pattern `YYYY-MM-DD-<current-goal>-handoff.md`.
- Write for a reader with little or no prior project context.
- Introduce the system or subsystem in plain English before using internal names heavily.
- Define project-specific terms, abbreviations, and component names on first use.
- Prefer user-facing problem statements before codebase-internal descriptions.
- Prefer specific file paths, commands, artifacts, and decision points over vague summaries.
- Keep the tone factual and handoff-oriented, not celebratory.
- If confidence is limited because context is missing, say what is missing and how that limits the handoff.
- Do not present the handoff as complete if the missing context would materially affect execution.
