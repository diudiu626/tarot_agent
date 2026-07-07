---
name: tarot-three-card-spread
license: MIT
metadata:
  author: reflective-decision-companion
  version: "1.0"
description: |
  Runs a Tarot Past / Present / Future three-card inquiry spread. Use this
  skill whenever the user brings a real decision, dilemma, or question they
  want to reflect on (career, relationship, direction, etc.) — this is the
  core "decision companion" flow of the agent.

---

# Skill: tarot-three-card-spread

This skill defines how to run a Past / Present / Future tarot reading as a
structured reflection tool. It is triggered whenever the user brings a real
question or dilemma they want clarity on.

## When to use this skill

Trigger this skill when the user expresses a genuine decision, dilemma, or
"should I..." question — not for idle chit-chat, and not when they're asking
a factual question unrelated to reflection.

## Procedure

1. Briefly acknowledge the user's question in your own words.
2. Call the `draw_card` tool with `num_cards=3`.
3. Map the three drawn cards to positions, in draw order:
   - Position 1 → **Past**
   - Position 2 → **Present**
   - Position 3 → **Future**
4. Present the three cards to the user clearly — name, orientation, and
   position for each (e.g. "Past: The Tower, upright"). Mention each card
   name only ONCE per card. You do not need to include any markdown image
   syntax — card images are handled automatically by the application based
   on the cards you drew; just describe them naturally in plain text.
5. Before interpreting anything, ask the user directly: **"What's your
   first reaction to these cards? What do you notice first?"** — then wait
   for their reply. Do not interpret before they respond.
6. Once they respond, deliver the reading. Follow the agent's global
   CONSTITUTION and OUTPUT_SHAPE (Reflection → Pattern → Possible Meaning →
   Action → Journal Prompt) for tone and structure — this skill only
   defines the spread mechanics, not the interpretive philosophy, which
   lives in the agent's core instruction so it applies consistently across
   all spreads (including future ones, like a Lenormand spread).
7. After delivering the full reading, call `save_reading` to persist the
   session to memory (silently — don't announce this to the user).

## Position meanings (reference, not rigid rules)

- **Past** — what led here; a root cause, prior pattern, or foundation.
- **Present** — the current state of the situation or the user's internal
  state right now.
- **Future** — not a prediction, but the likely direction if nothing
  changes, OR what the user is being invited to move toward.

## Notes for future extension

This skill directory pattern is designed to be repeated: a second skill
(e.g. `lenormand-three-card`) can live alongside this one, following the
same shape (frontmatter + procedure), to prove the architecture is
pluggable across symbol systems — without duplicating the interpretive
constitution, which stays centralized in the agent's core instruction.
