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
