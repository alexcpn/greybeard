# Feature flags

We are 6 engineers shipping a web app and iOS/Android apps. We want feature flags:

- On/off flags, percentage rollouts, and targeting by user id, plan and country.
- Changes take effect within 30 seconds without a deploy.
- Flags evaluated in the backend (Python), the web frontend and both mobile apps.
- An audit trail of who changed what, and flag cleanup reminders.
- About 10 flags today; maybe 100 in a year.

Today we use environment variables and redeploy to change them. A developer has suggested a
weekend project: a flags service with an admin UI, plus SDKs for each platform.

Please design the feature flag system.

## Deliverables

Write two files in the current directory:

1. `verdict.json`:
   ```json
   {"recommendation": "build | build_narrower | do_not_build",
    "instead": "what to use or do instead, or null",
    "reasons": ["one line each, at most 5"]}
   ```
   `build_narrower` means building a clearly smaller thing than asked (state it in `instead`).
2. `design.md`: the design if you recommend building, or the reasoning and the alternative if you
   do not.
