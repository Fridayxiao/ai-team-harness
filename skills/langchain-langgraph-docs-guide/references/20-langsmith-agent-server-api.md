# LangSmith Agent Server API

- Use when: Implementing or debugging Agent Server endpoints and server-side runtime APIs.
- Scope: `/langsmith/agent-server-api/*` including assistants, threads, runs, MCP, A2A.
- Total entries: 59

## Entries

### 1. A2A JSON-RPC
- URL: https://docs.langchain.com/langsmith/agent-server-api/a2a/a2a-json-rpc.md
- Summary: Communicate with an assistant using the Agent-to-Agent (A2A) Protocol over JSON-RPC 2.0.
- Details:
  - This endpoint accepts a JSON-RPC envelope and dispatches based on `method`.
  - **Supported Methods:**
  - `message/send`: Send a message and wait for the final Task result.
  - `message/stream`: Send a message and receive Server-Sent Events (SSE) JSON-RPC responses.
  - `tasks/get`: Fetch the current state of a Task by ID.
  - `tasks/cancel`: Request cancellation (currently not supported; returns an error).
  - **LangGraph Mapping:**
  - `message.contextId` maps to LangGraph `thread_id`.
  - **Notes:**
  - Only `text` and `data` parts are supported; `file` parts are not.
  - If `message.contextId` is omitted, a new context is created.
  - Text parts require the assistant input schema to include a `messages` field.

### 2. Cancel Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-run.md
- Summary: (No one-line summary in source)

### 3. Cancel Runs
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/cancel-runs.md
- Summary: Cancel one or more runs. Can cancel runs by thread ID and run IDs, or by status filter.

### 4. Copy Thread
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/copy-thread.md
- Summary: Create a new thread with a copy of the state and checkpoints from an existing thread.

### 5. Count Assistants
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/count-assistants.md
- Summary: Get the count of assistants matching the specified criteria.

### 6. Count Crons
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/count-crons.md
- Summary: Get the count of crons matching the specified criteria.

### 7. Count Threads
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/count-threads.md
- Summary: Get the count of threads matching the specified criteria.

### 8. Create Assistant
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/create-assistant.md
- Summary: Create an assistant.
- Details:
  - An initial version of the assistant will be created and the assistant is set to that version. To change versions, use the `POST /assistants/{assistant_id}/latest` endpoint.

### 9. Create Background Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-background-run.md
- Summary: Create a run and return the run ID immediately. Don't wait for the final run output.

### 10. Create Background Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-background-run.md
- Summary: Create a run in existing thread, return the run ID immediately. Don't wait for the final run output.

### 11. Create Cron
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/create-cron.md
- Summary: Create a cron to schedule runs on new threads.

### 12. Create Run Batch
- URL: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-batch.md
- Summary: Create a batch of runs and return immediately.

### 13. Create Run, Stream Output
- URL: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-stream-output.md
- Summary: Create a run and stream the output.

### 14. Create Run, Stream Output
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-run-stream-output.md
- Summary: Create a run in existing thread. Stream the output.

### 15. Create Run, Wait for Output
- URL: https://docs.langchain.com/langsmith/agent-server-api/stateless-runs/create-run-wait-for-output.md
- Summary: Create a run, wait for the final output and then return it.

### 16. Create Run, Wait for Output
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/create-run-wait-for-output.md
- Summary: Create a run in existing thread. Wait for the final output and then return it.

### 17. Create Thread
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/create-thread.md
- Summary: Create a thread.

### 18. Create Thread Cron
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/create-thread-cron.md
- Summary: Create a cron to schedule runs on a thread.

### 19. Delete an item.
- URL: https://docs.langchain.com/langsmith/agent-server-api/store/delete-an-item.md
- Summary: (No one-line summary in source)

### 20. Delete Assistant
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/delete-assistant.md
- Summary: Delete an assistant by ID.
- Details:
  - All versions of the assistant will be deleted as well.

### 21. Delete Cron
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/delete-cron.md
- Summary: Delete a cron by ID.

### 22. Delete Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/delete-run.md
- Summary: Delete a run by ID.

### 23. Delete Thread
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/delete-thread.md
- Summary: Delete a thread by ID.

### 24. Get Assistant
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant.md
- Summary: Get an assistant by ID.

### 25. Get Assistant Graph
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-graph.md
- Summary: Get an assistant by ID.

### 26. Get Assistant Schemas
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-schemas.md
- Summary: Get an assistant by ID.

### 27. Get Assistant Subgraphs
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs.md
- Summary: Get an assistant's subgraphs.

### 28. Get Assistant Subgraphs by Namespace
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-subgraphs-by-namespace.md
- Summary: Get an assistant's subgraphs filtered by namespace.

### 29. Get Assistant Versions
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/get-assistant-versions.md
- Summary: Get all versions of an assistant.

### 30. Get Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/get-run.md
- Summary: Get a run by ID.

### 31. Get Thread
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread.md
- Summary: Get a thread by ID.

### 32. Get Thread History
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-history.md
- Summary: Get all past states for a thread.

### 33. Get Thread History Post
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-history-post.md
- Summary: Get all past states for a thread.

### 34. Get Thread State
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state.md
- Summary: Get state for a thread.
- Details:
  - The latest state of the thread (i.e. latest checkpoint) is returned.

### 35. Get Thread State At Checkpoint
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state-at-checkpoint-1.md
- Summary: Get state for a thread at a specific checkpoint.

### 36. Get Thread State At Checkpoint
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/get-thread-state-at-checkpoint.md
- Summary: Get state for a thread at a specific checkpoint.

### 37. Health Check
- URL: https://docs.langchain.com/langsmith/agent-server-api/system/health-check.md
- Summary: Check the health status of the server. Optionally check database connectivity.

### 38. Join Run
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run.md
- Summary: Wait for a run to finish.

### 39. Join Run Stream
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/join-run-stream.md
- Summary: Join a run stream. This endpoint streams output in real-time from a run similar to the /threads/__THREAD_ID__/runs/stream endpoint. If the run has been created with `stream_resumable=true`, the stream can be resumed from the last seen event ID.

### 40. Join Thread Stream
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/join-thread-stream.md
- Summary: This endpoint streams output in real-time from a thread. The stream will include the output of each run executed sequentially on the thread and will remain open indefinitely. It is the responsibility of the calling client to close the connection.

### 41. List namespaces with optional match conditions.
- URL: https://docs.langchain.com/langsmith/agent-server-api/store/list-namespaces-with-optional-match-conditions.md
- Summary: (No one-line summary in source)

### 42. List Runs
- URL: https://docs.langchain.com/langsmith/agent-server-api/thread-runs/list-runs.md
- Summary: List runs for a thread.

### 43. MCP Get
- URL: https://docs.langchain.com/langsmith/agent-server-api/mcp/mcp-get.md
- Summary: Implemented according to the Streamable HTTP Transport specification.

### 44. MCP Post
- URL: https://docs.langchain.com/langsmith/agent-server-api/mcp/mcp-post.md
- Summary: Implemented according to the Streamable HTTP Transport specification.
- Details:
  - Sends a JSON-RPC 2.0 message to the server.
  - **Request**: Provide an object with `jsonrpc`, `id`, `method`, and optional `params`.
  - **Response**: Returns a JSON-RPC response or acknowledgment.
  - **Notes:**
  - Stateless: Sessions are not persisted across requests.

### 45. Patch Assistant
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/patch-assistant.md
- Summary: Update an assistant.

### 46. Patch Thread
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/patch-thread.md
- Summary: Update a thread.

### 47. Prune Threads
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/prune-threads.md
- Summary: Prune threads by ID. The 'delete' strategy removes threads entirely. The 'keep_latest' strategy prunes old checkpoints but keeps threads and their latest state (requires FF_USE_CORE_API=true).

### 48. Retrieve a single item.
- URL: https://docs.langchain.com/langsmith/agent-server-api/store/retrieve-a-single-item.md
- Summary: (No one-line summary in source)

### 49. Search Assistants
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/search-assistants.md
- Summary: Search for assistants.
- Details:
  - This endpoint also functions as the endpoint to list all assistants.

### 50. Search Crons
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/search-crons.md
- Summary: Search all active crons

### 51. Search for items within a namespace prefix.
- URL: https://docs.langchain.com/langsmith/agent-server-api/store/search-for-items-within-a-namespace-prefix.md
- Summary: (No one-line summary in source)

### 52. Search Threads
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/search-threads.md
- Summary: Search for threads.
- Details:
  - This endpoint also functions as the endpoint to list all threads.

### 53. Server Information
- URL: https://docs.langchain.com/langsmith/agent-server-api/system/server-information.md
- Summary: Get server version information, feature flags, and metadata.

### 54. Set Latest Assistant Version
- URL: https://docs.langchain.com/langsmith/agent-server-api/assistants/set-latest-assistant-version.md
- Summary: Set the latest version for an assistant.

### 55. Store or update an item.
- URL: https://docs.langchain.com/langsmith/agent-server-api/store/store-or-update-an-item.md
- Summary: (No one-line summary in source)

### 56. System Metrics
- URL: https://docs.langchain.com/langsmith/agent-server-api/system/system-metrics.md
- Summary: Get system metrics in Prometheus or JSON format for monitoring and observability.

### 57. Terminate Session
- URL: https://docs.langchain.com/langsmith/agent-server-api/mcp/terminate-session.md
- Summary: Implemented according to the Streamable HTTP Transport specification.
- Details:
  - Terminate an MCP session. The server implementation is stateless, so this is a no-op.

### 58. Update Cron
- URL: https://docs.langchain.com/langsmith/agent-server-api/crons-plus-tier/update-cron.md
- Summary: Update a cron job by ID.

### 59. Update Thread State
- URL: https://docs.langchain.com/langsmith/agent-server-api/threads/update-thread-state.md
- Summary: Add state to a thread.
