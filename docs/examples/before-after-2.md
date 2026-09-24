# Before / After: "Install Python for me"

Scenario `tests/scenarios/05-*.md`. Recorded on 2026-09-24 with Claude Code 2.1.281 (`claude -p`, then `--resume` for the second turn) in a Linux container. Replies are copied verbatim; tool calls are shown as one-line notes. **Before** is the same prompt with the plugin disabled; **After** starts with `/i-am-not-a-developer`.

**Setup:** An empty folder. Chat-only: the agent's command tool is turned off and it is told the user runs every command themselves.

**Prompt:** `install python for me` → follow-up: `Mac`

## What changed

- **Before:** four operating systems at once, then two options for Mac, one of which pipes a script from the internet into bash.
- **After:** one question (Mac or Windows?), then one harmless check with where to click, what success looks like, and "Tell me what you see."

## Before (no skill)

**Agent:**

I don't have access to your computer in this session, so I can't run the installation myself — but here's how to do it, depending on your OS:

**Windows**
1. Download the installer from the official source (python.org/downloads)
2. Run it, and check **"Add python.exe to PATH"** before clicking Install
3. Verify: open a new terminal and run `python --version`

**macOS**
- Easiest: `brew install python3` (requires Homebrew)
- Or download the installer from python.org/downloads
- Verify: `python3 --version`

**Linux (Debian/Ubuntu)**
```
sudo apt update
sudo apt install python3 python3-pip
```
**Linux (Fedora)**
```
sudo dnf install python3 python3-pip
```

Let me know which OS you're on and I'll give you the exact commands/steps, or troubleshoot if something goes wrong once you run them.

**User:** Mac

**Agent:**

Here's how to install Python on macOS:

**Option 1: Homebrew (recommended)**

If you don't have Homebrew yet, install it first:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Then install Python:
```
brew install python3
```
Verify:
```
python3 --version
pip3 --version
```

**Option 2: Official installer**
1. Go to python.org/downloads/macos
2. Download the latest macOS installer (`.pkg`)
3. Run it and follow the prompts
4. Verify with `python3 --version` in Terminal

**Note:** macOS comes with a system Python, but it's usually outdated or missing (Apple removed it in newer macOS versions), so don't rely on that — use one of the methods above.

After installing, run those in your Terminal app and paste back any output if something doesn't work as expected.

## After (`/i-am-not-a-developer`)

**Agent:**

I'll help you get Python (a programming language many apps and scripts need) installed on your computer.

The exact steps depend on whether you're on a Mac or a Windows computer, so I want to make sure I give you the right instructions.

Are you using a Mac or a Windows computer?

**User:** Mac

**Agent:**

Good — on a Mac, before installing anything I want to check whether Python is already on your computer. This is just a look, it won't change anything.

**Open Terminal** (a window for typing commands): press **⌘ Space**, type `Terminal`, then press **Return**.

In the window that opens, paste this and press **Return**:

```
python3 --version
```

- If it worked, you'll see something like `Python 3.13.x` — that means Python is already there.
- If instead you see something like `command not found`, that means Python isn't installed yet, and we'll install it next.

Tell me what you see.
