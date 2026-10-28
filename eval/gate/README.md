# Gate tasks

These tasks test whether the viability gate says no when it should. Each is a short brief with a
single turn and no follow-up.

- `expected.json`: `reuse` means mature products cover the need, so a pass is `do_not_build`, or
  `build_narrower` with a named alternative. `build` means the need is specific to the business,
  so a pass is anything except `do_not_build`.
- Scoring is deterministic and uses `verdict.json` (`score_gate.py`); no judges are
  needed.
- Both conditions are asked for the same `verdict.json`, so the test measures judgement, not
  whether the model is asked the question.
