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

A skill that makes Claude Code (or Codex, or Cursor) treat you like a smart person who has never used a terminal. No jargon. It tells you where to click. One step at a time. It stops and asks before it installs, deletes, charges or publishes anything. And it keeps a diary of everything it changed, with a way to undo each change.

One file: [`skills/i-am-not-a-developer/SKILL.md`](skills/i-am-not-a-developer/SKILL.md). Under 600 words. No scripts, no servers.

## Install

Type these three lines into Claude Code, one at a time:

```
/plugin marketplace add kajisho5/i-am-not-a-developer
/plugin install i-am-not-a-developer@i-am-not-a-developer
/i-am-not-a-developer
```

The last line turns it on. It stays on for the rest of the session. Say "developer mode" to turn it off.

From a terminal instead:

```
claude plugin marketplace add kajisho5/i-am-not-a-developer
claude plugin install i-am-not-a-developer@i-am-not-a-developer
```

**Can't run those?** Paste [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) into a file called `CLAUDE.md` in your project folder. It works the same, and it's always on.

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

| Agent | How |
| --- | --- |
| Claude Code | Plugin (above), or [`install/CLAUDE.md.snippet`](install/CLAUDE.md.snippet) → `CLAUDE.md` |
| Codex and other agents that read `AGENTS.md` | [`install/AGENTS.md.snippet`](install/AGENTS.md.snippet) → `AGENTS.md` in your project folder |
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
