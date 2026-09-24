# Before / After: "I want to undo what we did yesterday"

Scenario `tests/scenarios/04-*.md`. Recorded on 2026-09-24 with Claude Code 2.1.281 (`claude -p`, then `--resume` for the second turn) in a Linux container. Replies are copied verbatim; tool calls are shown as one-line notes. **Before** is the same prompt with the plugin disabled; **After** starts with `/i-am-not-a-developer`.

**Setup:** A git project whose `WHAT-WE-DID.md` says: yesterday the page title changed from "Hello" to "My Shop". The agent can run commands.

**Prompt:** `I want to undo what we did yesterday` → follow-up: `yes`

## What changed

- **Before:** reverts the file without asking, then, on "yes", commits and **deletes the diary**.
- **After:** reads the diary, says in plain words what will change back, waits for yes, then adds today's entry to the diary.

## Before (no skill)

> *tool: Bash — `git log --oneline -20 --date=short --pretty=format:"%h %ad %s" --date=short && echo "---ST …`*

> *tool: Bash — `git log --pretty=format:"%h | %ai | %an | %s" -20`*

> *tool: Bash — `git show --stat 331a368 && echo "===" && git show --stat 5233034`*

> *tool: Read — WHAT-WE-DID.md*

> *tool: Read — index.html*

> *tool: Bash — `git show 5233034 -- index.html`*

> *tool: Edit — index.html*

**Agent:**

`index.html` is reverted to `<title>Hello</title>` / `<h1>Hello</h1>`. Working tree is otherwise clean — let me know if you also want me to commit this revert or remove `WHAT-WE-DID.md`.

**User:** yes

> *tool: Bash — `rm WHAT-WE-DID.md && git add -A && git status`*

> *tool: Bash — `git commit -m "$(cat <<'EOF'`*

**Agent:**

Committed (`180d66a`): reverted the title/heading back to "Hello" and removed `WHAT-WE-DID.md`.

## After (`/i-am-not-a-developer`)

> *tool: Bash — List files in the project folder*

> *tool: Read — WHAT-WE-DID.md*

> *tool: Read — index.html*

**Agent:**

I found the diary entry for yesterday. Here's what it says:

**Yesterday (2026-09-23):** The page title (and heading) was changed from "Hello" to "My Shop" in the file `index.html`.

**Undoing this** would change it back to "Hello" in both places. Nothing gets installed, deleted, or costs anything — it's just changing text in one file. This can be undone again later the same way if you change your mind.

OK to change "My Shop" back to "Hello" in index.html? (yes/no)

**User:** yes

> *tool: Edit — index.html*

> *tool: Edit — WHAT-WE-DID.md*

**Agent:**

Done — the page title is back to "Hello" in index.html, and the diary now has today's entry too.

Open index.html in a browser to check it now shows "Hello".
