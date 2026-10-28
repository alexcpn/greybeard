# Follow-up (turn 2)

Send only the text below the line, in the same session, after turn 1 is complete.

---

Two bug reports came in after release:

1. With the hosted provider, long sessions fail with HTTP 400: "messages with role 'tool' must
   be a response to a preceding message with 'tool_calls'". Local models never complained.
2. In a multi-step task, step 1 wrote `results.txt`, step 3 overwrote it, and step 4 read it
   and got the old content. The user also edited an input file between two tasks in the same
   session and the agent answered from the old version.

New requirements: the conversation sent to any provider must always be valid for that
provider's strictest message rules, whatever the context-management strategy drops; and the
agent must never answer from stale file content, whether the file was changed by the agent's
own tools or by the user.

Update `design.md` (add a section describing what changes and why, and update any earlier
sections the change affects) and `decisions.json`.
