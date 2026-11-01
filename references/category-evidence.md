# Category evidence heuristics

These rules choose what to show. They do not author the participant's narrative.

## Web

Prioritize decisive application-state evidence:
- unusual routes such as `/robots.txt`, `/sitemap.xml`, hidden endpoints,
- source/JS clue,
- request/response mutation,
- cookie/header/token change,
- CyberChef or other transform if it was actually used,
- response containing the flag.

Avoid screenshots of generic homepage reconnaissance unless it mattered.

## Crypto

Prioritize:
- exact ciphertext/input,
- property that led to the successful transform if participant documented it,
- CyberChef/solver/script with parameters visible,
- final plaintext and flag.

Do not add cryptographic theory that the participant did not use.

## Pwn

Prioritize:
- service/binary target,
- checksec or equivalent only if it affected the exploit,
- payload/exploit execution,
- shell or direct flag output.

Do not include every debugging breakpoint.

## Reverse Engineering

Prioritize:
- exact function/string/control-flow clue that unlocked the solve,
- recovered constant/key/algorithm,
- solve script or patched execution if used,
- flag output.

Avoid unrelated decompiler views.

## Forensics

Prioritize:
- original artifact,
- decisive metadata/string/carving/packet/file discovery,
- extraction/decode action,
- recovered flag.

## OSINT

Prioritize:
- original image/text clue,
- decisive corroborating source/map/street-view evidence,
- exact location/name/coordinates used for the answer,
- accepted flag/result if available.

A screenshot should show the evidence, not merely a search-results page, when possible.

## Misc

Use the generic chain:
- clue,
- decisive manipulation/discovery,
- proof/flag.
