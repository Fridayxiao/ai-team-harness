# LangChain Docs Catalog Index (Sharded)

This index is generated from `references/llms.txt`.
Read only the shard that matches the task, then fetch the exact URL(s) you need.
All shards prioritize Overview and Quickstart first when available. LangChain then prioritizes: Agents, Models, Messages, Tools, Runtime, Middleware, Structured output, Multi-agent.

## Global Entry Points

### 00-global-index-and-misc.md
- Entries: 1
- Use when: Need top-level landing/index pages or uncategorized docs.
- Scope: Root pages like docs index and uncommon paths outside major families.

## LangSmith Platform

### 10-api-auth-and-deployments.md
- Entries: 24
- Use when: Working on OAuth provider flows or deployment CRUD/revisions.
- Scope: `/api-reference/auth-service-v2/*` and `/api-reference/deployments-v2/*`.

### 11-api-platform-infra.md
- Entries: 27
- Use when: Working on integrations, listeners, sandboxes, pools, templates, volumes.
- Scope: `/api-reference/integrations-v1/*`, `/listeners-v2/*`, `/sandboxes-v2/*`.

### 20-langsmith-agent-server-api.md
- Entries: 59
- Use when: Implementing or debugging Agent Server endpoints and server-side runtime APIs.
- Scope: `/langsmith/agent-server-api/*` including assistants, threads, runs, MCP, A2A.

### 21-langsmith-agent-build-and-serving.md
- Entries: 23
- Use when: Building/publishing agents or understanding serving entrypoints and remote graph usage.
- Scope: `/langsmith/agent-builder*`, `/langsmith/agent-server*`, `/langsmith/server-*`, `/langsmith/remote-graph*`.

### 22-langsmith-eval-observability-and-quality.md
- Entries: 111
- Use when: Designing evaluation pipelines, tracing, prompt iteration, dataset/feedback quality loops.
- Scope: LangSmith pages containing evaluation, experiment, trace, observability, prompt, dataset, feedback, insights, studio.

### 23-langsmith-deploy-and-self-host.md
- Entries: 45
- Use when: Deploying LangSmith/LangGraph infrastructure or configuring self-hosted setups.
- Scope: LangSmith pages with deploy, deployment, self-host, Kubernetes, Docker, Cloud/Hybrid, control/data plane, scaling.

### 24-langsmith-ops-security-and-admin.md
- Entries: 132
- Use when: Handling platform operations, governance, auth/access, billing, org/workspace administration.
- Scope: Remaining non-API LangSmith docs not matched by other LangSmith shards.

## Deep Agents

### 31-oss-javascript-deep-agents.md
- Entries: 11
- Use when: Building or debugging Deep Agents in JavaScript/TypeScript.
- Scope: `/oss/javascript/deepagents/*`.

### 41-oss-python-deep-agents.md
- Entries: 11
- Use when: Building or debugging Deep Agents in Python.
- Scope: `/oss/python/deepagents/*`.

## LangChain

### 32-oss-javascript-langchain.md
- Entries: 45
- Use when: Building or debugging LangChain JavaScript/TypeScript application logic.
- Scope: `/oss/javascript/langchain/*` with core topics prioritized first.

### 34-oss-javascript-integrations.md
- Entries: 30
- Use when: Selecting and wiring JS/TS providers, chat models, embeddings, retrievers, vector stores, and tools.
- Scope: `/oss/javascript/integrations/*`.

### 42-oss-python-langchain.md
- Entries: 45
- Use when: Building or debugging LangChain Python application logic.
- Scope: `/oss/python/langchain/*` with core topics prioritized first.

### 44-oss-python-integrations.md
- Entries: 19
- Use when: Selecting and wiring Python providers, chat models, embeddings, retrievers, vector stores, and tools.
- Scope: `/oss/python/integrations/*`.

## LangGraph

### 33-oss-javascript-langgraph.md
- Entries: 28
- Use when: Building or debugging LangGraph JavaScript/TypeScript graphs and runtime behavior.
- Scope: `/oss/javascript/langgraph/*`.

### 43-oss-python-langgraph.md
- Entries: 29
- Use when: Building or debugging LangGraph Python graphs and runtime behavior.
- Scope: `/oss/python/langgraph/*`.

## Shared Foundations

### 30-oss-javascript-foundations.md
- Entries: 25
- Use when: Reading shared OSS JavaScript concepts that are not specific to Deep Agents, LangChain, or LangGraph.
- Scope: `/oss/javascript/common-errors.md`, `/oss/javascript/concepts/*`, `/oss/javascript/contributing/*` and other shared pages.

### 40-oss-python-foundations.md
- Entries: 26
- Use when: Reading shared OSS Python concepts that are not specific to Deep Agents, LangChain, or LangGraph.
- Scope: `/oss/python/common-errors.md`, `/oss/python/concepts/*`, `/oss/python/contributing/*` and other shared pages.

## Refresh

Run this to regenerate all shard files after updating `llms.txt`:

```bash
uv run scripts/refresh_catalog.py
```
