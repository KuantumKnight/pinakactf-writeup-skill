# pinakactf-writeup-skill

A small Claude Code / Codex skill for turning an **already solved** PinakaCTF 2026 conversation into a compact handwriting/evidence reference pack.

It is intentionally optimized for lazy, short write-ups: successful path only, 3-6 useful screenshots, almost no theory, and the full flag at the end.

## Important

PinakaCTF's supplied rules require the final write-up to be handwritten and in the participant's own words. This repository does not try to bypass that rule. It organizes verified solve evidence and produces a DOCX reference sheet that you can use while writing the final submission by hand.

## What it does

- reads the already-solved chat in context;
- strips assistant suggestions that were never executed;
- keeps the shortest successful path;
- keeps failed attempts out by default;
- selects 3-6 meaningful screenshots;
- supports Web, Crypto, Forensics, Reverse, Pwn, OSINT, and Misc;
- includes the exact full flag;
- builds a clean Word reference sheet.

## Typical use

In the same conversation where the challenge was solved:

```text
make Pinaka writeup for this
```

The agent follows `SKILL.md`, verifies the successful path, gathers or requests genuine screenshots, creates a small JSON manifest, then runs:

```bash
python scripts/build_reference_docx.py manifest.json Challenge_Name_handwriting_sheet.docx
```

## Minimal style

The intended note style is short and factual:

```text
Checked /robots.txt and found /secret.
Opened it, got an encoded string.
Put it in CyberChef -> Base64 decode.
That gave the flag.
```

Use the participant's own wording from the solve conversation whenever available.

## Repo layout

```text
SKILL.md
CLAUDE.md
AGENTS.md
references/
  human-authoring.md
  category-evidence.md
  screenshot-selection.md
scripts/
  build_reference_docx.py
assets/
  manifest-example.json
examples/
  example-manifest.json
```

## Requirements

```bash
pip install python-docx
```

## License

MIT
