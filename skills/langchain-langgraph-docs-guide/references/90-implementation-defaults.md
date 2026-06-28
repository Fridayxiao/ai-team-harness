# Implementation Defaults

Use this file when multiple implementation paths are valid and you need a safe default recommendation.

## Decision Matrix

| Situation | Default | Why |
| --- | --- | --- |
| Standard production tool-calling agent | `langchain.agents.create_agent` | Good default with built-in LangGraph runtime features for persistence and streaming |
| Need explicit graph topology and custom control flow | LangGraph Graph API | Best for clear state transitions and branching logic |
| Need minimal refactor from function-first code | LangGraph Functional API | Keeps function-first style while adopting LangGraph runtime |
| Need higher autonomy with planning or subagents | Deep Agents | Better fit for long-running or open-ended agent tasks |
| Existing code uses `create_react_agent` | Migrate to `create_agent` | v1 guidance favors `create_agent` over older ReAct helper patterns |

## Recommendation Pattern

When you recommend an option:

1. Name the default.
2. Give one short reason linked to task constraints.
3. Give one alternative and when to pick it.
4. Cite the official URL(s) used to support the decision.

## Pre-Answer Verification Checklist

- Confirm exact API names and import paths from fetched pages.
- Confirm version-specific notes from release or migration docs.
- Confirm deprecation status before final recommendation.
