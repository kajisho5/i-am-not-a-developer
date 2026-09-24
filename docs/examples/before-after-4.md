# Before / After: "Something says permission denied"

Scenario `tests/scenarios/03-*.md`. Recorded on 2026-09-24 with Claude Code 2.1.281 (`claude -p`, then `--resume` for the second turn) in a Linux container. Replies are copied verbatim; tool calls are shown as one-line notes. **Before** is the same prompt with the plugin disabled; **After** starts with `/i-am-not-a-developer`.

**Setup:** An empty folder. Chat-only: the agent's command tool is turned off and it is told the user runs every command themselves.

**Prompt:** `something says permission denied` → follow-up: `zsh: permission denied: ./start.sh`

## What changed

- **Before:** asks three questions at once, then gives the fix plus three fallbacks including `sudo`, `cat -A` and `dos2unix`.
- **After:** asks one thing, then gives one command with what it does, what success looks like and what to do if it doesn't work.

## Before (no skill)

**Agent:**

I don't have enough detail to diagnose this yet — I can't see your screen or run commands myself. Could you share:

1. The exact error message (full text)
2. What you were doing when it happened (running a command, opening a file, using an app, etc.)
3. What platform/context this is in (terminal, a specific app, a website, etc.)

That'll let me point you to the actual cause.

**User:** zsh: permission denied: ./start.sh

**Agent:**

That means `start.sh` doesn't have the execute permission bit set. Fix it by running:

```bash
chmod +x ./start.sh
./start.sh
```

If that still fails, a couple other possibilities to check:
- **Wrong shebang or line endings**: if the file was created/edited on Windows, it may have `\r\n` line endings that break the shebang line. Check with `head -1 start.sh | cat -A` — if you see `^M` at the end, run `dos2unix start.sh` or `sed -i 's/\r$//' start.sh`.
- **Filesystem mounted noexec**: if the file lives on a mount (e.g. some `/mnt` or network share) with `noexec`, `chmod +x` won't help — you'd need to run it as `bash start.sh` instead, or move it to a normal filesystem location.
- **Ownership**: if you don't own the file, `chmod` on it may itself fail — check with `ls -l start.sh` and use `sudo chmod +x start.sh` if needed (only if you trust the script).

Try `chmod +x ./start.sh` first — that resolves it in the vast majority of cases.

## After (`/i-am-not-a-developer`)

**Agent:**

I can't see your computer myself, so I need a little detail from you first.

What were you doing right before you saw "permission denied" — for example, opening a file, running a program, or something else?

**User:** zsh: permission denied: ./start.sh

**Agent:**

That error means the file `start.sh` exists, but it isn't yet marked as something you're allowed to run like a program — zsh (the command program in Terminal) is refusing until you flip that on.

Fixing it: you'll run one command that marks the file as runnable. It's free, affects only this one file, and is easy to undo (a similar command switches it back).

In Terminal, type this and press Return:

```
chmod +x start.sh
```

Success looks like: no message at all, just a new empty line. If instead you see red text, copy it and paste it here.

Tell me what you see.
