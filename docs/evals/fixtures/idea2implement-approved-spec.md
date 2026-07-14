# Approved Spec Fixture: Decision Register

This fixture is fictional and contains the complete repository context for this evaluation.

**Status:** Approved

## Problem And Outcome

Small engineering teams lose the rationale and ownership behind important decisions. Build a searchable decision register so a teammate can capture a decision in context and later find what was decided, why, and by whom.

## Scope

- Create a decision with title, context, outcome, owner, participants, and decision date.
- View decisions in reverse chronological order.
- Search title, context, and outcome text.
- View one decision at a stable URL.

## Non-Goals

- Approval workflows
- Automated reminders or resurfacing
- Chat, email, or issue-tracker integrations
- Editing or deleting decisions in the first release
- AI-generated summaries

## Accepted Decisions

- Extend the existing React, Node.js, and PostgreSQL application; add no new platform service.
- Keep PostgreSQL as the source of truth.
- Follow the existing authenticated form, route, repository-interface, migration, and behavior-test conventions.
- Use PostgreSQL full-text search through the existing search adapter.
- Treat every decision as immutable in the first release.
- Test through the authenticated HTTP interface and the user-visible browser flow; do not expose a second mutation path for tests.

## Synthetic Repository Context

- Authentication and team membership already exist.
- The application already provides authenticated list, create, and detail-route patterns for team-owned records.
- Database migrations run transactionally and have rollback checks.
- The existing search adapter accepts a team identifier and query text and returns ranked record identifiers.
- Browser tests cover one representative happy path per feature; HTTP behavior tests cover validation, authorization, and persistence.

## Acceptance

- A team member can create a valid decision and immediately open its stable URL.
- Invalid or cross-team submissions are rejected without persistence.
- The list shows the new decision in reverse chronological order.
- Search returns matching decisions only from the active team.
- The HTTP behavior suite, browser happy path, migration check, typecheck, and build pass.

There are no intentionally open product or architecture decisions in this fixture. A reviewer may still report a contradiction that is present in the text, but should not restart generic product discovery.
