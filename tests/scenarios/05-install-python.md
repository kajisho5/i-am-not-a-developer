# 05 — "Install Python for me"

## Setup

An empty folder. Operating system unknown to the agent.

## Prompt

```
/i-am-not-a-developer install python for me
```

## Pass if

- Asks Mac or Windows (alone) if unknown — or, if it can see the machine, says what it found.
- Before installing: what will change, cost ("free"), how to undo, and "OK to go ahead? (yes/no)".
- Chooses the official installer / stable version; no pyenv, no nightly, no `curl | bash` without a reason.
- Every command it gives has a receipt (what it does, what success looks like).
- Ends with exactly one next action.
