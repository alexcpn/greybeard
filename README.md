# greybeard: NO MORE AI SLOP

```
                 .-""""""-.
               .'  _    _  '.
              /   (o)  (o)   \        "Before we build it...
             |   .-""""""-.   |        who is going to run it?"
             |  /  ~~~~~~  \  |
              \|  ~~~~~~~~  |/
               \ ~~~~~~~~~~ /
               /~~~~~~~~~~~~\
              /~~~~~~~~~~~~~~\
              \~~~~~~~~~~~~~~/
               \~~~~~~~~~~~~/
                '~~~~~~~~~~'
                  '~~~~~~'
```

**No more AI slop.** Coding agents have made code nearly free. The new failure is not
"we could not build it" but "we built a pile nobody can run, extend or trust": services that
drift between patterns, utility packages that couple everything, POCs that quietly become
products without persistence, auth or failure handling, and whole systems that should never
have been started.

Greybeard is an architect skill for coding agents (Claude Code, Codex, opencode, Gemini CLI and
any agent that reads `SKILL.md`). It works *before* the code:

1. **Should this exist?** It weighs build-vs-reuse, the production bill and who will own it,
   and **warns and stops** if the result would be AI slop or cost more than it is worth.
2. **Architecture first.** It designs the whole system, then fits every user story into it,
   instead of patching story by story.
3. **SOLID, open/closed, Unix philosophy.** Single responsibilities, dependency inversion at
   boundaries, extension points on the axes that will really change, small composable parts.
4. **Right-sized.** Not over-engineered, not under-engineered: POCs become products, and
   versioning, performance and failure semantics are hard to bolt on later.

It is **design only**: it writes no implementation code. It produces a verdict, a design and a
decision record that implementation must then follow.

## What it does

| Phase | The agent must |
|---|---|
| 0. Viability gate | Write down the problem, build-vs-reuse, the full production bill and the owner. Verdict **GO / GO, NARROWED / STOP**. On STOP it warns you and does not design. |
| 1. Constraints | List the constraints given and ask for the missing ones. No silent assumptions. |
| 2. Sizing | Do the arithmetic first: per-request budget, working set vs RAM, the bottleneck. |
| 3. Architecture first | Design the whole system, then walk every user story through it. A story that does not fit changes the architecture deliberately; it does not get a patch. SOLID and the Unix philosophy apply. Extension points go on the 2-4 axes of change you can name (open/closed). |
| 4. Right-size | Build in now what is cheap today and painful later (versioning, complete cache keys, identity, restart survival, idempotency, failure semantics, observability). Defer the rest, with a trigger. |
| 5. Self-review | Run the checklist in `references/checklist.md`. |
| 6. Deliverables | `design.md`, a committed `decisions.json`, and an `ARCHITECTURE.md` for coding agents that records **why**, not just what. |

## Install

Claude Code:

```
/plugin marketplace add alexcpn/greybeard
/plugin install greybeard@greybeard
```

Any agent (Claude Code, Codex, opencode, Cursor, Gemini CLI and more), using the
[skills CLI](https://github.com/vercel-labs/skills):

```
npx skills add alexcpn/greybeard          # this project; prompts for which agents
npx skills add alexcpn/greybeard -g       # global, for all your projects
npx skills add alexcpn/greybeard -a codex -a opencode -y   # pick agents, no prompts
```

`npx skills update` pulls new versions later.

No Node? Copy the folder into your agent's skills directory:

```
git clone --depth 1 https://github.com/alexcpn/greybeard /tmp/greybeard
cp -r /tmp/greybeard/skills/greybeard ~/.claude/skills/    # or .agents/skills/, .opencode/skills/
```

Then ask: *"Design a system for ..."*, *"Should we build ...?"*, or *"Review this architecture"*.

## How it was tested (with vs without, v0.2)

**In plain words.** Think of it as an exam for AI architects, where the answer key comes from
systems that were already built and had already failed in production.

1. **Pick real systems with real scars.** Each task comes from a system that was actually built
   and run, so its weak spots are known from its bug backlog and fix history. For example, a
   restart wiped all build history, or a cache returned stale results.
2. **Write the brief, hide the answers.** The AI gets only the facts the original team had:
   hardware, load, team size, budget and user stories. It does not see how the system was
   really built or what went wrong.
3. **Ask for a design, twice.** First the AI writes a design document. Then it gets a change
   request based on a real incident ("the server restarted and lost everything; fix it") and
   updates its design. A good design absorbs the change; a weak one needs rework.
4. **Grade against the known scars.** Each task has 9 topics (sizing, data, failure handling,
   security, extensibility and so on), each scored 0-4. Mentioning a topic earns little; the top
   score needs a design that would have avoided the real problem. Points come off for building
   far more than the facts justify, and for decisions that contradict each other.
5. **Use three graders from different companies.** Claude, GPT and Gemini each grade every
   design independently, and the middle score counts. The graders are told to ignore the skill's
   own labels and checklists, and to grade only the design itself.
6. **Run with and without the skill.** Each model does each task twice, once plain and once
   with greybeard, so the change between the two runs is the skill's effect.

The scores are out of 100. "Change" below is how much better or worse the design was with the
skill, as a percentage of the score without it.

**Tasks:**
- `ci`: agent-heavy CI for 15 repos on 5 VMs with 2 engineers, from
  [Relay CI](https://github.com/alexcpn/relay-ci). The skill's Relay CI paragraph was removed for
  this task.
- `finagent`: an LLM portfolio research agent with a per-run cost and time budget.
- `smallagent`: a terminal coding agent for 8-27B local models on a 16 GB GPU, from
  [Fox](https://github.com/alexcpn/fox).
- A fourth, proprietary task, not reported here.

**Subjects:** Claude Opus 5.5, GPT-6.1 Sol and DeepSeek V4.1 Flash, one run per condition.

**Interim results, three public tasks.** Usage limits stopped the round early; empty pairs were
not run or not judged.

| Task | Model | Without (of 100) | With (of 100) | Change | Change per judge (Claude / GPT / Gemini) |
|---|---|---|---|---|---|
| ci | Claude Opus 5.5 | 77.9 | 76.7 | -2% | +8% / -11% / - |
| ci | GPT-6.1 Sol | 92.0 | 94.0 | +2% | +2% / +8% / +6% |
| ci | DeepSeek V4.1 Flash | 94.2 | 93.3 | -1% | -1% / +1% / -3% |
| finagent | GPT-6.1 Sol | 94.5 | 92.0 | -3% | -3% / -10% / -8% |
| smallagent | GPT-6.1 Sol | 73.8 | 84.3 | +14% | +9% / +22% / - |

Change is relative to the score without the skill: (with - without) / without.

**What it showed:**
- **The gate did not cry wolf.** Every run with the skill returned "GO, NARROWED" on these
  legitimate briefs. On `ci`, GPT with the skill kept the existing CI and added a small
  agent-facing layer instead of building a new one.
- **The targeted weaknesses moved.** With the skill, GPT on `smallagent` keyed its file cache on
  file state in the first turn; that was the real system's bug.
- **It also cost detail.** "Don't over-engineer" led models to reject mechanisms their own
  numbers called for (cache tiers, cheap pruning before expensive work, input caps, stronger
  isolation). They also stayed vague on retry idempotency and on silent-failure paths, and the
  GPT designs grew up to 3x longer.
- **Noise.** With one run per condition, a change of about ±5% is within run-to-run noise, and the judges
  sometimes disagree on direction. This shows direction, not proof. The Gemini judge also
  scored near the ceiling, so the rubrics need harder level-4 descriptors.

v0.3 is the response. It keeps the gate, build-vs-reuse and the cache-key rule. It adds "simple
infrastructure, not a simple hot path", per-component budgets, per-operation retry, failure and
trust semantics, and a limit on document length. Because v0.3 was tuned on these judges'
notes, re-running these tasks would overstate it; the next test needs held-out tasks.

## Status

v0.3. The rules come from design mistakes seen repeatedly in AI-generated architectures and from
building a distributed CI system ([Relay CI](https://github.com/alexcpn/relay-ci)) with an agent,
revised after the trial above. Treat it as a well-founded checklist, not a proven improvement.
Issues and counter-examples welcome.

## License

MIT
