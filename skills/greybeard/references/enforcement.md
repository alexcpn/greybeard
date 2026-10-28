# Enforceable architecture rules

Coding agents forget prose after context compaction, and they trade rules for convenience. A
rule that matters needs a check that fails the build. The design names each check and what it
asserts; implementation writes it.

## Format in ARCHITECTURE.md

```
### R2 - Only `store/` talks to the database
Why: one owner per dataset; schema changes stay in one place (D4).
Enforced by: dependency rule - no module outside store/ imports the DB driver.
```

A rule with no practical check says `Enforced by: review only`. Keep those few.

## Checks worth naming (pick the 3-7 that guard this design)

| Rule kind | Check |
|---|---|
| Dependency direction, data ownership | Import/dependency rules (import-linter, dependency-cruiser, ArchUnit, depguard, a test that parses imports) |
| No new top-level components or shared util packages | A test that lists allowed top-level packages or services |
| Complete cache keys | A contract test: change each input listed in the key and assert that the key changes |
| Schema and contract compatibility | Schema diff in CI (OpenAPI, protobuf breaking-change check, JSON Schema versions) |
| Per-component budgets | Tests or runtime assertions on timeouts, request and token caps, queue limits |
| Failure semantics | Fault-injection tests: a dependency that fails or times out must give the stated fail-closed result, never a default value |
| Idempotent retries | A test that runs the operation twice and asserts one effect |
| Forbidden patterns | Lint rules: bare `except`, catch-and-continue in aggregates, secrets in config, sleeping retries |
| Size caps on inputs | A test with an over-limit input that expects rejection |

In `decisions.json`, set `enforced_by` on each decision a check guards.
