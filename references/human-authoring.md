# Human-authoring gate

This is the primary module of the PinakaCTF write-up skill.

## Purpose

The reference sheet must be built from the participant's own account of what they did. The agent may organize, quote, and lightly normalize the material, but it must not substitute its own challenge narrative.

## Source priority

Use wording in this order:

1. Participant sentence that directly describes the action.
2. Participant sentence that describes the observation/result.
3. Participant command plus participant-provided output, with a short structural label only.
4. A new one-line answer requested from the participant.

Never use assistant prose as if it were the participant's wording.

## What counts as participant-authored

Good sources include messages such as:

- `found this in robots.txt`
- `then i put it in cyberchef`
- `this gave the flag`
- `strings showed this weird key`
- `i changed the cookie and refreshed`

Keep the user's vocabulary. Do not expand these into textbook explanations.

## Structural text the agent may add

The agent may add neutral labels that are not part of the submission narrative, for example:

- `Step 1`
- `Screenshot 2`
- `Command`
- `Flag`
- `Web`
- `Challenge: ...`

These labels must not introduce new claims about the solve.

## Missing-step drill

Ask only when a necessary link is absent.

Good question:

`What did you do with that encoded string? Answer exactly how you'd write it by hand, one line.`

Bad question:

`Did you recognize it as Base64 and decode it in CyberChef?`

The bad version plants wording and reasoning.

## Editing level

Default: preserve wording.

Do not:
- change simple wording into formal security jargon,
- add words such as "therefore", "subsequently", "upon inspection", or "leveraging",
- add artificial slang,
- insert intentional spelling mistakes,
- create fake pauses or uncertainty,
- imitate a specific person's handwriting or prose style,
- tune against an AI detector.

If the participant explicitly asks for spelling cleanup, correct spelling without changing sentence structure more than necessary.

## Concision

Prefer the shortest participant-authored sentence that carries the step.

If the participant wrote ten messages while solving the same action, select the one or two that best state the successful action and result. Do not preserve chat noise just for realism.

## Example transformation

Conversation evidence:

Participant: `i checked robots.txt and there is this weird encoded line`
Participant later: `used cyberchef from base64 and got the flag`

Reference-sheet wording:

- `I checked robots.txt and there is this weird encoded line.`
- `Used CyberChef From Base64 and got the flag.`

Only obvious tool capitalization may be normalized. The agent should not rewrite this as a polished vulnerability explanation.
