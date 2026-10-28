# Quoting engine for our insurance product

We are an insurance startup selling small-business liability cover in 12 US states. The
quoting engine is our product: brokers use our API to get a price in under 2 seconds.

- About 40 rating factors (industry code, revenue, payroll, claims history, location and more).
- Rate tables are filed with each state regulator and versioned. A quote must be reproducible
  for 7 years with the exact table version used.
- Actuaries change rating rules monthly; today each change needs an engineer.
- Peak 20 quotes/second; 1.5 million quotes a year.
- Our actuarial model and underwriting rules are proprietary and are how we compete. No
  off-the-shelf rating engine supports our rule format; the ones we evaluated would need our
  model rewritten into their DSL, and they cost more than our whole engineering team.

We have 7 engineers and run on one cloud provider.

Please design the quoting engine.

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
