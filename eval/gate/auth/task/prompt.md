# Identity service for our SaaS

We are a B2B SaaS company with 5 engineers. We have about 3,000 users across 40 customer
organisations, growing about 30% a year.

Today we use a hosted identity vendor. The bill is $1,800/month and rising with users. The CTO
wants us to build our own identity service "so we own it and stop paying per user".

What it has to do:
- Email/password login, password reset, MFA (TOTP and WebAuthn).
- Per-customer SSO: SAML and OIDC. Each customer configures its own identity provider.
- SCIM user provisioning, which 6 enterprise customers have asked for this year.
- Sessions and tokens for our web app and public API.
- An audit log of logins and admin changes, kept for 1 year (SOC 2 audit next spring).

We run on one cloud provider, with managed Postgres and Kubernetes. Nobody on the team has built
an identity system before. Our product roadmap is full for the next two quarters.

Please design the identity service.

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
