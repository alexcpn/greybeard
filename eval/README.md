# Evals

How greybeard is tested. Results are in `results/`.

## Design tasks (`ci/`, `finagent/`, `smallagent/`)

Each task is the brief for a real system whose production failures are known.

- `task/prompt.md` gives the facts only: hardware, load, team, budget and user stories. The
  deliverables spec (`DELIVERABLES.md`) is already inlined.
- `task/followup.md` is the second turn: a change request based on a real incident.
- `hidden/reference_design.md` describes what the real system did and its known weaknesses.
  Never show it to the model being tested.
- `hidden/rubric.json` holds 9 weighted dimensions scored 0-4, plus the follow-up and penalties.
  Level 4 means the design avoids the known weakness, not just that it names the topic.

| Task | From |
|---|---|
| `ci` | Agent-heavy CI, from [Relay CI](https://github.com/alexcpn/relay-ci). Remove the Relay CI paragraph from the skill before running this task; it names the answers. |
| `finagent` | An LLM portfolio research agent with a cost and time budget per run. |
| `smallagent` | A terminal coding agent for small local models, from [Fox](https://github.com/alexcpn/fox). |

**Running a design task:**

1. Copy `task/prompt.md` into an empty directory that has nothing above it the model could read.
2. Ask the agent to "read prompt.md and complete the task". For the skill condition, also copy
   the skill into that directory and add "first read skill/SKILL.md and follow it".
3. Save `design.md` as `design_turn1.md`, then send the text of `task/followup.md` after its
   `---` line in the same session.
4. Give each judge `judge_prompt.md`, the task's `hidden/` files, `design_turn1.md`, `design.md`
   and `decisions.json`. Each judge writes `verdict.json`.
5. Score each verdict with `python3 score_generic.py <task> verdict.json`, and take the median
   across judges.

## Gate tasks (`gate/`)

Seven single-turn briefs that check whether the design says "don't build" when mature software
already covers the need, and "build" when the need is specific to the business. Each run writes
`verdict.json`. Score a directory of `<model>-<task>-<base|skill>` runs with
`python3 gate/score_gate.py <runs-dir>`.

## Caveats

- One run per condition is noisy: a change of about ±5% is within run-to-run variation.
- Skill versions after v0.2 were revised using the judges' notes on these tasks, so these tasks
  are no longer held out for those versions.
- The gate tasks are at the ceiling: every model passes them with or without the skill.
