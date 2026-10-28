# Viability gate

Answer briefly, in writing, before any design.

1. **Problem and user.** Who uses this, for what, and how is it done today?
2. **Build vs reuse.** Name the best existing product, library, managed service or OS feature.
   If it covers 80% of the need, the design is "integrate X", not "build X".
3. **Production bill.** What it takes to run this for real, not to demo it: persistence across
   restarts, identity and auth, retries and recovery, upgrades and migrations, retention,
   backups, on-call, security patching.
4. **Owner.** Who runs it after launch, and does the team size match the operational load?
5. **Slop risk.** Will agents build it without a stable architecture, an owner or a way to
   verify behaviour? Will it compete with mature software that has years of production fixes it
   cannot reproduce?

## Cost table

Fill it in for building it and for the best reuse option. Rough numbers are fine; missing
numbers are not.

| | Build | Reuse: <name> |
|---|---|---|
| People-months to first production use | | |
| People-months to the parity users will expect | | |
| Yearly running cost (infrastructure + licences) | | |
| Ongoing people (on-call, patching, upgrades) | | |
| What only this option gives us | | |

If building costs more and the last row is empty for "Build", the verdict is STOP or
GO, NARROWED.

## Verdicts

- **GO**: the need is specific to this business, or no existing option meets a stated
  requirement, and the team can carry the production bill.
- **GO, NARROWED**: build only the part nothing else covers, usually an adapter, plugin or
  thin layer on the reused product. State the reduced scope.
- **STOP**: say what makes it slop-prone, too complex or too costly to run, and name the cheaper
  alternative. Do not design. Continue only if the user explicitly accepts the risk, and record
  that acceptance as decision D1.

Price is not by itself a reason to rebuild commodity software. Compare the licence bill with
the people-months in the table.

## Reference failure

A distributed CI system was built by one engineer and an agent in two months: 12.5k lines and
177 tests, and it worked. Its top-priority backlog was a restart that wiped all build history,
one shared API token, manual retries when a worker died, and unbounded logs. None of that was
hard to code; it was missing because nobody had run the system in production. Parity with the
mature CI it replaced was unreachable. The code was the cheap part.
