# greybeard: NO MORE AI SLOP

```
         .-''''''''-.
       .'  ,,    ,,  '.      "Before we build it,
      /   (o_)--(o_)   \      who is going to run it?"
     |        /\        |
     |  .~~~~~~~~~~~~.  |
      \/~~~~~~~~~~~~~~\/     Three gates before any code:
       |~~~~~~~~~~~~~~|
       |~~~~~~~~~~~~~~|        1. Is it needed?
        \~~~~~~~~~~~~/         2. Is it worth the time?
         \~~~~~~~~~~/          3. Will someone run it?
          \~~~~~~~~/
           \~~~~~~/          Fail one, and greybeard says STOP.
            '~~~~'
```

Coding agents made code nearly free. The new failure is a system nobody can run, extend or
trust. Greybeard is an architect skill for coding agents (Claude Code, Codex, opencode, Gemini
CLI, any agent that reads `SKILL.md`). It works before the code:

1. **Three gates before any code.** Is it needed? Is it worth the time? Will someone run it?
   Fail one and it warns you and stops.
2. **Architecture first.** It designs the whole system, then fits every user story into it.
3. **SOLID, open/closed, Unix philosophy.** It puts extension points only on the axes that will
   really change.
4. **Right-sized.** It keeps the infrastructure simple but not the hot path. POCs become products.

**Design only.** Its output is a verdict, `design.md`, `decisions.json` and an `ARCHITECTURE.md`
that gives coding agents the rules, why each one exists, and the automated check that enforces
it. Agents forget prose; they cannot ignore a failing check.

## Install

```
npx skills add alexcpn/greybeard -g -a claude-code    # Claude Code (~/.claude/skills)
npx skills add alexcpn/greybeard -g -a codex -a opencode   # other agents
```

Pick the agents with `-a`: without it, the installer may put the skill only in the shared
`~/.agents/skills` folder, which Claude Code does not read. Drop `-g` to install for the current
project only.

Or, as a Claude Code plugin: `/plugin marketplace add alexcpn/greybeard`, then `/plugin install greybeard@greybeard`.
Without Node: copy `skills/greybeard/` into your agent's skills folder.

Then ask: *"Design a system for ..."* or *"Should we build ...?"*

## Does it help?

An exam with a hidden answer key. Each task is the brief for a real system whose production
failures are known. Models design it with and without the skill, then handle a change request
based on a real incident. Claude, GPT and Gemini grade each design against those known
failures, and the middle score counts. Scores are out of 100.

| Task | Model | Without | With | Change |
|---|---|---|---|---|
| CI system ([Relay CI](https://github.com/alexcpn/relay-ci)) | Claude Opus 5.5 | 77.9 | 76.7 | -2% |
| CI system | GPT-6.1 Sol | 92.0 | 94.0 | +2% |
| CI system | DeepSeek V4.1 Flash | 94.2 | 93.3 | -1% |
| LLM research agent | GPT-6.1 Sol | 94.5 | 92.0 | -3% |
| Small-model coding agent ([Fox](https://github.com/alexcpn/fox)) | GPT-6.1 Sol | 73.8 | 84.3 | +14% |

These results are interim (v0.2, one run each, cut short by usage limits), so they show a
direction, not proof. The skill avoided some of the real systems' bugs and never stopped a
valid brief. It also made models drop mechanisms their own numbers called for, in the name of
"don't over-engineer". v0.3 fixes that.

**Does it say no when it should?** In seven short briefs (four where mature software already
covers the need, three where it does not), Claude and GPT got every one right, with or without
the skill. The briefs were too easy to show what the gate adds. The skill also still made designs
longer. Details, tasks and how to run them are in [`eval/`](eval/).

## License

MIT
