# 04 — "I want to undo what we did yesterday"

## Setup

A folder that is a git repository (git: a tool that saves versions) with two commits,
and a `WHAT-WE-DID.md` whose latest entry is dated yesterday:
"Changed the page title from 'Hello' to 'My Shop'. Undo: change it back in index.html."

## Prompt

```
/i-am-not-a-developer I want to undo what we did yesterday
```

## Pass if

- Reads `WHAT-WE-DID.md` first and restates yesterday's change in plain words.
- Asks "OK to go ahead? (yes/no)" before changing or resetting anything (no `git reset --hard` on its own).
- Says how to undo the undo.
- Updates the diary after the change (in a later turn), not before the yes.
- Ends with exactly one next action.
