---
name: write-handoff
description: Record useful handoff context for another person or agent taking over work. Use when pausing, transferring, summarizing progress, preserving debugging or implementation context, preparing a resume note, or recording what the next agent should know.
---

# Write Handoff

## Core Rule

Record anything that would help the next person or agent continue correctly without rediscovering important context.

Do not force a rigid template. Choose the headings and level of detail that fit the work. A short handoff is fine when the situation is simple.

## What To Capture

Include whichever details would help the receiver:

- Why the work exists and what outcome is expected
- Current state, status, and relevant artifacts
- What has been completed and what remains
- Important files, commands, links, branches, commits, issues, or documents
- Decisions made and the reasons behind them
- Constraints, assumptions, risks, blockers, and open questions
- What has been verified and what remains unverified
- Debugging findings, dead ends, and things not worth repeating
- User preferences, prior agreements, or context that affects the next move
- Suggested skills, tools, or commands the next agent should consider
- Concrete next actions

## How To Write

- Use concise Markdown.
- Start with enough context for a new reader to orient quickly.
- Preserve facts, decisions, and reasoning rather than a transcript.
- Do not duplicate content already captured in PRDs, plans, ADRs, issues, commits, diffs, or other artifacts; reference those by path or URL.
- Mark uncertainty directly instead of implying confidence.
- Use specific paths, commands, artifacts, and identifiers when they help.
- Define project-specific shorthand when the receiver may not know it.
- Redact secrets and sensitive information, including API keys, passwords, tokens, private credentials, and unnecessary personal data.
- If the user gives a focus for the next session, tailor the handoff to that focus.
- If context is missing, say what is missing and how that limits the handoff.

## Default Structure

Use this structure when it fits. Rename, remove, or add sections as needed.

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

- If the handoff is written to disk, use Markdown.
- Prefer `YYYY-MM-DD-<short-goal>-handoff.md` when no filename is provided.
- If the handoff is delivered in chat, keep it readable and structured.
