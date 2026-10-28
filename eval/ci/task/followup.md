# Follow-up (turn 2)

Send only the text below the line, in the same session, after turn 1 is complete.

---

The system has been running for six weeks. Three things happened:

1. The control VM was restarted for an OS patch. Every build that was running was lost, and
   the build history agents rely on to compare a red build with the last green one was gone.
2. A worker VM died mid-afternoon. Six builds stayed "running" until a human noticed the next
   morning and retried them.
3. One agent loop submitted 140 builds overnight on the same failing change. Nobody can tell
   from the records which agent did it; every agent uses the same API token.

New requirements: no build state or history may be lost when any single component restarts;
work on a dead worker must recover without a human; and every build must be attributable to
a specific human or agent identity, with a per-identity limit on builds.

Update `design.md` (add a section describing what changes and why, and update any earlier
sections the change affects) and `decisions.json`.
