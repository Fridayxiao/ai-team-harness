# Optional Modules

Load this reference when the handoff would benefit from scenario-specific detail beyond the core sections.

Append only the modules that materially improve pickup quality.

## Implementation Details

Use for engineering work, code changes, configuration changes, migrations, or environment setup.

Include:

- Relevant files, directories, modules, or services
- What changed and what did not change
- Entry points, commands, scripts, or feature flags
- Test status, build status, and any missing verification
- Environment dependencies or setup details that could block progress

Skip:

- Obvious code detail that is already clearer in the diff than in prose

## Investigation Trail

Use for debugging, incident response, research, or exploratory work.

Include:

- What was tried
- What was ruled out
- What evidence supports the current theory
- Which leads still look promising
- Which routes are not worth repeating without new evidence

Skip:

- A blow-by-blow log if only two or three findings actually matter

## Agent Relay Notes

Use when another agent will continue the work and context loss is likely.

Include:

- Which judgments were high-confidence versus provisional
- Which assumptions should be re-checked before acting
- Which prior context mattered most in shaping the current plan
- Which tasks are easy to overdo, repeat, or misunderstand
- Which unresolved questions most affect the next decision

Skip:

- Self-referential commentary that does not help the next agent execute
