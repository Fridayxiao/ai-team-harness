---
name: write-handoff
description: Record useful handoff context and put it in the right place. Reusable project knowledge goes into long-lived docs such as README or AGENTS, while task-specific state goes into a handoff note. Use when pausing, transferring, summarizing progress, preserving debugging or implementation context, preparing a resume note, or recording what the next agent should know.
---

# Write Handoff

## Core Rule

Record useful context where the next person or agent is most likely to look for it.

- Reusable project knowledge belongs in existing long-lived docs, such as README, AGENTS.md, docs, runbooks, architecture notes, or project context files.
- Task- or goal-specific state belongs in a handoff note or chat handoff.
- If both types are present, update the long-lived docs for reusable knowledge and make the handoff point to those docs.

A short handoff is fine. Do not force a rigid template.

## Choose The Destination

Update existing long-lived docs when the information applies beyond the current task:

- Setup, install, run, test, deploy, or troubleshooting commands
- Repository conventions, common workflows, architecture, or important file locations
- Recurring errors and their fixes
- User or team preferences that future work should respect
- Validated external service setup steps
- Domain terms, project background, or important relationships
- Decisions that future work should preserve

Use a task handoff when the information is specific to the current task, goal, branch, or session:

- The exact goal, status, current edits, and relevant artifacts
- What has been completed and what remains
- Temporary debugging state, logs, failed attempts, or things not worth repeating
- Open questions, blockers, risks, assumptions, and unverified areas
- Decisions that only apply to this task
- Concrete next actions for the receiver

Common document targets:

- `README.md`: human-facing overview, setup, usage, and common commands.
- `AGENTS.md`, `CLAUDE.md`, or similar files: agent-facing repo instructions, command preferences, and workflow rules.
- `CONTEXT.md` or docs context files: domain vocabulary, project background, and important relationships.
- `docs/adr/` or architecture notes: significant decisions and tradeoffs. ADR means architecture decision record.
- `docs/runbooks/` or operational docs: repeatable debugging, deployment, maintenance, or recovery procedures.
- Existing PRDs, plans, issues, or design docs: requirements, plans, and status already owned by those artifacts.

If there is no suitable existing doc and creating one would be surprising, report the suggested destination instead of creating a new doc.

## What To Capture

Include whichever details would help the receiver:

- Why the work exists and what outcome is expected
- Current state, status, and relevant artifacts
- Important files, commands, links, branches, commits, issues, or documents
- Decisions made and the reasons behind them
- Constraints, assumptions, risks, blockers, and open questions
- What has been verified and what remains unverified
- User preferences, prior agreements, or context that affects the next move
- Suggested skills, tools, or commands the next agent should consider

## How To Write

- Use concise Markdown.
- Start with enough context for a new reader to orient quickly.
- Preserve facts, decisions, and reasoning rather than a transcript.
- Do not duplicate content already captured in PRDs, plans, architecture notes, issues, commits, diffs, or other artifacts; reference those by path or URL.
- When updating existing docs, make the smallest useful change, match the document style, and avoid unrelated rewrites.
- When writing a task handoff, link to the long-lived docs that now hold reusable context.
- Mark uncertainty directly instead of implying confidence.
- Use specific paths, commands, artifacts, and identifiers when they help.
- Define project-specific shorthand when the receiver may not know it.
- Redact secrets and sensitive information, including API keys, passwords, tokens, private credentials, and unnecessary personal data.
- If the user gives a focus for the next session, tailor the handoff to that focus.
- If context is missing, say what is missing and how that limits the handoff.

## Default Task Handoff Structure

Use this structure when a task-specific handoff fits. Rename, remove, or add sections as needed.

```markdown
# Handoff: <goal>

Date:
Status:

## Context

## Current State

## Completed

## Remaining / Next Actions

## Decisions / Rationale

## Risks / Unknowns

## Useful References

## Suggested Skills / Tools
```

## File Output

- If the information belongs in long-lived project docs, update the appropriate existing file when allowed. Do not create a new handoff file just to store reusable project knowledge.
- If the handoff is task-specific and written to disk, use Markdown.
- Prefer `YYYY-MM-DD-<short-goal>-handoff.md` when no filename is provided for a task-specific handoff.
- If the handoff is delivered in chat, keep it readable and structured.
