#!/usr/bin/env python3
"""Validate the structure of a plan-build ready-to-paste brief.

Usage:
    python3 scripts/validate-brief.py <brief.md> [more.md ...]

Exit status is 0 when every file passes, 1 when any check fails,
and 2 when no file path is given.

Checks headings, a user story, an acceptance criterion, non-empty
in-scope and out-of-scope text, and placeholder tokens in mandatory
fields. It does not judge whether the requirements are clear or true.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_H2 = (
    "Context",
    "Desired outcome",
    "Scope",
    "User stories",
    "Acceptance criteria",
    "Constraints",
    "Assumptions",
    "Open questions",
    "Build sequence",
)

MANDATORY_FIELDS = {
    "Context": (
        "Request source",
        "Primary user",
        "Secondary users / approvers",
        "Problem or opportunity",
        "Current behavior / workaround",
    ),
    "Desired outcome": (
        "User outcome",
        "Business or client outcome",
        "Prototype question",
        "Success looks like",
    ),
    "Scope": (
        "In scope",
        "Out of scope",
        "Future considerations",
    ),
    "Constraints": (
        "Technical",
        "Design/brand",
        "Data/privacy",
        "Timeline/budget",
        "Platform",
    ),
}

PLACEHOLDER_RES = (
    re.compile(r"\bTBD\b", re.IGNORECASE),
    re.compile(r"\bTODO\b", re.IGNORECASE),
    re.compile(r"\bFIXME\b", re.IGNORECASE),
    re.compile(r"\[user\]", re.IGNORECASE),
    re.compile(r"\[goal\]", re.IGNORECASE),
    re.compile(r"\[benefit\]", re.IGNORECASE),
    re.compile(r"\[context\]", re.IGNORECASE),
    re.compile(r"\[action\]", re.IGNORECASE),
    re.compile(r"\[observable result\]", re.IGNORECASE),
    re.compile(r"\[short title\]", re.IGNORECASE),
)

STORY_RE = re.compile(
    r"\bas\s+(?:a|an|the)\b.+?\bi want\b.+?\bso that\b",
    re.IGNORECASE | re.DOTALL,
)
GWT_RE = re.compile(r"\bgiven\b.+?\bwhen\b.+?\bthen\b", re.IGNORECASE | re.DOTALL)
NUMBERED_STEP_RE = re.compile(r"^\s*\d+\.\s+\S", re.MULTILINE)


def extract_brief(text: str) -> str | None:
    match = re.search(r"(?m)^# Ready-to-paste brief\s*$", text)
    if not match:
        return None
    return text[match.start() :]


def parse_sections(brief: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for part in re.split(r"(?m)^(?=## )", brief):
        match = re.match(r"##\s+(.+?)\s*\n(.*)$", part, re.DOTALL)
        if match:
            sections[match.group(1).strip()] = match.group(2)
    return sections


def field_value(section: str, label: str) -> str | None:
    lines = section.splitlines()
    label_re = re.compile(
        rf"^(\s*)[-*]\s+\**{re.escape(label)}\**\s*:\s*(.*)$"
    )
    for index, line in enumerate(lines):
        match = label_re.match(line)
        if not match:
            continue
        base = len(match.group(1))
        chunks = [match.group(2).strip()]
        cursor = index + 1
        while cursor < len(lines):
            follow = lines[cursor]
            if follow.strip() == "":
                peek = cursor + 1
                while peek < len(lines) and lines[peek].strip() == "":
                    peek += 1
                if peek >= len(lines):
                    break
                next_indent = len(re.match(r"(\s*)", lines[peek]).group(1))
                if next_indent > base:
                    cursor = peek
                    continue
                break
            next_indent = len(re.match(r"(\s*)", follow).group(1))
            if next_indent > base:
                chunks.append(follow.strip())
                cursor += 1
                continue
            break
        return "\n".join(chunk for chunk in chunks if chunk).strip()
    return None


def placeholder_hit(text: str) -> str | None:
    for pattern in PLACEHOLDER_RES:
        found = pattern.search(text)
        if found:
            return found.group(0)
    return None


def validate(text: str) -> list[str]:
    errors: list[str] = []
    brief = extract_brief(text)
    if brief is None:
        return ["Missing exact heading: # Ready-to-paste brief"]

    sections = parse_sections(brief)
    for heading in REQUIRED_H2:
        if heading not in sections:
            errors.append(f"Missing heading: ## {heading}")

    for section_name, labels in MANDATORY_FIELDS.items():
        body = sections.get(section_name)
        if body is None:
            continue
        for label in labels:
            value = field_value(body, label)
            where = f"{section_name} > {label}"
            if value is None:
                errors.append(f"Missing field: {where}")
                continue
            if value.strip() == "":
                errors.append(f"Empty field: {where}")
                continue
            hit = placeholder_hit(value)
            if hit:
                errors.append(f"Placeholder {hit!r} in {where}")

    stories = sections.get("User stories")
    if stories is not None:
        if not STORY_RE.search(stories):
            errors.append(
                "User stories: need at least one "
                "'As a ..., I want ..., so that ...' story"
            )
        hit = placeholder_hit(stories)
        if hit:
            errors.append(f"Placeholder {hit!r} in User stories")

    criteria = sections.get("Acceptance criteria")
    if criteria is not None:
        has_gwt = GWT_RE.search(criteria) is not None
        has_bullet = re.search(r"(?m)^\s*[-*]\s+\S", criteria) is not None
        if not has_gwt and not has_bullet:
            errors.append(
                "Acceptance criteria: need at least one criterion"
            )
        hit = placeholder_hit(criteria)
        if hit:
            errors.append(f"Placeholder {hit!r} in Acceptance criteria")

    for freeform in ("Assumptions", "Open questions", "Build sequence"):
        body = sections.get(freeform)
        if body is None:
            continue
        if re.search(r"[A-Za-z0-9]", body) is None:
            errors.append(f"Empty section: {freeform}")
        hit = placeholder_hit(body)
        if hit:
            errors.append(f"Placeholder {hit!r} in {freeform}")

    steps = sections.get("Build sequence")
    if steps is not None and not NUMBERED_STEP_RE.search(steps):
        errors.append("Build sequence: need at least one numbered step")

    return errors


def main(argv: list[str]) -> int:
    if not argv:
        print(
            "Usage: python3 scripts/validate-brief.py <brief.md> [more.md ...]",
            file=sys.stderr,
        )
        return 2

    failed = False
    for raw_path in argv:
        path = Path(raw_path)
        if not path.is_file():
            failed = True
            print(f"FAIL: {raw_path}")
            print("  - File not found")
            continue
        errors = validate(path.read_text(encoding="utf-8"))
        if errors:
            failed = True
            print(f"FAIL: {raw_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"ok: {raw_path}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
