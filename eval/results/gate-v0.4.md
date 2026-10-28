# Gate test (skill v0.4)

Does the viability gate say no when reuse is right, and yes when building is right?
Seven single-turn briefs (`../gate/`), two models, with and without the skill, one run each.
Both conditions are asked for the same `verdict.json`. Scored by `../gate/score_gate.py`; no
judges are needed.

| Task | Expected | Model | Without skill | With skill |
|---|---|---|---|---|
| auth | reuse | Claude Opus 5.5 | do_not_build ✓ | do_not_build ✓ |
| auth | reuse | GPT-6.1 Sol | do_not_build ✓ | do_not_build ✓ |
| vector | reuse | Claude Opus 5.5 | do_not_build ✓ | do_not_build ✓ |
| vector | reuse | GPT-6.1 Sol | do_not_build ✓ | do_not_build ✓ |
| queue | reuse | Claude Opus 5.5 | build_narrower ✓ | do_not_build ✓ |
| queue | reuse | GPT-6.1 Sol | do_not_build ✓ | do_not_build ✓ |
| flags | reuse | Claude Opus 5.5 | do_not_build ✓ | do_not_build ✓ |
| flags | reuse | GPT-6.1 Sol | do_not_build ✓ | do_not_build ✓ |
| reconcile | build | Claude Opus 5.5 | build ✓ | build ✓ |
| reconcile | build | GPT-6.1 Sol | build ✓ | build ✓ |
| pricing | build | Claude Opus 5.5 | build ✓ | build ✓ |
| pricing | build | GPT-6.1 Sol | build ✓ | build ✓ |
| configmigrate | build | Claude Opus 5.5 | build ✓ | build ✓ |
| configmigrate | build | GPT-6.1 Sol | build ✓ | build ✓ |

| Model | Condition | Says no when it should (reuse tasks) | Says yes when it should (build tasks) |
|---|---|---|---|
| Claude Opus 5.5 | without | 4/4 | 3/3 |
| Claude Opus 5.5 | with skill | 4/4 | 3/3 |
| GPT-6.1 Sol | without | 4/4 | 3/3 |
| GPT-6.1 Sol | with skill | 4/4 | 3/3 |

Total `design.md` words over the 7 tasks: Claude 12.7k without the skill, 21.4k with it (+69%);
GPT 20.8k without, 24.9k with (+20%).

## What it means

- **Ceiling.** Every run was right, with and without the skill. Once a model is asked "build,
  build narrower or don't build?", today's frontier models already answer these briefs
  correctly. The briefs make the answer too easy to find ("nobody on the team has built
  identity", "a weekend project"), so this test cannot show the gate adding judgement.
- **The question itself may be the gate.** The useful part may simply be asking the question,
  which a plain "design X" request never does. The next test should give the plain request
  with no verdict question, and use ambiguous briefs where reuse and build are close.
- **Length.** v0.4's shorter skill still made the designs longer. The document-length rule is
  not working yet.
