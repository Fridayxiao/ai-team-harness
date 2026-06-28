---
name: codex-thread-manager
description: Use when the user asks Codex to manage, inspect, coordinate, continue, message, summarize, organize, rename, pin, archive, hand off, fork, or create Codex threads on their behalf. Operates user-visible Codex threads autonomously within the user's current request, with risk-based user confirmation. Do not use for ordinary internal subagent parallelism or simple implementation tasks.
---

# Codex Thread Manager

Manage user-visible Codex threads on behalf of the user. Inspect threads, clarify their state, send useful follow-ups, collect results, organize threads, and report what changed.

A Codex thread is user-visible and user-owned. Do not treat it as an ordinary internal subagent. For internal parallel work inside the current request, use subagents or multi-agent tools instead of creating user-visible threads.

## Required Start

1. Identify the requested thread operation: inspect, brief, send, collect, organize, continue, create, fork, hand off, or archive.
2. Search for the relevant thread tool if it is not already callable: `list_threads`, `read_thread`, `send_message_to_thread`, `create_thread`, `fork_thread`, `handoff_thread`, `set_thread_pinned`, `set_thread_archived`, or `set_thread_title`.
3. Resolve target threads from the user request, current workspace, thread titles, thread IDs, or recent context.
4. If target threads are ambiguous and guessing would affect user-visible state, ask one concise question.
5. Otherwise proceed within the user's request and report what you did.

## Autonomy And Boundaries

Operate autonomously within the user's current thread-management request.

Do not ask for confirmation for routine thread management: reading, summarizing, comparing, collecting results, drafting scoped briefs, sending follow-ups, sending context updates, sending scoped task briefs, continuing existing work, or renaming threads for clarity.

Use low-frequency operations only when the user asks for them or when the current thread-management goal clearly requires them: pin, unpin, archive, hand off, fork, or create threads. When you use one of these operations, report it to the user afterward.

Ask before acting only when:

- the target thread is unclear;
- creating more than three new threads;
- archiving a thread with unresolved questions, uncollected output, or useful context;
- handing off in a way that changes the goal, ownership, or responsibility boundary;
- sending work that may cause broad code changes, production changes, external-service changes, billing impact, permission changes, or security impact;
- multiple threads may write the same files or make conflicting changes;
- thread outputs conflict and the next step requires a product, architecture, scope, or priority decision from the user.

`create_thread` may be used only when the user's request explicitly authorizes creating or setting up user-visible threads for the current goal.

## Actions

### Inspect

Read one or more threads and identify their purpose, current status, latest meaningful output, blocker or open question, and likely next action.

### Brief

Write self-contained task messages for threads. A self-contained message includes the user goal, task, relevant context, scope, non-scope, expected output, expected evidence, and stop conditions.

### Send

Send follow-ups, clarifications, context updates, task briefs, or continuation messages to existing threads when they are within the user's current request.

Do not send broad implementation instructions when multiple threads may edit the same files unless the user has approved an isolation strategy.

### Collect

Read thread results and synthesize what each thread produced, what is verified, what is unverified, what conflicts exist, what risks remain, and what should happen next.

Thread output is not verified truth. You own synthesis and judgment.

### Organize

Rename threads when clearer titles help the user's current request.

Pin, unpin, archive, hand off, fork, or create threads only when requested or clearly needed. Report these operations afterward.

## Completion

Finish with a concise report covering:

- threads inspected;
- messages sent;
- results collected;
- threads renamed, pinned, unpinned, archived, handed off, forked, or created;
- risks, conflicts, and next actions.
