# pinakactf-writeup-skill

A Claude Code / Codex helper for PinakaCTF 2026 write-up preparation, designed around the participant's own account of an already-solved challenge.

**No template. No fixed write-up format.** It does not force headings, sections, numbered steps, bullet lists, tables, a TL;DR, introduction, conclusion, or a standard narrative pattern. The participant's own wording and natural flow decide how the account reads.

PinakaCTF requires handwritten write-ups in the participant's own words and prohibits AI-written submissions. This skill helps recover the participant's own actions and organize genuine screenshots. Any DOCX it creates is a plain reference copy, not a substitute for the participant's handwritten submission.

## What it does

- works in the same conversation where the challenge was solved;
- keeps the participant's own wording instead of generating a polished narrative;
- asks only for missing facts, using short neutral questions;
- ignores assistant suggestions that were never actually performed;
- omits failed attempts by default;
- places 3–6 genuine screenshots directly beside the relevant account;
- uses category knowledge only to select useful evidence;
- includes the exact full flag at the end;
- can create a plain DOCX with no imposed layout.

## Use

In the solved conversation, ask:

```text
make the Pinaka write-up from this chat
```

The skill reads the conversation already in context. It does not ask you to paste it again.

If a Word reference is needed, the agent builds an ordered content manifest and runs:

```bash
pip install python-docx
python scripts/build_reference_docx.py manifest.json Challenge_Name_notes.docx
```

The manifest is an internal way to place the participant's text and screenshots in order. It is not a required write-up format.

## Files

- `SKILL.md` — main skill
- `CLAUDE.md` — Claude Code instructions
- `AGENTS.md` — Codex instructions
- `references/human-authoring.md` — primary authorship rules
- `references/screenshot-selection.md` — genuine screenshot handling
- `references/category-evidence.md` — category-specific evidence hints
- `scripts/build_reference_docx.py` — plain DOCX assembler
- `assets/manifest-example.json` — internal assembly example

## Important

Do not use this skill to disguise AI authorship, fabricate a solve, invent screenshots, or bypass the event's rules. The participant must handwrite the actual submission in their own words.
