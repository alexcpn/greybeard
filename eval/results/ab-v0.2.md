# With vs without the skill (v0.2), three public tasks

One run per condition. Usage limits cut the round short; pairs without scores on both sides are
omitted. Scores are out of 100, the median of the judges that graded both sides (Claude, GPT,
Gemini), computed with `../score_generic.py` from each judge's verdict. "Change" is relative to
the score without the skill.

| Task | Model | Without | With | Change | Change per judge (Claude / GPT / Gemini) |
|---|---|---|---|---|---|
| ci | Claude Opus 5.5 | 77.9 | 76.7 | -2% | +8% / -11% / - |
| ci | GPT-6.1 Sol | 92.0 | 94.0 | +2% | +2% / +8% / +6% |
| ci | DeepSeek V4.1 Flash | 94.2 | 93.3 | -1% | -1% / +1% / -3% |
| finagent | GPT-6.1 Sol | 94.5 | 92.0 | -3% | -3% / -10% / -8% |
| smallagent | GPT-6.1 Sol | 73.8 | 84.3 | +14% | +9% / +22% / - |

Where the skill lost points, the judges' notes show models rejecting mechanisms their own sizing
called for (cache tiers, pruning before expensive work, input caps, stronger isolation) for the
sake of "don't over-engineer", and staying vague on retry idempotency and silent failures. v0.3
and v0.4 address that; they were tuned on these notes, so re-running these tasks would overstate
them.
