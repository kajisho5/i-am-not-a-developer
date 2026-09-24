# Decisions

One line per decision. Newest at the bottom.

- 2026-09-24 P0: Plugin and marketplace share one repo (`"source": "./"` in marketplace.json), as documented at https://code.claude.com/docs/en/plugin-marketplaces.
- 2026-09-24 P0: No `commands/` directory. A plugin skill at `skills/<name>/SKILL.md` is registered as `/i-am-not-a-developer:i-am-not-a-developer` with the alias `/i-am-not-a-developer` (verified on Claude Code 2.1.281 via the `commands_changed` stream event). Docs: https://code.claude.com/docs/en/skills.
- 2026-09-24 P0: Model invocation stays enabled (no `disable-model-invocation`), so the description's trigger words ("not a developer", "非エンジニア", …) can switch the skill on without the slash command.
- 2026-09-24 P0: Only `name` is required in plugin.json; we also set `version` so users get updates only when release-please bumps it.
- 2026-09-24 P1: Snippets carry the SKILL.md body verbatim; `scripts/check.py` fails CI if they drift.
- 2026-09-24 P1: The 600-word limit applies to the SKILL.md body (everything after the frontmatter).
- 2026-09-24 P1: Rule 2 lets the agent run a step itself when it has tools, because Claude Code usually can; only steps the user must do are handed over one at a time.
- 2026-09-24 P1: "Reply in the user's language" lives in the intro, not as an 11th rule.
- 2026-09-24 P1: The off switch is the phrase "developer mode".
- 2026-09-24 P2 (round 1→2): Rule 1 — asked Mac/Windows even when irrelevant. Now: ask only "if the steps differ on Mac and Windows and you can't check yourself".
- 2026-09-24 P2 (round 1→2): Never list — agent asked the user for things it could look up. "Never say read the docs" became "Never ask what you can find out yourself: look at the files, run a harmless check, read the docs."
- 2026-09-24 P2 (round 1→2): Removed the "Shape of a reply" section to stay under 600 words; rules 2, 3 and 10 already cover it.
- 2026-09-24 P2 (round 2→3): Rule 8 — agent offered GitHub *or* Netlify. Added "with the fewest sign-ups". Rule 10 — "the single thing to do or answer now", so a final question counts as the one action.
- 2026-09-24 P2 (round 2→3): Never list — "Never ask for two things" was ignored; reworded to "Never ask more than one question per reply."
- 2026-09-24 P2 (round 3→5): Rule 5 — for steps the user runs, the agent asked "OK to go ahead?" and gave no step. Now: "If you are doing it, ask … and wait. If they are doing it, give their one step right away; doing it is their yes."
- 2026-09-24 P2 (round 3→5): Rule 7 — "undo what we did yesterday" was edited without asking in 3 of 4 runs (editing a file is not install/delete). Now: "Before any undo, read the diary, say what will change back and wait for yes." 4/4 passed afterwards.
- 2026-09-24 P2 (round 6→7): Rule 6 — first reply to "permission denied" asked two or three questions. Added "Haven't seen the error? Ask them to paste it, and nothing else."
- 2026-09-24 P2 (round 7→8): Rule 7 — one run installed and started a server but skipped the diary. Now "add a dated entry before replying". 2/2 wrote the diary afterwards.
- 2026-09-24 P2: Stopped at round 8 (10 runs, 2 per scenario). Remaining misses are minor and inconsistent: "Open index.html in your browser" without saying where to click, and an occasional second clause in a question.
- 2026-09-24 P2: Before/After examples use real transcripts from `claude -p` with the plugin disabled (Before) and enabled (After). Chat-only scenarios (03, 05) run with the command tool disabled.
- 2026-09-24 P5: release-please with `release-type: simple`, `initial-version: 0.1.0` and an empty manifest (`{}`), so the first release PR is v0.1.0. `extra-files` bumps `.claude-plugin/plugin.json` `$.version` (JSON updater, per release-please docs/customizing.md).
- 2026-09-24 P4: Translations keep the Before/After transcripts in English (they are real recordings) and translate only the narrative. Line-match check against i-have-adhd: 0 prose lines; the only identical lines are markup (`<p align="center">`, `| --- | --- |`), `license: MIT` and one- or two-word headings such as "## Instalación".
- 2026-09-24 P5: The repo requires actions pinned to full commit SHAs (the first release run failed with "all actions must be pinned to a full-length commit SHA"). Pinned every action to the latest tag of the major we already used, with the tag in a comment.
- 2026-09-24 v0.1.1: Rule 2 — Japanese replies split "open Terminal, then type one command" into numbered micro-steps. That is one step, not a list of tasks, so the rule now says "give one step: one command, click or paste, plus how to get there … Never give a second step before hearing back." This changes the grading as much as the behavior; it is recorded as such in `docs/logs/scenario-results-v0.1.1.md`.
- 2026-09-24 v0.1.1: Rules 2 and 5 — Japanese replies sometimes ended with the literal English "Tell me what you see." / "OK to go ahead?". Both quoted phrases now say "in their language". A single "reply in the user's language, including the quoted phrases" line in the intro did not stop it (2 slips in 8 replies), per-rule markers did (0 in 10).
- 2026-09-24 v0.1.1: Rule 6 — "Ask for exactly one thing: the error, pasted." Still ~1 in 4 first replies to "permission denied" ask two things, in both languages. Known limitation; not fixed by wording so far.
- 2026-09-24 v0.1.1: Word budget kept at ≤600 by dropping "ports", "in plain words", "the/files/docs" articles and shortening rule 5's access/password clause.
- 2026-09-24 README: The first install path is now one sentence the user pastes into Claude Code; Claude runs the two `claude plugin` commands. A vaguer sentence ("install the kajisho5/i-am-not-a-developer plugin") failed in a cloud session (the agent searched a plugin catalog instead), so the sentence names both commands. Verified: fresh uninstall → `claude -p` with that sentence → v0.1.1 installed from GitHub.
- 2026-09-24 README: Zero-install path: "follow the rules at <raw SKILL.md URL>" as the first message. Verified in Claude Code with the plugin disabled (asked Mac/Windows alone for "Python 入れて"). Not verified in other chat apps; the README says it depends on whether they can open links.
- 2026-09-24 README: The `/plugin` and terminal commands moved into a collapsed "Comfortable with commands?" block.
