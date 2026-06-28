# API Reference Auth And Deployments

- Use when: Working on OAuth provider flows or deployment CRUD/revisions.
- Scope: `/api-reference/auth-service-v2/*` and `/api-reference/deployments-v2/*`.
- Total entries: 24

## Entries

### 1. Authenticate
- URL: https://docs.langchain.com/api-reference/auth-service-v2/authenticate.md
- Summary: Get OAuth token or start authentication flow if needed.

### 2. Check Oauth Token Exists
- URL: https://docs.langchain.com/api-reference/auth-service-v2/check-oauth-token-exists.md
- Summary: Return whether the current user has any tokens for a given provider (across agents).

### 3. Check Workspace Slack Tokens Exist
- URL: https://docs.langchain.com/api-reference/auth-service-v2/check-workspace-slack-tokens-exist.md
- Summary: Check if the workspace has any Slack tokens.

### 4. Create Deployment
- URL: https://docs.langchain.com/api-reference/deployments-v2/create-deployment.md
- Summary: Create a new deployment.

### 5. Create Mcp Oauth Provider
- URL: https://docs.langchain.com/api-reference/auth-service-v2/create-mcp-oauth-provider.md
- Summary: Create an OAuth provider via MCP auto-discovery.

### 6. Create Oauth Provider
- URL: https://docs.langchain.com/api-reference/auth-service-v2/create-oauth-provider.md
- Summary: Create a new OAuth provider manually.

### 7. Delete Deployment
- URL: https://docs.langchain.com/api-reference/deployments-v2/delete-deployment.md
- Summary: Delete a deployment by ID.

### 8. Delete Deployments
- URL: https://docs.langchain.com/api-reference/deployments-v2/delete-deployments.md
- Summary: Delete multiple deployments with partial success support.
- Details:
  - Returns:
  - 200: All deployments deleted successfully
  - 207: Some deployments deleted successfully, some failed

### 9. Delete Oauth Provider
- URL: https://docs.langchain.com/api-reference/auth-service-v2/delete-oauth-provider.md
- Summary: Delete an OAuth provider.

### 10. Delete Oauth Tokens For User
- URL: https://docs.langchain.com/api-reference/auth-service-v2/delete-oauth-tokens-for-user.md
- Summary: Delete all tokens for the current user for the given provider (across agents).

### 11. Get Deployment
- URL: https://docs.langchain.com/api-reference/deployments-v2/get-deployment.md
- Summary: Get a deployment by ID.

### 12. Get Oauth Provider
- URL: https://docs.langchain.com/api-reference/auth-service-v2/get-oauth-provider.md
- Summary: Get a specific OAuth provider.

### 13. Get Revision
- URL: https://docs.langchain.com/api-reference/deployments-v2/get-revision.md
- Summary: Get a revision by ID for a deployment.

### 14. List Deployments
- URL: https://docs.langchain.com/api-reference/deployments-v2/list-deployments.md
- Summary: List all deployments.

### 15. List Oauth Providers
- URL: https://docs.langchain.com/api-reference/auth-service-v2/list-oauth-providers.md
- Summary: List OAuth providers.

### 16. List Revisions
- URL: https://docs.langchain.com/api-reference/deployments-v2/list-revisions.md
- Summary: List all revisions for a deployment.

### 17. Oauth Callback
- URL: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback.md
- Summary: (No one-line summary in source)

### 18. Oauth Callback Get
- URL: https://docs.langchain.com/api-reference/auth-service-v2/oauth-callback-get.md
- Summary: Handle OAuth callback redirect from OAuth providers.
- Details:
  - Processes the OAuth token exchange, then redirects to the frontend callback
  - page for a consistent UI experience.

### 19. Oauth Setup Callback
- URL: https://docs.langchain.com/api-reference/auth-service-v2/oauth-setup-callback.md
- Summary: Handle OAuth setup callback redirect from GitHub Apps.
- Details:
  - This endpoint handles the "Setup URL" callback from GitHub Apps, which is
  - triggered when a user installs or updates their GitHub App installation.
  - For "update" actions (user modified repo access via GitHub), we just show
  - a success page since no token exchange is needed.
  - For new installations with code/state, we process similar to the regular
  - OAuth callback.

### 20. Patch Deployment
- URL: https://docs.langchain.com/api-reference/deployments-v2/patch-deployment.md
- Summary: Patch a deployment by ID.

### 21. Redeploy Revision
- URL: https://docs.langchain.com/api-reference/deployments-v2/redeploy-revision.md
- Summary: Redeploy a specific revision ID.

### 22. Revoke All Slack Tokens For Workspace
- URL: https://docs.langchain.com/api-reference/auth-service-v2/revoke-all-slack-tokens-for-workspace.md
- Summary: Revoke ALL Slack tokens for the workspace. Admin-only action that disconnects Slack entirely.
- Details:
  - This is a destructive operation that:
  - Revokes all Slack tokens on Slack's side for all users in the workspace
  - Deletes all Slack tokens from the database

### 23. Update Oauth Provider
- URL: https://docs.langchain.com/api-reference/auth-service-v2/update-oauth-provider.md
- Summary: Update an OAuth provider.

### 24. Wait For Auth Completion
- URL: https://docs.langchain.com/api-reference/auth-service-v2/wait-for-auth-completion.md
- Summary: Wait for OAuth authentication completion.
