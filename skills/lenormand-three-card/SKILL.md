---
name: lenormand-three-card
license: MIT
metadata:
  author: reflective-decision-companion
  version: "1.0"
description: |
  Runs a Lenormand three-card combination reading, read together as a
  literal "sentence" rather than three separate positions. Use this skill
  when the user's question is concrete and event-driven — "how will this
  unfold," "what does this situation actually mean," "what's likely to
  happen with X" — as opposed to inner emotional/psychological questions
  (use tarot-three-card-spread for those instead).

---

# Skill: lenormand-three-card

This skill defines how to run a Lenormand three-card reading. Unlike tarot,
Lenormand cards are read TOGETHER as a combined sentence, not as separate
positions (no Past/Present/Future mapping, and no reversed orientation).

## When to use this skill (vs. the tarot skill)

Lenormand and tarot answer different kinds of questions:

- **Use tarot-three-card-spread** for inner, psychological, archetypal
  questions — "what am I feeling," "what am I afraid of," "what do I need
  to understand about myself."
- **Use lenormand-three-card** for concrete, event-driven, literal
  questions — "how will this unfold," "what does this actually mean,"
  "what's the situation with X really."

If the user's question is ambiguous, you may briefly ask which kind of
clarity they're looking for (inner reflection vs. a read on the concrete
situation) before choosing a skill — but don't force this if the question
is already clearly one or the other.

## Procedure

1. Briefly acknowledge the user's question in your own words.
2. Call the `draw_lenormand_card` tool with `num_cards=3`.
3. Present the three cards to the user in draw order, as a set — do NOT
   assign them Past/Present/Future positions (that's a tarot convention,
   not a Lenormand one). Mention each card name only ONCE per card. You do
   not need to include any markdown image syntax — card images are handled
   automatically by the application based on the cards you drew; just
   name them naturally in plain text.
4. Before interpreting anything, ask the user directly: **"What's your
   first reaction to these three cards together? What do you notice
   first?"** — then wait for their reply. Do not interpret before they
   respond.
5. Once they respond, deliver the reading by reading the three cards
   TOGETHER as a combined sentence (this is the classic Lenormand method —
   e.g. Ship + Heart + Anchor might read as "a journey toward a
   love that becomes stable/secure"). Follow the agent's global
   CONSTITUTION and OUTPUT_SHAPE (Reflection → Pattern → Possible Meaning
   → Action → Journal Prompt) for tone and structure — this skill only
   defines the spread mechanics, not the interpretive philosophy, which
   lives in the agent's core instruction so it applies consistently across
   all spreads.
6. After delivering the full reading, call `save_reading` to persist the
   session to memory (silently — don't announce this to the user). In the
   `cards` field, note it's a Lenormand reading, e.g. "Lenormand: Ship +
   Heart + Anchor (combined)".

## Why this skill exists (architecture note)

This skill exists alongside `tarot-three-card-spread` to prove the
agent's architecture holds more than one symbol system as a pluggable
skill, without duplicating the interpretive constitution — which stays
centralized in the agent's core instruction and applies to every skill
equally.
