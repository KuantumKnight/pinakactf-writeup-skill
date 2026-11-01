---
name: pinakactf-writeup
version: 1.0.0
description: Turn an already-solved PinakaCTF conversation into a concise handwritten-writeup evidence pack using only verified user actions, genuine screenshots, and the full recovered flag.
---

# PinakaCTF Write-up Coach

## Scope

Use this skill only after the challenge is already solved. The source of truth is the current conversation plus files/screenshots produced on the user's own system.

The skill exists to reduce clerical work around PinakaCTF write-up preparation. It does **not** fabricate a solve path, invent terminal output, manufacture screenshots, or intentionally disguise AI authorship. PinakaCTF requires the final write-up to be handwritten and in the participant's own words, so the DOCX produced by this skill is a **copy/evidence sheet for handwriting**, not a submission-ready substitute for that requirement.

## User preferences for this skill

- Event: PinakaCTF 2026 only.
- Output tone: very short, casual, practical, no essay voice.
- Explain only when the explanation is needed to understand why the next step worked.
- Omit failed attempts unless the user explicitly asks to keep one.
- Include the full flag.
- Use 3 to 6 screenshots per challenge.
- Prefer the minimum number of screenshots that still proves the solve.
- Screenshots must come from the user's own system.
- The final DOCX should be easy to copy by hand.
- Support Web, Pwn, Crypto, Forensics, Reverse, OSINT, and Misc.

## Invocation

Typical user request:

> make Pinaka writeup for this solved chat

When invoked in the same conversation that contains the solve, treat the visible conversation as the primary source. Do not ask the user to paste it again.

## Hard rules

1. **Solved-only gate.** Do not generate a write-up pack unless a final flag or equivalent successful completion is present.
2. **User-action gate.** A step may be included only if the conversation shows that the user actually performed it, or the user confirms they performed it.
3. **No invented prose.** Prefer exact or near-exact wording already written by the user. If a necessary step has no user-authored explanation, ask for one short sentence such as: `what did you do here in your own words?` Do not silently invent a first-person account.
4. **No fake screenshots.** Never synthesize, recreate, edit, or cosmetically alter screenshots to make them look authentic. Use genuine captures from the user's own system.
5. **No fake terminal history.** Do not create commands or outputs that did not occur in the solve.
6. **No detector-evasion behavior.** Do not add deliberate typos, random grammar errors, fake hesitations, handwriting simulation, or other artifacts intended to bypass authorship checks.
7. **No over-explaining.** The pack should read like quick personal notes, not a tutorial.
8. **No failed attempts by default.** Keep only the shortest successful path.
9. **Pinaka screenshot rule.** Select 3-6 screenshots, each tied to a key break in the challenge.
10. **Full flag.** Put the exact recovered flag at the end.

## Workflow

### Phase 0 — Human-authoring gate (always first)

Read `references/human-authoring.md` before doing anything else. The participant's own wording controls the voice. Category rules, screenshot planning, and DOCX formatting are secondary and must never overwrite that voice.

### Phase 1 — Extract the successful path

Read the solved conversation from the first useful observation to the flag.

Build an internal table with:

- `step`
- `user_action`
- `tool_or_command`
- `observed_result`
- `user_wording_available` = yes/no
- `screenshot_value` = low/medium/high
- `verified` = yes/no

Ignore assistant suggestions that the user never executed.

Then reduce the timeline to the smallest successful chain. Usually 3-7 steps.

### Phase 2 — Verify missing ownership

If any required step is assistant-only or ambiguous, ask one compact question. Example:

> I can verify `/robots.txt` and the CyberChef decode, but I can't verify that you opened `/backup.zip` yourself. Did you actually do that? If yes, give me one short line in your words.

Do not interrogate the user about already verified steps.

### Phase 3 — Select screenshots

Read `references/screenshot-selection.md` and the matching section in `references/category-evidence.md`.

Pick 3-6 screenshots that prove the actual breakpoints, not every minor command.

A screenshot is useful when it shows one of:

- the hidden clue/endpoint/file;
- the exploit or decisive command;
- the decoder/decompiler/filter/output that changes the direction of the solve;
- the shell/secret/location/key obtained;
- the final flag.

Prefer a short visual chain. Example for Web:

1. `/robots.txt` revealing the hidden path.
2. Hidden resource or response containing the encoded string.
3. CyberChef recipe/output decoding it.
4. Final flag page/output.

If genuine screenshots already exist in the conversation or working directory, use them. If the challenge is still accessible and the current environment can capture screenshots, reproduce only the exact verified steps and capture them. If direct capture is unavailable, emit a screenshot checklist with exact screen state to capture; never substitute a fabricated image.

### Phase 4 — Compose handwriting notes

The prose must be minimal.

Preferred pattern:

- `Checked /robots.txt and found /secret.`
- `Opened it, got this encoded string.`
- `Put it in CyberChef -> Base64 decode.`
- `That gave the flag.`

Use the user's own wording whenever possible. Preserve natural shorthand already used by the user. Do not deliberately introduce mistakes.

Do not write paragraphs unless a category genuinely needs one to explain the exploit.

### Phase 5 — Produce the pack

Create a challenge folder:

```text
<Challenge_Name>/
  notes.json
  screenshots/
    01_<meaningful_name>.png
    02_<meaningful_name>.png
    ...
  <Challenge_Name>_handwriting_sheet.docx
```

Use a small JSON manifest matching `assets/manifest-example.json`.

Generate the DOCX with:

```bash
python scripts/build_reference_docx.py manifest.json <Challenge_Name>_handwriting_sheet.docx
```

The DOCX is a reference sheet for the participant to handwrite. It should contain:

- challenge name;
- category and points if known;
- 3-7 short user-authored/verified steps;
- command snippets only when important;
- screenshot placed directly after the step it proves;
- full flag at the end.

Do not add introduction, conclusion, TL;DR, lessons learned, vulnerability theory, or remediation unless the user asks.

### Phase 6 — Final audit

Before returning the pack, check:

- solved flag exactly matches the conversation;
- no assistant-only step is presented as a user action;
- no failed attempt remains unless requested;
- 3-6 screenshots are selected;
- every screenshot is genuine and from the user's system;
- screenshot order matches the successful path;
- no screenshot contains unrelated private information when avoidable;
- notes are short enough to handwrite without pointless filler;
- Word file opens and images are readable.

## Output style

When reporting completion, keep it terse:

> Done. I kept the successful path only, used 4 screenshots, and put the full flag at the end. The DOCX is a handwriting reference sheet; copy it into your handwritten submission in your own words.
