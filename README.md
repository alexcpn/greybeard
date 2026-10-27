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

## Status

v0.1. The rules come from design mistakes seen repeatedly in AI-generated architectures and from
building a distributed CI system ([Relay CI](https://github.com/alexcpn/relay-ci)) with an agent.
The skill itself has not yet been benchmarked with and without; treat it as a well-founded
checklist, not a proven improvement. Issues and counter-examples welcome.

## License

MIT
