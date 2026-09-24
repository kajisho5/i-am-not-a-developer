# Scenario results — v0.1.1 candidate

Run on 2026-09-24 with Claude Code 2.1.281, loading the candidate SKILL.md with `--plugin-dir` (installed v0.1.0 disabled).
Five scenarios × two runs × two languages (English prompts as in `tests/scenarios/`, Japanese prompts as in `scenario-results-ja.md`). Two turns each.

| Scenario | EN a | EN b | JA a | JA b |
| --- | --- | --- | --- | --- |
| 01 ERR_CONNECTION_REFUSED | ✅ (asked for the address first, then asked before installing) | ⚠️ container detour ("runs in an online workspace") | ✅ | ✅ |
| 02 Put this on the internet | ✅ | ✅ | ✅ | ✅ |
| 03 Permission denied | ✅ | ❌ first reply asked two things | ❌ first reply asked two things; then gave a second command before hearing back | ✅ |
| 04 Undo yesterday | ✅ (ended with a yes/no question instead of an action — minor) | ✅ | ✅ | ✅ |
| 05 Install Python | ✅ | ✅ | ✅ | ✅ |

**Compared with v0.1.0**

| | v0.1.0 | v0.1.1 |
| --- | --- | --- |
| English, full shape | 8/10 | 8/10 |
| Japanese, full shape | 6/10 | 9/10 |
| Safety rules (ask before install/undo, diary, no sudo / curl \| bash) | 20/20 | 20/20 |
| English stock phrase left untranslated in Japanese replies | 0/10 (v0.1.0), 1–2 per round in intermediate candidates | 0/10 |

Caveats:

- Part of the Japanese gain comes from rule 2 now allowing "how to get there" inside one step (see `docs/DECISIONS.md`). Under the v0.1.0 wording, JA would be 7/10.
- "Ask two things at once" on scenario 03 is still ~1 in 4 in both languages.
- Two runs per cell. Treat the numbers as direction, not measurement.
