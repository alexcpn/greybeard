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

Coding agents made code nearly free. The new failure is a system nobody can run, extend or
trust. Greybeard is an architect skill for coding agents (Claude Code, Codex, opencode, Gemini
CLI, any agent that reads `SKILL.md`). It works before the code:

1. **Should this exist?** Build vs reuse, the production bill, the owner. It warns and stops
   if the result would be slop or cost more than it is worth.
2. **Architecture first.** It designs the whole system, then fits every user story into it.
3. **SOLID, open/closed, Unix philosophy.** It puts extension points only on the axes that will
   really change.
4. **Right-sized.** It keeps the infrastructure simple but not the hot path. POCs become products.

**Design only.** Its output is a verdict, `design.md`, `decisions.json` and an `ARCHITECTURE.md`
that tells coding agents what the rules are and why.

## Install

```
npx skills add alexcpn/greybeard        # any agent; -g for global
```

Claude Code: `/plugin marketplace add alexcpn/greybeard`, then `/plugin install greybeard@greybeard`.
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

## License

MIT
