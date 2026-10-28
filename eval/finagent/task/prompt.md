# Design Task: LLM portfolio research agent

You are the architect. Produce a design for the system below. You have no code to look at;
everything you know is in this document.

## Context

A single developer, who is also the main user, wants an LLM-based research assistant for their
own equity portfolio. Every few days they export holdings from their broker and want a research
report: per holding, what the evidence says, and an opinion, each claim traceable to a source.
They may later share it with a few friends who would run it on their own portfolios.

## Facts

| Item | Value |
|---|---|
| Portfolio | ~40 holdings, Indian equities (NSE/BSE), exported from the broker as CSV: ticker, quantity, average cost, sometimes last price. Exports are messy: renamed columns, blank rows, ticker formats vary, free-text fields |
| Data sources | (a) a paid market-research provider exposed as an MCP server: technical indicators, price quotes, broker research summaries; billed per call, ~60 calls/min limit. (b) a paid web-search API exposed as an MCP server, billed per search. (c) company filings and investor presentations: PDFs of 2–20 MB on company websites, change roughly quarterly |
| LLM | Hosted API by default, billed per token; must be switchable to another hosted provider or a local model (8–30B, weaker at tool calling and structured output) with configuration only |
| Budget | A full portfolio run should cost under US$2 and finish in under 15 minutes |
| Runtime | The developer's laptop (32 GB RAM), Docker available; runs on demand, optionally from CI |
| Regulation and safety | It must not give personalised investment advice: no price targets, no position sizing, no "buy X" instructions. Opinions are allowed only as clearly labelled research views with evidence and risks |
| Behaviour | LLM output is non-deterministic. The developer changes prompts and models often and has been burnt by a prompt tweak that silently made reports worse |
| Team | 1 developer, Python, evenings and weekends |

## User stories

1. As the user, I give a holdings CSV and get a portfolio report: portfolio-level summary plus a
   section per holding with evidence, risks and a research view.
2. As the user, I can ask for a deep dive on a single ticker.
3. As the user, the report reflects today's macro/market news relevant to my holdings.
4. As the user, company research (filings, presentations) is reused between runs and refreshed
   when stale, and every statement from it links to the stored source.
5. As the user, I choose an analysis lens (for example "quality compounding" or "deep value")
   that the agent must test, including evidence against it, rather than argue for.
6. As the user, weeks later I can see whether past research views were right, judged against
   what prices actually did, not against the model's own recollection.
7. As the developer, when I change a prompt or model, I find out before using it whether
   answers got worse, and this can run in CI.
8. As the developer, I can see for any run which tools were called, what they returned, tokens
   and cost, and why a step failed.

## Deliverables

Write these files in the current directory:

1. `design.md`: your design. Cover at least: workload and constraints analysis, components and
   their responsibilities, contracts between them, data storage, concurrency/execution model,
   failure handling, security, how each user story is served, extensibility, operations,
   trade-offs and rejected alternatives, risks. Commit to decisions; a list of options without
   a choice is not a decision.
2. `decisions.json`: a JSON array of your committed decisions:
   ```json
   [{"id": "D1", "area": "short area name", "decision": "what you will do",
     "rationale": "the fact that forces it", "status": "decided | assumption | deferred"}]
   ```
