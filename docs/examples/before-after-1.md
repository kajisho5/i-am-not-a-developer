# Before / After: "My website shows ERR_CONNECTION_REFUSED"

Scenario `tests/scenarios/01-*.md`. Recorded on 2026-09-24 with Claude Code 2.1.281 (`claude -p`, then `--resume` for the second turn) in a Linux container. Replies are copied verbatim; tool calls are shown as one-line notes. **Before** is the same prompt with the plugin disabled; **After** starts with `/i-am-not-a-developer`.

**Setup:** A folder with a small Vite site (`package.json` + `index.html`) that has never been installed or started. The agent can run commands.

**Prompt:** `my website shows ERR_CONNECTION_REFUSED when I open it in Chrome` → follow-up: `yes, it says localhost:5173`

## What changed

- **Before:** runs `npm install` without asking, says "I ran this in my sandboxed session", then hands over two commands and asks a two-part question.
- **After:** explains the error in plain words, asks before installing (cost, undo), does the work itself, writes `WHAT-WE-DID.md`, and ends with one action: reload the tab.

## Before (no skill)

> *tool: Bash — List working directory contents*

> *tool: Read — package.json*

> *tool: Read — index.html*

> *tool: Bash — Check if dependencies are installed and node/npm available*

> *tool: Bash — Install npm dependencies for the vite project*

> *tool: Bash — Start vite dev server briefly to confirm it starts and listens*

**Agent:**

Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. That's what `ERR_CONNECTION_REFUSED` means: no server there at all.

I ran `npm install` here and confirmed `npm run dev` starts fine, serving on `http://localhost:5173/`.

To fix it on your end, in the project folder run:
```
npm install
npm run dev
```
then open `http://localhost:5173` in Chrome. Note: I ran this in my sandboxed session, not your machine — you'll need to run those two commands yourself wherever you're opening Chrome from. If you're still getting `ERR_CONNECTION_REFUSED` after that, let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

**User:** yes, it says localhost:5173

**Agent:**

That matches — `localhost:5173` is exactly the port Vite serves on, and it'll refuse the connection until the dev server is actually running.

On your machine, in the project folder, run:
```
npm install
npm run dev
```
Leave that terminal running (don't close it), then reload `localhost:5173` in Chrome.

Have you run those two commands there yet, or did it already fail at `npm install`/`npm run dev`?

## After (`/i-am-not-a-developer`)

> *tool: Bash — List files in the project folder*

> *tool: Read — package.json*

> *tool: Read — index.html*

> *tool: Bash — Check if dependencies are installed and if vite is running*

**Agent:**

I looked at your project folder to see what's going on before asking you anything.

**What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing:
1. The website's building blocks ("dependencies" — code libraries the site needs) haven't been installed yet.
2. The little program that actually shows the site in your browser (the "server") isn't running.

That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.

**What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.

OK to go ahead? (yes/no)

**User:** yes, it says localhost:5173

> *tool: Bash — Install the website's dependencies*

> *tool: Write — WHAT-WE-DID.md*

> *tool: Bash — Start the website's local preview server*

**Agent:**

The building blocks installed fine, and I've started the preview server — it's now running at `http://localhost:5173/`.

I added a line to `WHAT-WE-DID.md` in your project folder noting this change and how to undo it.

Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

The diary it wrote (`WHAT-WE-DID.md`):

```markdown
# What we did

## 2026-09-24
- Installed the website's building blocks (a folder called `node_modules`) so the site can run. To undo: delete the `node_modules` folder — nothing else on your computer is affected.
```
