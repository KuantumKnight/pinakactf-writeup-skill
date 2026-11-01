# Screenshot selection

PinakaCTF requires 3–6 screenshots per challenge.

## Objective

Choose screenshots that prove the successful path with the fewest images.

A screenshot should answer at least one of these:
- Where was the clue found?
- What decisive value/artifact was discovered?
- What command/tool transformed or exploited it?
- What output proved success?
- Where is the final flag visible?

## Default count

Prefer 3 screenshots for a short challenge, 4 for a normal challenge, and 5–6 only when distinct stages genuinely need evidence.

## Ordering

Put screenshots immediately after the participant-authored sentence they support.

## Screenshot target syntax

When direct capture is unavailable:

`[SS1 — browser showing /robots.txt with the encoded string visible]`

Keep targets specific enough that the participant can reproduce the screenshot on their own machine.

## Genuine-evidence rule

Never:
- fabricate a terminal window,
- regenerate a fake challenge page,
- alter a screenshot to add a flag or command,
- use another participant's screenshot,
- claim a screenshot was captured when only a placeholder exists.

Cropping a genuine participant screenshot for legibility is acceptable only if it does not change its contents.

## Typical minimal chains

### Web
1. decisive endpoint/page
2. discovered token/string/request change
3. decoder/exploit/result showing flag

### Crypto
1. ciphertext/challenge artifact
2. decisive transform/tool/script
3. decoded plaintext/flag

### Pwn
1. binary/service interaction or protection info
2. exploit execution
3. shell/flag output

### Reverse
1. decisive decompiler/disassembly/strings view
2. recovered logic/key or solve script
3. successful output/flag

### Forensics
1. source artifact/file finding
2. extraction/analysis result
3. recovered flag

### OSINT
1. original clue
2. decisive external evidence/location match
3. final answer/flag submission evidence
