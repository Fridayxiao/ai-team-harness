---
name: reuse-opportunity-review
description: Review completed work, existing projects, or mature examples to extract reusable lessons, architecture and module patterns, interface designs, workflows, fixes, conventions, and automation opportunities worth preserving or adapting. Use only when the user explicitly asks to review work, a project, or an example for automation, reuse, lessons learned, knowledge capture, design patterns, architecture notes, or repeated manual work. Do not trigger proactively at the end of normal tasks unless the user asks.
---

# Reuse Opportunity Review

## Philosophy

**Core principle**: Preserve what prevents rediscovery, and extract what is worth reusing elsewhere. Automate only when automation is the best preservation form.

Good reviews are selective and evidence-based. They notice hard-won context, repeated command sequences, known errors and fixes, validation routines, prompt or handoff shapes, project conventions, architecture and module patterns, interface designs, coupling and decoupling choices, and recurring agent workflows that future work should reuse or adapt.

Bad reviews turn every completed task into a backlog. They recommend scripts because scripting is possible, write long implementation plans before the user chooses a candidate, or preserve obvious information that is cheaper to rediscover than maintain.

## Anti-Pattern: Automating Because You Can

**DO NOT recommend automation just because a step was manual.**

This produces poor follow-up work:

- One-off steps become brittle scripts
- Useful lessons get buried inside tooling instead of written down plainly
- Maintenance cost exceeds the cost of repeating the work
- The user receives a backlog instead of a useful shortlist
- Future agents repeat the same misunderstanding because the actual lesson was not captured

**Correct approach**: first decide what should be preserved, then choose the simplest durable form for preserving it.

## Workflow

### 1. Inspect The Existing Work

Review the available evidence from the completed work, project, repo, product, PRs, issues, ADRs, docs, code, tests, commands, artifacts, errors, fixes, and decisions. Separate observed facts from guesses. If context is missing, say what is missing and recommend only candidates supported by available evidence.

### 2. Spot Reusable Signals

Look for repeated steps, fragile command order, manual transformations, known error causes and fixes, validations that should recur, context that had to be rediscovered, cross-tool handoffs, project rules, constraints, terminology, architecture boundaries, module shapes, interface designs, dependency direction, coupling or decoupling choices, style conventions, or low-value manual work with high error risk.

### 3. Filter Hard

Recommend a candidate only when it is likely to repeat, reduces meaningful error risk, preserves hard-won context, captures a transferable design pattern, prevents repeated failed investigation, shortens a known frequent workflow, or captures a rule, decision, or fix that would be expensive to rediscover.

Skip candidates that are merely possible, obvious, unlikely to repeat, or more expensive to maintain than to rediscover.

### 4. Choose The Preservation Form

Choose the lowest-maintenance form that will actually help:

- `error note`: known error, cause, fix, and verification
- `reference`: reusable project knowledge, API behavior, schemas, tool quirks, or decision rules
- `architecture note / ADR`: module boundaries, dependency direction, interface shape, coupling risks, architectural constraints, hard-to-reverse design choices, or why an architectural path was chosen
- `checklist`: ordered verification, release, review, or handoff steps
- `template`: repeated document, prompt, report, spec, or handoff shape
- `script`: deterministic file, data, command, or batch processing
- `command wrapper`: repeated CLI sequence that benefits from one entrypoint
- `workflow`: cross-tool process with clear inputs, outputs, and checkpoints
- `skill`: recurring agent workflow with judgment, branching, or domain context
- `skill update`: improvement to an existing skill based on observed friction

### 5. Return A Short Candidate List

Return only justified candidates, usually 1-5. If none are worth preserving, say so and explain briefly.

Use this compact shape:

```markdown
### <candidate name>

- Preserve: <specific lesson, pattern, design choice, fix, workflow, command sequence, or reusable context>
- Form: <error note | reference | architecture note / ADR | checklist | template | script | command wrapper | workflow | skill | skill update>
- Evidence: <observed command, file, code structure, interface, ADR, doc, error, decision, repeated step, or verification>
- Value: <time saved, error avoided, consistency gained, or context preserved>
- Cost/Priority: <low/medium/high cost; low/medium/high priority>
```

After the list, give one sentence naming the best next candidate to pursue, if any. Do not include an implementation plan by default.

## Checklist Per Review

```text
[ ] Every candidate is grounded in observed work
[ ] The preserved lesson or pattern is concrete enough to reuse or adapt later
[ ] Documentation, architecture notes or ADRs, templates, and skill updates were considered before scripts
[ ] Automation is recommended only when it beats simpler preservation forms
[ ] The output is a shortlist, not a build plan
[ ] User control is preserved: wait for the user to choose what to pursue
```
