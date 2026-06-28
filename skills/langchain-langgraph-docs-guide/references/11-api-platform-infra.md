# API Reference Platform Infra

- Use when: Working on integrations, listeners, sandboxes, pools, templates, volumes.
- Scope: `/api-reference/integrations-v1/*`, `/listeners-v2/*`, `/sandboxes-v2/*`.
- Total entries: 27

## Entries

### 1. Create a Sandbox
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/create-a-sandbox.md
- Summary: Create a new SandboxClaim in tenant's namespace.
- Details:
  - If wait_for_ready is True (default), this will block until the sandbox
  - is ready or the timeout is reached.
  - The sandbox creation can fail for several reasons:
  - Image pull errors (invalid image, registry auth issues)
  - Container crashes (bad entrypoint, missing dependencies, health check failures)
  - Scheduling failures (no suitable nodes available)
  - Sandbox creation is subject to quota limits (count, CPU, memory)
  - configured via Metronome org config.
  - On failure, the claim is automatically cleaned up and a descriptive error
  - is returned.

### 2. Create a Sandbox Pool
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/create-a-sandbox-pool.md
- Summary: Create a new Sandbox Pool in tenant's namespace.
- Details:
  - Pools pre-provision sandboxes from a template for faster claim binding.
  - Requirements:
  - The referenced template must exist
  - The template must not have any volume mounts (volumes are stateful)
  - Pool creation is subject to quota limits. The total resource usage
  - (replicas * per-replica resources) is checked against the organization's
  - quota limits.

### 3. Create a SandboxTemplate
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/create-a-sandboxtemplate.md
- Summary: Create a new SandboxTemplate in tenant's namespace.

### 4. Create a Volume
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/create-a-volume.md
- Summary: Create a new persistent volume in the tenant's sandbox namespace.
- Details:
  - This creates both a PersistentVolume (PV) and PersistentVolumeClaim (PVC).
  - The volume can then be referenced in sandbox templates.
  - Volume creation is subject to quota limits (count and total storage)
  - configured via Metronome org config.
  - If wait_for_ready is True (default), this blocks until the PVC is bound
  - or the timeout is reached.

### 5. Create Listener
- URL: https://docs.langchain.com/api-reference/listeners-v2/create-listener.md
- Summary: Create a listener.<br>
- Details:
  - <br>
  - Creating a listener is only allowed for LangSmith organizations with self-hosted enterprise plans.

### 6. Delete a Sandbox
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/delete-a-sandbox.md
- Summary: Delete a SandboxClaim from tenant's namespace.

### 7. Delete a Sandbox Pool
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/delete-a-sandbox-pool.md
- Summary: Delete a Sandbox Pool from tenant's namespace.
- Details:
  - This will terminate all sandboxes in the pool.

### 8. Delete a SandboxTemplate
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/delete-a-sandboxtemplate.md
- Summary: Delete a SandboxTemplate from tenant's namespace.
- Details:
  - Deletion will fail if the template is in use by any sandboxes or pools.

### 9. Delete a Volume
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/delete-a-volume.md
- Summary: Delete a persistent volume (both PV and PVC) from tenant's namespace.
- Details:
  - This will fail if any templates reference this volume. Delete or update
  - those templates first before deleting the volume.

### 10. Delete Listener
- URL: https://docs.langchain.com/api-reference/listeners-v2/delete-listener.md
- Summary: Delete a listener by ID.

### 11. Get a Sandbox
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/get-a-sandbox.md
- Summary: Get a specific Sandbox by name in tenant's namespace.
- Details:
  - This endpoint queries the database for fast performance.

### 12. Get a Sandbox Pool
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/get-a-sandbox-pool.md
- Summary: Get a specific Sandbox Pool by name in tenant's namespace.
- Details:
  - This endpoint queries the database for fast performance.

### 13. Get a SandboxTemplate
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/get-a-sandboxtemplate.md
- Summary: Get a specific SandboxTemplate by name in tenant's namespace.
- Details:
  - This endpoint queries the database for fast performance.

### 14. Get a Volume
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/get-a-volume.md
- Summary: Get a specific volume by name in the tenant's sandbox namespace.
- Details:
  - This endpoint queries the database for fast performance.

### 15. Get Listener
- URL: https://docs.langchain.com/api-reference/listeners-v2/get-listener.md
- Summary: Get a listener by ID.

### 16. List all Sandbox Pools
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/list-all-sandbox-pools.md
- Summary: List all Sandbox Pools in the tenant's namespace.
- Details:
  - This endpoint queries the database for fast performance.
  - Supports optional pagination via `limit` and `offset` query parameters.

### 17. List all Sandboxes
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/list-all-sandboxes.md
- Summary: List all Sandboxes in the tenant's namespace.
- Details:
  - This endpoint queries the database for fast performance.
  - Supports optional pagination via `limit` and `offset` query parameters.

### 18. List all SandboxTemplates
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/list-all-sandboxtemplates.md
- Summary: List all SandboxTemplates in the tenant's sandbox namespace.
- Details:
  - This endpoint queries the database for fast performance.
  - Supports optional pagination via `limit` and `offset` query parameters.

### 19. List all Volumes
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/list-all-volumes.md
- Summary: List all persistent volumes in the tenant's sandbox namespace.
- Details:
  - This endpoint queries the database for fast performance.
  - Supports optional pagination via `limit` and `offset` query parameters.

### 20. List GitHub Integrations
- URL: https://docs.langchain.com/api-reference/integrations-v1/list-github-integrations.md
- Summary: List available GitHub integrations for LangGraph Platfom Cloud SaaS.

### 21. List GitHub Repositories
- URL: https://docs.langchain.com/api-reference/integrations-v1/list-github-repositories.md
- Summary: List available GitHub repositories for an integration that are available to deploy to LangSmith Deployment.

### 22. List Listeners
- URL: https://docs.langchain.com/api-reference/listeners-v2/list-listeners.md
- Summary: List all listeners.

### 23. Patch Listener
- URL: https://docs.langchain.com/api-reference/listeners-v2/patch-listener.md
- Summary: Patch a listener by ID.

### 24. Update a Sandbox
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/update-a-sandbox.md
- Summary: Update a Sandbox's display name.
- Details:
  - Currently only the display name can be updated.

### 25. Update a Sandbox Pool
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/update-a-sandbox-pool.md
- Summary: Update a Sandbox Pool's display name and/or replica count.
- Details:
  - You can update:
  - **name**: New display name (must be unique within the organization)
  - **replicas**: New replica count (scaling up is subject to quota limits)
  - The template reference cannot be changed after creation.
  - Set replicas to 0 to pause the pool without deleting it.

### 26. Update a SandboxTemplate
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/update-a-sandboxtemplate.md
- Summary: Update a SandboxTemplate's display name.
- Details:
  - Currently only the display name can be updated. The image, resources,
  - and volume mounts cannot be changed after creation.

### 27. Update a Volume
- URL: https://docs.langchain.com/api-reference/sandboxes-v2/update-a-volume.md
- Summary: Update a volume's display name and/or storage size.
- Details:
  - You can update:
  - **name**: New display name (must be unique within the organization)
  - **size**: New storage size (only increases allowed, cannot decrease)
  - The storage increase is subject to quota limits configured via
  - Metronome org config.
