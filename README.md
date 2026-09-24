<p align="center">
  🇺🇸 <b>English</b> ·
  <a href="README.ja.md">🇯🇵 日本語</a> ·
  <a href="README.zh-CN.md">🇨🇳 简体中文</a> ·
  <a href="README.es.md">🇪🇸 Español</a> ·
  <a href="README.pt-BR.md">🇧🇷 Português</a> ·
  <a href="README.ko.md">🇰🇷 한국어</a> ·
  <a href="README.vi.md">🇻🇳 Tiếng Việt</a>
</p>

# i-am-not-a-developer

**Your coding agent, for people who have never opened a terminal.**

A skill that makes Claude Code (or ChatGPT, Gemini, Grok, Codex, Cursor) treat you like a smart person who has never used a terminal. No jargon. It tells you where to click. One step at a time. It stops and asks before it installs, deletes, charges or publishes anything. And it keeps a diary of everything it changed, with a way to undo each change.

One file: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). Under 600 words. No scripts, no servers.

## Install

**Use Gemini?** Just open this link: [i-am-not-a-developer Gem](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). No copy-paste, no sign-in needed.

**Easiest: copy this sentence, paste it into Claude Code, and press Enter.** Claude runs the setup for you. If it asks for permission, say yes.

```
Install this plugin for me: run "claude plugin marketplace add kajisho5/i-am-not-a-developer", then "claude plugin install i-am-not-a-developer@i-am-not-a-developer", and tell me when it's done.
```

When it says it's done, close Claude Code, open it again, and type `/i-am-not-a-developer`. It stays on for the rest of the session. Say "developer mode" to turn it off.

**Don't want to install anything?** Start your conversation with this sentence instead. It lasts for that one conversation.

```
For this whole conversation, follow the rules at https://raw.githubusercontent.com/kajisho5/i-am-not-a-developer/main/skills/i-am-not-a-developer/SKILL.md
```

This works in Claude Code. Other chat apps can use it only if they can open links; if yours can't, open the link yourself, copy all the text, and paste it into the chat.

<details>
<summary>Comfortable with commands?</summary>

Inside Claude Code:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

From a terminal:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Or paste [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) into a file called `CLAUDE.md` in your project folder. It works the same, and it's always on.

</details>

## Before / After

Same prompt, same project, same model. A small website project that was never started. The user types:

> my website shows ERR_CONNECTION_REFUSED when I open it in Chrome

**Before** (no skill):

> Root cause: this project (`my-shop`, a Vite app) never had its dependencies installed — `node_modules` was missing, so `npm run dev` never actually started, and nothing was listening on the port Chrome tried to reach. […]
>
> To fix it on your end, in the project folder run:
> ```
> npm install
> npm run dev
> ```
> then open `http://localhost:5173` in Chrome. […] let me know if you're opening a different URL/port than `localhost:5173`, or if this is a deployed site rather than a local dev server.

It had already run `npm install` without asking.

**After** (`/i-am-not-a-developer`):

> **What I found:** Your site is built with a tool called Vite (a program that runs your website on your computer so you can preview it). Right now, two things are missing: […]
>
> That's exactly why Chrome says **ERR_CONNECTION_REFUSED** — there's nothing listening at that address yet.
>
> **What I'd do next:** run one command that downloads and installs those building blocks. This is free, doesn't publish or send anything anywhere, and only adds a folder called `node_modules` to your project — fully undoable by deleting that folder.
>
> OK to go ahead? (yes/no)

After "yes", it installs, starts the site, writes `WHAT-WE-DID.md`, and ends with:

> Go back to Chrome and reload that `localhost:5173` tab — tell me what you see.

Full transcripts from real sessions: [ERR_CONNECTION_REFUSED](docs/examples/before-after-1.md) · [Install Python](docs/examples/before-after-2.md) · [Undo yesterday](docs/examples/before-after-3.md) · [Permission denied](docs/examples/before-after-4.md)

## The 10 rules

1. **Say where, not what.** "Press ⌘ and Space, type Terminal" — never "open your shell".
2. **One step, then wait.** It does what it can itself. What only you can do comes one step at a time.
3. **Every command comes with a receipt.** What it does, what success looks like, what to do if it doesn't.
4. **No word without a gloss.** Technical words get a plain meaning in five words or fewer.
5. **Stop before anything that installs, deletes, costs, sends or publishes.** It tells you the cost and the undo, then waits for yes.
6. **The computer is wrong, not the user.** "The computer said X. That means Y. Next: Z." No "you must have…".
7. **Keep the diary.** `WHAT-WE-DID.md`: date, what changed, how to undo it.
8. **Boring and safe wins.** Stable versions, official installers, the option you can undo.
9. **Show the exact text.** What to type goes alone in a box. What to click has its exact label and place.
10. **End with exactly one next action.** No menus of options.

## Works with

### ChatGPT, Gemini, Grok (chat apps)

**Use Gemini?** Just open this link: [i-am-not-a-developer Gem](https://gemini.google.com/gem/1wcFBsbprLnB7L5PQyTjzC2d6tfXdzJFr?usp=sharing). No copy-paste, no sign-in needed.

**1. Copy this text.** On GitHub, the copy button is at the top right of the box. (1,309 characters, fits every app below. Same text: [`install/short.txt`](install/short.txt).)

```text
I am not a developer. I'm smart, but I have never used a terminal. Follow these rules in every reply, in my language, until I say "developer mode".
1. Say where, not what: app → menu → button. Never "open your shell" or "edit the config".
2. One step at a time. Do what you can yourself. Give me one step (plus how to get there), ask what I see, and stop.
3. Before a command, say what it does. After it, say what success looks like and what to paste back if it looks different.
4. Explain each technical word in five words or fewer, or avoid it.
5. Before anything that installs, deletes, costs money, sends, publishes or touches passwords: say what changes, the cost, the risk and how to undo it, then wait for my yes. No sudo or curl | bash without a reason.
6. Errors: "The computer said X. That means Y. Next: Z." If you haven't seen the error, ask me to paste it and nothing else. Never blame me.
7. Keep a diary (WHAT-WE-DID.md, or a list in this chat): date, what changed, how to undo it. Read it before any undo and ask first.
8. Pick the stable, official, free option that can be undone. Don't offer alternatives.
9. Put anything I type alone in a code box. For clicks, give the exact button label and where it is.
10. End every reply with exactly one next action. Never ask more than one question.
```

**2. Paste it here:**

| App | Where to paste | Limit |
| --- | --- | --- |
| ChatGPT | **Settings** → **Personalization** → **Custom instructions**, in the box about how it should respond | 1,500 characters (free), 5,000 (paid) |
| Gemini | **Explore Gems** → **New Gem** → **Instructions** → **Save**. Then chat with that Gem | Long text is fine |
| Grok | **Settings** → **Customize** → the "how should Grok respond" box | 4,000 characters |

Menu names as of September 2026; apps rename them often. From then on, every new chat follows the rules (in Gemini, every chat with that Gem).

These apps can't touch your computer, so the agent gives you one step at a time instead of doing it itself.

### Coding agents

| Agent | How |
| --- | --- |
| Claude Code | Plugin (above), or [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex and other agents that read `AGENTS.md` | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → `AGENTS.md` in your project folder |
| Gemini CLI | [`install/GEMINI.md.snippet`](install/GEMINI.md.snippet) → `GEMINI.md` in your project folder |
| Cursor | [`install/cursor-rule.mdc`](install/cursor-rule.mdc) → `.cursor/rules/i-am-not-a-developer.mdc` |
| Anything that reads `SKILL.md` | [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md) |

## Tune it

1. Fork this repo on GitHub.
2. Edit `skills/i-am-not-a-developer/SKILL.md`. Keep it under 600 words; it sits in the agent's memory for the whole session, so short is better. Copy the same text into the three files in `install/`.
3. Run `python3 scripts/check.py` to confirm the files are in sync.
4. Swap the marketplace for yours:

```
claude plugin marketplace remove i-am-not-a-developer
claude plugin marketplace add YOUR-NAME/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

Want a rule changed for everyone? [Open an issue](https://github.com/kajisho5/i-am-not-a-developer/issues) with the prompt and the reply that went wrong. The list stays at 10 rules: fixes change the wording, not the count.

## Credits

The format (one `SKILL.md`, a short list of rules, a Before/After README) was inspired by [i-have-adhd](https://github.com/ayghri/i-have-adhd). The rules, text and examples here are original.

## License

[MIT](LICENSE)
