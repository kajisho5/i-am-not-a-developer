#!/usr/bin/env python3
"""Repository checks for i-am-not-a-developer. Standard library only.

- required files exist
- JSON manifests parse and carry the required keys
- SKILL.md frontmatter has name/description and the body is <= 600 words
- the SKILL.md body appears verbatim in every install/ snippet
- plugin.json and marketplace.json agree on the plugin name
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/i-am-not-a-developer/SKILL.md"
SNIPPETS = ["install/CLAUDE.md.snippet", "install/AGENTS.md.snippet", "install/cursor-rule.mdc"]
READMES = ["README.md", "README.ja.md", "README.zh-CN.md", "README.es.md",
           "README.pt-BR.md", "README.ko.md", "README.vi.md"]
REQUIRED = [
    ".claude-plugin/plugin.json",
    ".claude-plugin/marketplace.json",
    "skills/i-am-not-a-developer/SKILL.md",
    "LICENSE",
    "CHANGELOG.md",
    "docs/DECISIONS.md",
    *SNIPPETS,
    *READMES,
]
MAX_WORDS = 600
NAME = "i-am-not-a-developer"

errors = []


def fail(msg):
    errors.append(msg)


def load_json(rel):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        fail(f"{rel}: {e}")
        return None


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        return None, text
    return m.group(1), m.group(2)


def main():
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            fail(f"missing file: {rel}")

    plugin = load_json(".claude-plugin/plugin.json")
    if plugin is not None:
        if plugin.get("name") != NAME:
            fail(f"plugin.json: name must be {NAME!r}")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(plugin.get("version", ""))):
            fail("plugin.json: version must be X.Y.Z")

    market = load_json(".claude-plugin/marketplace.json")
    if market is not None:
        for key in ("name", "owner", "plugins"):
            if key not in market:
                fail(f"marketplace.json: missing {key!r}")
        if not isinstance(market.get("owner"), dict) or "name" not in market.get("owner", {}):
            fail("marketplace.json: owner.name is required")
        plugins = market.get("plugins") or []
        if not plugins:
            fail("marketplace.json: plugins must not be empty")
        for i, p in enumerate(plugins):
            for key in ("name", "source"):
                if key not in p:
                    fail(f"marketplace.json: plugins[{i}] missing {key!r}")
        if plugins and plugins[0].get("name") != NAME:
            fail(f"marketplace.json: plugins[0].name must be {NAME!r}")
        if plugins and plugins[0].get("source") != "./":
            fail("marketplace.json: plugins[0].source must be './' (this repo)")

    if SKILL.is_file():
        fm, body = split_frontmatter(SKILL.read_text(encoding="utf-8"))
        if fm is None:
            fail("SKILL.md: missing frontmatter")
        else:
            if not re.search(rf"^name:\s*{NAME}\s*$", fm, re.M):
                fail(f"SKILL.md: frontmatter name must be {NAME}")
            if not re.search(r"^description:", fm, re.M):
                fail("SKILL.md: frontmatter description is required")
        body = body.strip()
        words = len(body.split())
        print(f"SKILL.md body: {words} words (limit {MAX_WORDS})")
        if words > MAX_WORDS:
            fail(f"SKILL.md: body is {words} words, limit is {MAX_WORDS}")
        rule_section = body.split("## The 10 rules", 1)[-1].split("\n## ", 1)[0]
        count = len(re.findall(r"^\d+\. \*\*", rule_section, re.M))
        if count != 10:
            fail(f"SKILL.md: expected 10 rules, found {count}")
        for rel in SNIPPETS:
            path = ROOT / rel
            if path.is_file() and body not in path.read_text(encoding="utf-8"):
                fail(f"{rel}: out of sync with the SKILL.md body (copy it verbatim)")

    if errors:
        for e in errors:
            print(f"FAIL {e}")
        return 1
    print("OK all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
