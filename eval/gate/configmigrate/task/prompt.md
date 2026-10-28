# Config migration to schema v2

We run 1,200 internal services. Each has a YAML config in our own in-house format (v1),
validated by our own tooling. Platform has defined a v2 schema: renamed keys, nested resource
blocks, and secrets moved to references instead of inline values.

- All 1,200 configs must move to v2 within one quarter; v1 support ends after that.
- About 15% of configs use deprecated fields that need a human decision.
- Owners must review a diff for their service before it is merged.
- No external tool knows our format; it is ours.

One platform engineer has 3 weeks for this. The configs live in a monorepo with CI.

Please design the migration.

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
