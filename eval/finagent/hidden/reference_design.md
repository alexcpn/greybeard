# Reference design (hidden from the agent): LLM portfolio research agent

The real system is a Python project (~3.6k lines plus tests) built with Pydantic AI by one
developer, organised around evaluation-driven development.

## What the real system did

- **Versioned behaviour contract.** One JSON file holds, per agent: agent id, version, prompt,
  model string (`provider:model`), runtime guardrails, request/tool-call limits, eval checks
  and judge rubric. The same contract drives the application, live evals and trace evals.
  Switching provider or model is a one-line contract edit (Anthropic, OpenAI, local Ollama).
- **Deterministic code where determinism is possible.** CSV parsing and validation (Decimal
  arithmetic), portfolio snapshot (weights, P&L, contributors) and research-target selection
  are Python, not LLM. CSV fields are treated as untrusted data, never instructions
  (prompt-injection guard).
- **Orchestration.** A Python pipeline (not an LLM planner) reads the research cache, selects
  targets, runs specialist agents directly (macro news with exactly two capped searches;
  technicals; broker reports), each with bounded tool/request budgets, then hands the composed
  evidence to a tool-free synthesis agent that only writes the report. Usage aggregated across
  stages.
- **Research cache.** Per ticker under `data/reports/<ticker>/`: original PDFs/HTML retained
  with hashes, extracted text, JSONL search history with discovery provenance, and a versioned
  JSON snapshot. A structured-output summariser produces cited findings and rejects citations
  that do not match a stored source ID. Guarded downloader (domain exclusions, size limits).
  Refresh by max-age (24 h default).
- **Closed-vocabulary judgments.** Per holding: Add/Hold/Exit, confidence floor, positive and
  risk citations, thesis implication (Supports/Contradicts/Neutral/Refines), horizon
  (30/90/180 d) and a resolution date computed in code; a later job grades it against the real
  price move with a materiality band, from an append-only ledger. A code-level regex blocks
  advice-shaped rationale (price target, position size, fair value).
- **Analysis themes.** Human-owned, versioned registry: statement, anti-thesis, observable
  indicators; the model tests the theme and cannot silently amend it.
- **Evaluation.** Pydantic Evals: repeated live runs to expose stochastic failures,
  deterministic checks, minimum-tool-call checks, LLM judge; plus deterministic regression and
  LLM-judge regression over stored traces (no new model/search calls). Markdown/JSON reports
  and exit status as a CI gate.
- **Observability.** OpenTelemetry traces and logs; Prometheus counters for model, tokens and
  MCP outcomes by server/tool/result/status.

## Known weaknesses (basis for level 4)

1. Infrastructure out of proportion: a local Docker stack of Prometheus, Loki, Tempo,
   SeaweedFS (S3 for trace blocks) and Grafana for a one-person laptop tool. Log retention
   unset. A design that gets traceability with far less (e.g. OTel to a single local
   backend, or traces/JSONL files queried by the eval tooling) is better.
2. Research cache refreshes by age (24 h), not by source change (filing dates, document hash),
   so it either re-downloads unchanged filings or misses new ones.
3. One 1,600-line agent module: orchestration, specialists and tool wiring coupled.
4. The judge model defaults to a different provider than the agent; judge drift is not
   versioned with the contract.
5. Local-model path is fragile (exact tool-call budgets and strict structured output fail);
   no degraded mode.
6. Reproducibility of a past judgment depends on prompt version and research snapshot being
   recorded with it; versioning of the evidence snapshot used by each judgment is implicit.

## Calibration

- Letting an LLM planner do arithmetic, selection or orchestration that code can do is weak.
- "Use LangChain/LangGraph" or "use a vector DB / RAG over filings" without a forcing fact is
  at most level 2 on the relevant dimension; the real project removed a RAG layer.
- Multi-service infrastructure (Kubernetes, Kafka, separate microservices) for one developer is
  over-engineering.
