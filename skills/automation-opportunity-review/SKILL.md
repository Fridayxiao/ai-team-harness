---
name: automation-opportunity-review
description: Review recent completed work to identify lightweight automation opportunities in file/document processing, code workflows, and cross-tool pipelines. Use only when the user explicitly asks to find automation opportunities, reduce repeated manual work, review a completed workflow for automation candidates, or run an automation opportunity review. Do not trigger proactively at the end of normal tasks unless the user asks.
---

# Automation Opportunity Review

## Overview

Review a recently completed collaboration and identify practical opportunities to reduce repeated manual work. Optimize for lightweight, user-controlled follow-up: produce a short candidate list, not an implementation plan.

## Invocation Rules

- Use this skill only after the user explicitly asks for an automation opportunity review or asks what parts of recent work could be automated.
- Do not invoke this skill automatically at the end of normal work.
- Do not implement automation, create scripts, create new skills, or write detailed plans unless the user explicitly asks to continue with a specific recommendation.
- Keep the default output short enough to scan quickly.

## Review Scope

Focus on automation opportunities from these areas:

- File and document processing: repetitive formatting, conversion, extraction, generation, cleanup, reporting, or handoff work.
- Code workflows: repeated commands, setup steps, test/lint/build loops, release notes, changelogs, commits, PR preparation, project scaffolding, or recurring fixes.
- Cross-tool pipelines: workflows that require switching between CLI tools, APIs, browser steps, web research, local files, and generated artifacts.

Ignore work that is unlikely to repeat or that would cost more to automate than to perform manually.

## Core Workflow

### 1. Reconstruct the recent work

Review the visible conversation, commands, files touched, artifacts produced, verification steps, and decisions made. Separate observed facts from guesses. If the recent context is insufficient, say what is missing and still provide only the candidates supported by available evidence.

### 2. Identify repeated or fragile signals

Look for:

- steps performed more than once
- manual transformations that could be scripted or templated
- commands that must be remembered in a specific order
- recurring searches for the same kind of information
- context that had to be rediscovered
- validations that should become a checklist
- cross-tool handoffs that could be wrapped into a repeatable workflow
- low-value manual work with high error risk

### 3. Apply the automation filter

Recommend a candidate only when at least one condition is true:

- It is likely to repeat at least 3 times.
- It reduces meaningful error risk.
- It preserves hard-won context for future work.
- It shortens a workflow that is already known to be frequent.

Avoid recommending automation only because something is technically possible.

### 4. Choose the right automation form

Prefer the smallest useful form:

- `script`: deterministic file, data, command, or batch processing
- `checklist`: ordered human-in-the-loop verification
- `template`: repeated document, prompt, report, spec, or handoff shape
- `skill`: recurring agent workflow with judgment, branching, or domain context
- `reference`: reusable project knowledge, API details, schemas, or decision rules
- `command wrapper`: a repeated CLI sequence that benefits from a single entrypoint
- `workflow`: a cross-tool process with clear inputs, outputs, and checkpoints

## Default Output

Return 3-5 candidates. If fewer than 3 are genuinely justified, return fewer and say why. Use this format:

```markdown
### 1. <candidate name>

- Automation point: <specific repeated or fragile step>
- Suggested form: <script | checklist | template | skill | reference | command wrapper | workflow>
- Why it is worth considering: <time, error reduction, consistency, or context reuse benefit>
- Cost: <low | medium | high>
- Priority: <high | medium | low>
```

After the list, add a one-sentence recommendation naming the single best candidate to pursue next, if any. Do not include a detailed implementation plan by default.

## Quality Bar

- Be selective. A shorter useful list is better than a padded list.
- Keep each candidate grounded in observed recent work.
- Distinguish automation from documentation. Sometimes the right answer is a checklist or reference, not code.
- Prefer low-maintenance automation over brittle multi-step machinery.
- Preserve user control: present options and wait for the user to choose whether to go deeper.
