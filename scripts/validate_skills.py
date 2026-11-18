#!/usr/bin/env python3
"""Validate every skill: frontmatter, naming, description, links, evals, triggers.

Usage: python3 scripts/validate_skills.py   (exit code 1 on any error)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")


def parse_frontmatter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = {}
    for line in text[4:end].splitlines():
        m = re.match(r"^([a-z_]+):\s*(.*)$", line)
        if m:
            fm[m.group(1)] = m.group(2).strip().strip('"')
    return fm


def validate():
    errors = []
    names = set()
    for skill_dir in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        name = skill_dir.name
        names.add(name)
        md = skill_dir / "SKILL.md"
        if not md.exists():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = md.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{name}: missing or malformed frontmatter")
            continue
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name '{fm.get('name')}' != folder")
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append(f"{name}: name must be kebab-case, <=64 chars")
        desc = fm.get("description", "")
        if not desc:
            errors.append(f"{name}: empty description")
        elif len(desc) > 1024:
            errors.append(f"{name}: description {len(desc)} chars > 1024")
        elif "use when" not in desc.lower() and "use at" not in desc.lower() and "use for" not in desc.lower():
            errors.append(f"{name}: description should say when to use it")
        if text.count("\n") > 400:
            errors.append(f"{name}: SKILL.md over 400 lines; move detail to references/")
        # links in SKILL.md and references
        for f in [md, *sorted((skill_dir / "references").glob("*.md"))]:
            for target, _ in LINK_RE.findall(f.read_text(encoding="utf-8")):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (f.parent / target).resolve().exists():
                    errors.append(f"{name}: broken link '{target}' in {f.relative_to(ROOT)}")
        # evals
        ev = skill_dir / "evals" / "evals.json"
        if not ev.exists():
            errors.append(f"{name}: missing evals/evals.json")
        else:
            try:
                data = json.loads(ev.read_text(encoding="utf-8"))
                if data.get("skill_name") != name:
                    errors.append(f"{name}: evals skill_name mismatch")
                cases = data.get("evals", [])
                if len(cases) < 2:
                    errors.append(f"{name}: needs at least 2 evals")
                for c in cases:
                    for k in ("id", "prompt", "expected_output", "assertions"):
                        if k not in c:
                            errors.append(f"{name}: eval missing '{k}'")
            except json.JSONDecodeError as e:
                errors.append(f"{name}: invalid evals JSON ({e})")
        if not (skill_dir / "references").is_dir():
            errors.append(f"{name}: missing references/ folder")

    trig = ROOT / "evals" / "triggers" / "triggers.json"
    if trig.exists():
        data = json.loads(trig.read_text(encoding="utf-8"))
        covered = set()
        for c in data.get("cases", []):
            if c["expected_skill"] not in names:
                errors.append(f"triggers: unknown skill '{c['expected_skill']}'")
            covered.add(c["expected_skill"])
        for n in sorted(names - covered):
            errors.append(f"triggers: no trigger case for '{n}'")

    for doc in [ROOT / "README.md", *sorted((ROOT / "docs").glob("*.md"))]:
        for target, _ in LINK_RE.findall(doc.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if not (doc.parent / target).resolve().exists():
                errors.append(f"broken link '{target}' in {doc.relative_to(ROOT)}")
    return names, errors


if __name__ == "__main__":
    names, errors = validate()
    for e in errors:
        print(f"ERROR: {e}")
    print(f"{len(names)} skills checked, {len(errors)} error(s).")
    sys.exit(1 if errors else 0)
