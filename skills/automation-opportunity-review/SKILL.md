---
name: automation-opportunity-review
description: Review recent completed work to identify reusable knowledge and lightweight automation opportunities worth preserving. Use only when the user explicitly asks to find reusable lessons, preserve hard-won context, review a completed workflow for automation or knowledge candidates, capture error-resolution notes, reduce repeated manual work, or run an automation/reuse opportunity review. Do not trigger proactively at the end of normal tasks unless the user asks.
---

# Automation Opportunity Review

## Overview

Review a recently completed collaboration and identify practical reusable assets worth preserving. Include automation opportunities, but do not limit the review to automation. Look for knowledge, errors and fixes, command sequences, validation steps, templates, references, workflows, and skill updates that would help a future person or agent avoid rediscovery.

Optimize for a short, user-controlled follow-up: produce a candidate list, not an implementation plan.

## Invocation Rules

- Use this skill only after the user explicitly asks for an automation, reuse, knowledge-capture, or lessons-learned opportunity review.
- Do not invoke this skill automatically at the end of normal work.
- Do not create scripts, references, skills, notes, or detailed plans unless the user explicitly asks to continue with a specific recommendation.
- Keep the default output short enough to scan quickly.

## Review Scope

Look for reusable candidates in these areas:

- Automation: repetitive formatting, conversion, extraction, generation, cleanup, reporting, command sequences, test/lint/build loops, release steps, PR preparation, or cross-tool pipelines.
- Knowledge: errors encountered, root causes, fixes, tool quirks, API behavior, setup constraints, permissions, environment assumptions, and deprecation or version findings.
- Process: checklists, verification routines, handoff shapes, prompt shapes, review criteria, and decision flows that should be repeated consistently.
- Project context: local conventions, directory layouts, schemas, commands, ownership boundaries, integration rules, or source-of-truth files that future work should reuse.
- Agent capability: recurring judgment-heavy workflows that may deserve a skill, reference, template, or update to an existing skill.

Ignore candidates that are unlikely to repeat, are too obvious to preserve, or would cost more to maintain than to rediscover.

## Core Workflow

### 1. Reconstruct the recent work

Review the visible conversation, commands, files touched, artifacts produced, verification steps, errors, fixes, and decisions made. Separate observed facts from guesses. If context is insufficient, say what is missing and only recommend candidates supported by available evidence.

### 2. Identify reusable signals

Look for:

- steps performed more than once
- commands that had to be run in a specific order
- manual transformations that could be scripted or templated
- errors whose cause and fix are now known
- validations that should become a checklist
- context that had to be rediscovered
- cross-tool handoffs that could be wrapped into a repeatable workflow
- decisions, constraints, or terminology that future agents should know
- low-value manual work with high error risk

### 3. Apply the preservation filter

Recommend a candidate only when at least one condition is true:

- It is likely to repeat at least 3 times.
- It reduces meaningful error risk.
- It preserves hard-won context that was not obvious at the start.
- It prevents future agents from repeating investigation or failed attempts.
- It shortens a workflow that is already known to be frequent.
- It captures a rule, constraint, or fix that would be expensive to rediscover.

Avoid recommending something only because it is technically possible to automate or document.

### 4. Choose the smallest useful form

Prefer the smallest durable form:

- `error note`: known error, cause, fix, and verification
- `reference`: reusable project knowledge, API details, schemas, tool behavior, or decision rules
- `checklist`: ordered human-in-the-loop verification or release/review steps
- `template`: repeated document, prompt, report, spec, or handoff shape
- `script`: deterministic file, data, command, or batch processing
- `command wrapper`: repeated CLI sequence that benefits from one entrypoint
- `workflow`: cross-tool process with clear inputs, outputs, and checkpoints
- `skill`: recurring agent workflow with judgment, branching, or domain context
- `skill update`: improvement to an existing skill based on observed friction

## Default Output

Return 3-5 candidates. If fewer than 3 are genuinely justified, return fewer and say why. Use this format:

```markdown
### 1. <candidate name>

- Reuse point: <specific reusable lesson, process, or repeated/fragile step>
- Suggested form: <error note | reference | checklist | template | script | command wrapper | workflow | skill | skill update>
- What to preserve: <the concrete knowledge, command sequence, template shape, or automation target>
- Evidence from recent work: <observed command, file, error, decision, or repeated step>
- Why it is worth preserving: <time, error reduction, consistency, or context reuse benefit>
- Cost: <low | medium | high>
- Priority: <high | medium | low>
```

After the list, add a one-sentence recommendation naming the single best candidate to pursue next, if any. Do not include a detailed implementation plan by default.

## Quality Bar

- Be selective. A shorter useful list is better than a padded list.
- Keep each candidate grounded in observed recent work.
- Distinguish automation from documentation. Sometimes the right answer is an error note, checklist, reference, or skill update, not code.
- Prefer low-maintenance preservation over brittle machinery.
- Preserve user control: present options and wait for the user to choose whether to go deeper.
