# Bank reconciliation tool for finance

Our finance team (4 people) reconciles bank transactions against our billing database every day.
Today two people spend about 3 hours a day matching rows by hand in spreadsheets.

- Around 8,000 bank transactions a day, from two banks' CSV exports (different formats).
- Matching rules specific to us: our invoice number appears in free text in the payment memo,
  customers pay several invoices in one transfer or pay in parts, and FX payments differ by
  small amounts.
- Unmatched items go to a review queue; finance approves matches; everything is audited.
- Our ERP has no reconciliation module. We trialled two reconciliation SaaS products; neither
  could parse our memo format or handle split payments, and both needed bank API integrations
  our banks do not offer.

One developer is available for about 2 months. We run Python services and Postgres.

Please design the tool.

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
