# Changelog

## 0.1.0-beta.3 (2026-11-14)

- The optional guidance link to salespeak.ai/agent-screened-email in sender evidence requests is now **off by default**. It is opt-in, the same as attribution. Screening itself stays off until separately approved.
- Existing beta.2 setups that already approved sender screening: say `Turn off the screening guidance link` to match the new default.
- No other behavior changes. No new permissions, schedules or telemetry.

<!-- BEGIN D1-D2A 2026-11-06 -->
## 0.1.0-beta.2 (2026-11-06): D1 + D2a

- Added optional manual, unbranded email signature copy and public landing-page component (website integration separate).
- Added structured, first-line AI-disclosed sender evidence request; independently controlled guidance link; explicit opt-in skill attribution (default off); upgrade consent guidance and status controls.
- Clarified personal-agent portability versus host-specific permissions and autonomous-send verification; retained all original sending safeguards. No D2b protocol or telemetry.
<!-- END D1-D2A 2026-11-06 -->

## 0.1.0-beta.1 (2026-11-06)

- Consolidated portable skill, onboarding, autonomy lifecycle, feedback and public opportunity research.
- Added explicit agent-to-agent permission gates and an experimental local company-agent conversation reference client.
- Added GitHub publishing documents, user FAQ, acceptance tests, Grok template and release checklist.
- No new user permissions or scheduled tasks are enabled by installing this update.
- Repository publication: Salespeak maintainer disclosure in README, MIT copyright set to Salespeak, maintainer process docs moved to `docs/maintainers/`, private vulnerability reporting via GitHub, unverified host product names replaced with generic wording.
