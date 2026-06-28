# Maintenance and Refresh

Use this file when the reference catalog needs refresh or consistency checks.

## When To Refresh

Refresh the catalog when:

- Official docs have changed and links look stale.
- A needed URL is missing from routing references.
- Release or migration pages introduce new sections.

## Refresh Procedure

1. Update the raw source list:

```bash
curl -L https://docs.langchain.com/llms.txt -o references/llms.txt
```

2. Rebuild routing references:

```bash
uv run scripts/refresh_catalog.py
```

3. Spot-check generated files:

```bash
ls references/00-catalog-index.md references/31-oss-javascript-deep-agents.md references/32-oss-javascript-langchain.md references/33-oss-javascript-langgraph.md references/41-oss-python-deep-agents.md references/42-oss-python-langchain.md references/43-oss-python-langgraph.md
```

## Guardrails

- Keep generated routing files deterministic; avoid manual edits to generated sections.
- If manual edits are necessary, document why and keep them minimal.
- Re-run the refresh command after script changes to confirm output remains stable.
