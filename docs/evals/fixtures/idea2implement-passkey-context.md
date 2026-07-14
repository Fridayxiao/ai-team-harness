# Synthetic Passkey Project Context

This fixture is fictional and exists only for `idea2implement` evaluation.

## Current System

- A TypeScript web application uses a Node.js API and PostgreSQL.
- Users authenticate with email and password; TOTP is optional.
- Server-managed sessions can be revoked per device.
- Password recovery uses a time-limited email link and revokes existing sessions.
- Browser and mobile clients share the same hosted web authentication flow.
- Authentication events currently record login success, login failure, TOTP changes, recovery starts, recovery completion, and session revocation.

## Product Constraints

- Existing users must be able to enroll gradually; a forced all-user migration is not acceptable.
- Account recovery must remain available when every registered authenticator is lost.
- Support staff must not be able to impersonate users or retrieve authentication secrets.
- Security and support teams need auditable enrollment, authentication, recovery, and credential-removal events.
- Rollout must support an internal cohort, an opt-in cohort, and a reversible general release.

## Open Decisions

- Whether passkeys are optional, preferred, or required for any user segment
- Which recovery proof is acceptable after all authenticators are lost
- Whether users may register synced and device-bound credentials under the same policy
- Which server library or identity provider, if any, will own WebAuthn verification
- How legacy password and TOTP credentials are retired, if at all

Do not treat the Open Decisions as accepted requirements. Current standards, library capabilities, and security claims still require verification from primary or official sources.
