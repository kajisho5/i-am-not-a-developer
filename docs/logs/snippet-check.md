# Snippet check: CLAUDE.md only, plugin disabled

Recorded on 2026-09-24 with Claude Code 2.1.281. The plugin was disabled (`claude plugin disable`), `install/CLAUDE.md.snippet` was copied to `CLAUDE.md` in the test folder, and the prompt was sent **without** `/i-am-not-a-developer`.

## Scenario 01

> *tool: Bash — List files in the project folder*

> *tool: Read — package.json*

> *tool: Read — index.html*

> *tool: Bash — Check if dependencies are installed and if the server is running*

**Agent:**

I found the site's project folder. It's a small project (called "my-shop") that needs its own program running to show the page — that program (called **Vite**, a tool that runs your site while you build it) has never been set up here yet, which is why Chrome can't connect.

To fix this I need to install that tool. Here's what that means:
- **What it does:** downloads and sets up Vite so your site can run.
- **Cost:** free.
- **What could go wrong:** a slow or failed download (fixable by trying again); nothing on your computer is deleted or changed outside this project folder.
- **Undo:** delete the folder it creates (`node_modules`) — I'll note this in the diary once done.

OK to go ahead? (yes/no)

**User:** yes, it says localhost:5173

> *tool: Bash — Install project dependencies*

> *tool: Bash — Start the Vite dev server in the background*

> *tool: Write — WHAT-WE-DID.md*

**Agent:**

Your site is now running. Reload the page at `localhost:5173` in Chrome.

Tell me what you see.


## Scenario 05

**Agent:**

I can help with that. I need to know which computer you're using, since the steps are different.

Are you on a Mac or on Windows?

**User:** Mac

**Agent:**

Before installing anything, let's check if Python is already on your computer — that way we don't install something you already have.

Open **Terminal** (a window for typing commands): press **⌘ Space** together, type `Terminal`, then press **Return**.

In the Terminal window, type this exactly and press **Return**:

```
python3 --version
```

If Python is already installed, you'll see something like `Python 3.` followed by numbers. If instead it says something like `command not found`, that means it's not installed yet, and we'll install it next.

Tell me what you see.

