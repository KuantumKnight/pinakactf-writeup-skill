---
name: pinakactf-writeup
version: 1.1.0
description: Help the participant prepare a free-form PinakaCTF 2026 write-up from their own solved conversation, with genuine screenshots and no imposed template.
---

# PinakaCTF Write-up Helper

## Purpose

Use this skill only for an already-solved PinakaCTF 2026 challenge. Work from the current conversation and genuine files or screenshots from the participant's own system.

**There is no write-up format.** Do not impose a template, fixed sequence of sections, headings, numbered steps, bullet lists, tables, TL;DR, introduction, conclusion, tools-used list, methodology section, or standard paragraph pattern. Let the account follow the way the participant naturally describes the solve.

The competition requires handwritten write-ups in the participant's own words and prohibits AI-written submissions. This skill therefore helps the participant recover their own account and organize genuine evidence; it must not replace their authorship. A Word file, if requested, is only a plain reference containing the participant's own wording and genuine screenshots, not a submission-ready AI-authored write-up.

## Priority

Human authorship comes first. Screenshots and category-specific evidence are secondary. Formatting is not a goal.

- Preserve the participant's own wording and natural order wherever possible.
- Keep it casual and direct if that is how the participant speaks.
- Explain only when the participant's account needs a missing link to make the action understandable.
- Do not turn short observations into polished cybersecurity prose.
- Do not add filler, generic explanations, or textbook theory.
- Do not force a particular length. Include only what is needed to explain the actual solve.
- Omit failed attempts by default, as requested.
- Include the exact full flag at the end of the reference material.
- Include 3–6 genuine screenshots per challenge, as required by PinakaCTF.

## Invocation

The participant will normally invoke this skill in the same conversation where the challenge was solved, for example:

`make the Pinaka write-up from this chat`

Use the conversation already in context. Do not ask the participant to paste it again.

## Non-negotiable authorship rules

1. Include an action only when the participant performed it or confirms they performed it.
2. Never present an assistant suggestion as something the participant did.
3. Prefer the participant's exact words. Do not author connective explanations on their behalf.
4. If an essential part is missing, ask one short, neutral question at a time, such as: `What did you actually do next?`
5. Do not suggest an answer inside the question.
6. Do not invent commands, outputs, reasoning, screenshots, tool usage, or flag construction.
7. Do not add deliberate typos, fake mistakes, artificial hesitations, or other devices intended to disguise AI involvement.
8. Do not claim the result is human-authored. The participant must write the final competition submission themselves.

## Workflow

### First: recover the participant's account

Read `references/human-authoring.md` before processing the solve. Identify the participant's own observations, actions, commands, and descriptions. Ignore assistant-only suggestions unless the participant later confirms them.

Do not convert the conversation into a checklist or numbered solve path. Understand the real sequence internally, then preserve the participant's natural telling of it.

If the conversation already explains the solve clearly, do not ask unnecessary questions. If an essential action is unclear, ask one concise, non-leading question and wait.

### Then: choose the evidence

Read `references/screenshot-selection.md` and the relevant category notes in `references/category-evidence.md`. These references are only for deciding which evidence matters. They must never dictate the prose or impose a structure.

Choose 3–6 screenshots that show the decisive parts of the solve. Place each screenshot immediately after the participant's words that it supports. Do not create a numbered screenshot list, captions, a screenshot gallery, or a separate evidence section.

Use genuine screenshots from the participant's own machine. If the current environment has authorized access to the relevant browser, terminal, or application, capture the actual screen state. Reproduce only steps that the participant really performed. If capture is not possible, ask for the real screenshot or leave a plain, temporary note at the exact insertion point, such as `(screenshot needed: /robots.txt with the hidden path visible)`. Never pretend a placeholder is a screenshot.

### Then: prepare the material

If a DOCX is requested, create a plain Word document containing only:
- the participant's own text, in the participant's natural order;
- genuine screenshots placed where they belong;
- a plain screenshot reminder at the relevant point only when the image is not yet available;
- the exact full flag as the final text.

Do not add a title page, metadata table, headings, labels, numbered steps, bullets, decorative styling, borders, screenshot captions, headers, footers, or a forced conclusion. Use normal Word defaults. Do not rewrite the participant's words to fill space.

Use the ordered `content` array in `assets/manifest-example.json` as an internal assembly format only. It is not a write-up template.

Generate the DOCX with:

```bash
python scripts/build_reference_docx.py manifest.json <Challenge_Name>_notes.docx
```

### Final check

Check that:
- every described action is participant-performed or participant-confirmed;
- the wording remains the participant's own;
- no assistant-only suggestion has slipped into the account;
- failed attempts are omitted unless requested;
- there are 3–6 genuine screenshot images or clearly marked screenshot reminders awaiting replacement;
- screenshots appear beside the relevant part of the account;
- the full flag is exact and last;
- the document has no imposed write-up template.

## Category handling

Supported categories: Web, Pwn, Crypto, Forensics, Reverse, OSINT, and Misc. Use category-specific knowledge only to identify decisive evidence. Never make the prose sound like a category-specific template.

## Completion message

Keep the completion message short. State what evidence was included and whether any screenshot reminders still need real captures. Do not claim that the Word reference is a compliant final submission.
