# Follow-up (turn 2)

Send only the text below the line, in the same session, after turn 1 is complete.

---

Two friends want to use the tool, and one of them holds US equities as well as Indian ones.
They also want a second research provider (a different vendor, different MCP tools and data
shapes) because the first has thin coverage of small caps.

Separately, one friend asked "why did it say Exit on this stock in March?" and the developer
could not answer: the prompt, the model and the cached research had all changed since.

New requirements: support a second market (US) and a second research provider, and make every
research view reproducible and explainable later: exactly which prompt version, model, analysis
lens and evidence produced it.

Update `design.md` (add a section describing what changes and why, and update any earlier
sections the change affects) and `decisions.json`.
