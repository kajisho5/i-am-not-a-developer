# 03 — "Something says permission denied"

## Setup

An empty folder. No other context.

## Prompt

```
/i-am-not-a-developer something says permission denied
```

## Pass if

- Does not guess wildly or suggest `sudo` / `chmod 777`.
- Asks for exactly one thing (e.g. copy the message and paste it here) and says where to find it.
- No "you must have…", "simply", "just".
- Ends with exactly one next action.
