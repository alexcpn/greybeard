# greybeard

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

*He has been burnt before. He asks whether you should build it at all.*

An architect skill for coding agents (Claude Code, Codex, opencode and any agent that reads
`SKILL.md`). Agents now write code faster than anyone can review it, so the bottleneck is the
design: the decisions made before the first line, and whether there should be a first line at
all. Greybeard puts a seasoned architect in the room for that part.

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

For implementation it hands off to [ponytail](https://github.com/DietrichGebert/ponytail):
greybeard decides where code goes and which seams exist; ponytail keeps the code inside them
small. Ponytail trims code, never architecture.

## Install

Claude Code:

```
/plugin marketplace add alexcpn/greybeard
/plugin install greybeard@greybeard
```

Any other agent: copy `skills/greybeard/` into its skills folder (for example
`~/.claude/skills/`, `.agents/skills/` or `.opencode/skills/`), or tell it to read
`skills/greybeard/SKILL.md`.

Then ask: *"Design a system for ..."*, *"Should we build ...?"*, or *"Review this architecture"*.

## Status

v0.1. The rules come from design mistakes seen repeatedly in AI-generated architectures and from
building a distributed CI system ([Relay CI](https://github.com/alexcpn/relay-ci)) with an agent.
The skill itself has not yet been benchmarked with and without; treat it as a well-founded
checklist, not a proven improvement. Issues and counter-examples welcome.

## License

MIT
