# Design Task: terminal agent loop for small local LLMs

You are the architect. Produce a design for the system below. You have no code to look at;
everything you know is in this document.

## Context

A developer wants an interactive terminal agent, like the coding agents built on frontier
models, but running on small local models so that data never leaves the machine. The user types
a task; the agent uses tools to complete it.

## Facts

| Item | Value |
|---|---|
| Models | Local models of 8B–27B parameters served by Ollama (OpenAI-compatible chat API with tool calling); optionally a hosted OpenAI-compatible API when the user has a key |
| Hardware | A laptop with a 16 GB GPU, 32 GB RAM. Practical context window 8k–32k tokens; generation 20–60 tokens/s, so every 1,000 tokens of prompt costs seconds |
| Observed small-model behaviour | Repeats the same tool call in a loop; invents file names that do not exist; loses track of earlier steps in long tasks; emits malformed tool calls or JSON; declares success when the output is wrong or missing; struggles to plan more than 3–4 steps; embeds whole file contents as string literals in code |
| Tools needed | Run shell commands; run Python scripts; read files (with line ranges); write files; regex search across files; list directories |
| Typical tasks | Questions over local source or log files; analysis of a 5,000-line log or a 50 MB CSV; multi-step data tasks (parse, compute, compare, summarise); generating binary documents (pptx, xlsx) via libraries |
| Team | 1 developer, Python; wants minimal dependencies and a single process |
| Platform | Linux and macOS terminals |

## User stories

1. As a user, I ask a question about files in the current directory and get a correct answer.
2. As a user, I give a multi-step task over a large input file and the agent completes it
   without running out of context.
3. As a user, I ask for a generated document (for example a slide deck) and get a valid file.
4. As a user, I can see what the agent did: each step, tool call, result and why it stopped.
5. As a user, the agent gets better at kinds of tasks it has done successfully before.
6. As a user, I am told honestly when a task failed, instead of a confident wrong answer.
7. As the developer, I can switch between local and hosted models, and add a new tool, without
   changing the agent loop.

## Deliverables

Write these files in the current directory:

1. `design.md`: your design. Cover at least: workload and constraints analysis, components and
   their responsibilities, contracts between them, data storage, concurrency/execution model,
   failure handling, security, how each user story is served, extensibility, operations,
   trade-offs and rejected alternatives, risks. Commit to decisions; a list of options without
   a choice is not a decision.
2. `decisions.json`: a JSON array of your committed decisions:
   ```json
   [{"id": "D1", "area": "short area name", "decision": "what you will do",
     "rationale": "the fact that forces it", "status": "decided | assumption | deferred"}]
   ```
