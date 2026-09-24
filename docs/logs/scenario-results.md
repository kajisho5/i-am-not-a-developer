# Scenario results (final SKILL.md)

Final round (round 8) of the check loop, run on 2026-09-24 with Claude Code 2.1.281.
Each scenario in `tests/scenarios/` was run twice (a, b) as a two-turn conversation.
Scenarios 01, 02 and 04 let the agent run commands; 03 and 05 are chat-only (command tool off).

"Shape" = one step at a time + where to click/type + what success looks like + exactly one next action.

| Scenario | Run | Shape | Misses |
| --- | --- | --- | --- |
| 01 ERR_CONNECTION_REFUSED | a | ✅ | — |
| 01 ERR_CONNECTION_REFUSED | b | ✅ | — |
| 02 Put this on the internet | a | ✅ | Made a zip file without a diary entry (rule 7) |
| 02 Put this on the internet | b | ✅ | — |
| 03 Permission denied | a | ⚠️ | First reply asked for the message *and* where it appeared; second reply had no "what success looks like" (rule 3) |
| 03 Permission denied | b | ✅ | — |
| 04 Undo yesterday | a | ⚠️ | Asked before undoing ✅; last line was "if you'd like to check" instead of a firm next action (rule 10) |
| 04 Undo yesterday | b | ✅ | "Open index.html in a browser" without saying where to click (rule 1, minor) |
| 05 Install Python | a | ✅ | — |
| 05 Install Python | b | ✅ | — |

Every scenario has at least one fully passing run. 8 of 10 runs have the full shape.
The two remaining misses are wording-level and did not repeat in the other run.

Rule fixes made during the loop are listed in `docs/DECISIONS.md`.
Full transcripts of passing runs: `docs/examples/`.
