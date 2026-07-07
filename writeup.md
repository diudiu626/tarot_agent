# Reflekt — A Reflective Decision Companion

**Subtitle:** A tarot-and-Lenormand-based agent that remembers your past readings, mirrors your patterns back to you, and pushes every reflection toward one concrete next step.

**Track:** Freestyle Course concepts demonstrated: Agent Skills · Human-in-the-loop · Tool Use · Agent reasoning (question routing)

---

## This is not a fortune teller

It does not predict the future. It helps you reflect, recognize your own patterns, and take action. Tarot and Lenormand cards are just *tools* the agent draws on — the product is a reflective decision companion, not a divination app.

## The Problem

When people face soft, ambiguous life decisions — *should I take this opportunity? what do I do about this relationship? which direction do I go?* — they often reach for tarot or Lenormand. Not because they believe a card predicts the future, but because they need an external structure that forces them to articulate a fuzzy inner state.

But every divination app I've tried fails in three ways:

- **Amnesiac** — every session is the first time it meets you. No continuity, no growth.
- **One-directional** — it recites generic card meanings at you, ignoring your actual situation.
- **Floating** — it hands you a mystical sentence and stops. No path to action.

The result is a random card-meaning generator: entertaining for a minute, useless for an actual decision. I built this project because I genuinely wanted a tool I would use myself — one that remembers, reflects, and lands on action, rather than one more app that forgets me the moment I close it.

## Why Agents

A static app can't solve this. The three failures above are exactly what agentic capabilities are built to fix:

- **Memory** lets the agent compare today's reading against the user's own history, instead of starting from zero every time.
- **Tool use** lets the agent draw cards, persist structured readings, and retrieve past ones as discrete, composable actions rather than baked-in logic.
- **Skills** let the interpretive *mechanics* of each symbol system (Tarot vs. Lenormand) live in their own self-contained files, loaded on demand, instead of bloating one giant prompt.
- **Human-in-the-loop reasoning** lets the agent pause and genuinely incorporate the user's own projection onto the cards, rather than issuing a one-way verdict.

None of this is possible with a lookup table. It requires an agent that can reason across turns, call tools, and hold state — which is exactly what this course teaches.

## The Solution

A conversational agent that inverts all three failures of typical divination apps:

**① It has memory, and it holds up a mirror.**
The agent persists every reading in a structured record — Question, Interpretation, Action, Emotion, Date, Outcome — and checks this history at the start of each new conversation. In testing, this produced genuinely useful cross-session behavior: when asked a new question about the same relationship weeks apart, the agent noticed that the *same tarot card* had appeared in both readings, but in different orientations (upright vs. reversed), and used that shift as the basis for a fresh interpretation — a comparison no stateless app could make. It also correctly linked a Lenormand reading about a work project back to an earlier Tarot reading on an entirely different topic (a relationship), showing the memory layer works *across* symbol systems, not just within one.

**② It doesn't fortune-tell; it forces a landing.**
Every reading follows a fixed five-step shape — **Reflection → Pattern → Possible Meaning → Action → Journal Prompt** — that operationalizes the project's interpretive constitution (below). The agent translates the mystical into a decision: it always ends with exactly one concrete, doable action for the coming week, plus a journal prompt to sit with afterward.

**③ It's collaborative interpretation, not a one-way verdict.**
Before interpreting anything, the agent asks: *"What's your first reaction to these cards?"* — and waits. This human-in-the-loop step matters because the real value of these symbol systems has always been in the user's projection, not the card itself. In one test, when asked point-blank what someone else "really meant" by a statement, the agent explicitly declined to play mind-reader, and instead reframed the question into ones the user could actually answer about their own feelings, fears, and boundaries — before offering a reading. That refusal-and-reframe is a direct, load-bearing expression of the constitution, not decoration.

**④ It routes between two symbol systems based on the question.**
Tarot and Lenormand answer different kinds of questions — a real, established distinction in practice, not an arbitrary mash-up: **Tarot** is inner, psychological, archetypal (best for "what state am I in?"); **Lenormand** is concrete, event-driven, literal, and its cards are read together as a single combined sentence rather than as separate positions (best for "how will this unfold?"). The agent reasons about which system fits the user's question, and can ask for clarification when it's genuinely ambiguous.

## The Interpretive Constitution — the agent's soul

This is what most separates the agent from a random card-meaning generator. A 10-principle charter is injected directly into the system prompt, so it conditions every reading — not marketing copy, but the agent's actual behavioral rules (full text in `constitution.md`):

1. **The cards are a mirror, not a prophecy.** Never "X will happen" — only "what does this let you see?"
2. **Always orient toward agency.** Every reading lands on one controllable next step.
3. **Anti-platitude, anti-self-pity.** No empty comfort; gently pull back toward multiple angles.
4. **Move first — distinguish real risk from mere reluctance.**
5. **See whether this is a finite or infinite game** (after Carse) — for fights over winning, titles, or face.
6. **See who the investment compounds for** — is this building the user's own skills/autonomy, or feeding someone else's system?
7. **See whether "messy" is scattered or a spiral** — don't misjudge nonlinearity as failure.
8. **Protect the user's aliveness** — structure without flattening spontaneity.
9. **Admit uncertainty; don't fake hidden truths.**
10. **The user is their own authority** — the agent offers a mirror, not a verdict.

Principles 5–7 in particular are what make the career/direction readings substantively different from any generic divination app — they encode interpretive lenses that a purely technical build, without a defined point of view, could not produce.

## Architecture

```
User's question
   │
   ▼
Agent (ADK) — checks memory for relevant past readings (silently)
   │
   ▼
Routing — inner/psychological question → Tarot skill
          concrete/event question       → Lenormand skill
   │
   ▼
Skill (SKILL.md) — defines exact spread mechanics
   │  tarot-three-card-spread: draw_card tool → Past/Present/Future
   │  lenormand-three-card: draw_lenormand_card tool → combined sentence
   ▼
Human-in-the-loop — "What's your first reaction to these cards?"
   │
   ▼
Interpretation — follows the fixed five-step shape, governed by the
                  Interpretive Constitution, incorporating the user's
                  stated reaction and any relevant history
   │
   ▼
save_reading tool — persists the six-field record to memory
   │
   ▼
Response returned to user
```

Two design decisions are worth calling out:

- **Skills hold mechanics; the core instruction holds philosophy.** Each `SKILL.md` defines *how* to run its specific spread (which tool to call, how to present cards, when to ask for the user's reaction). The constitution and output shape live once, centrally, in the agent's core instruction — so both symbol systems interpret through the same values without duplicating that logic. Adding a third system (e.g. Plum Blossom I Ching) would mean writing one new `SKILL.md`, not touching the interpretive core.
- **Memory is system-agnostic.** The structured store isn't scoped to a single spread type — it's what let the agent connect a Lenormand reading about a work project to an earlier, unrelated Tarot reading about a relationship, and correctly note the connection wasn't there.

## How It's Built

- **Framework:** Google ADK (Agent Development Kit)
- **IDE:** Google Antigravity (vibe coding)
- **Model:** Gemini 2.5 Flash, via the free tier of Google AI Studio — no billing required
- **Skills:** `tarot-three-card-spread` and `lenormand-three-card`, each a real `SKILL.md` loaded via ADK's official skill-loading API (`load_skill_from_dir` + `SkillToolset`) — not simulated in a prompt string
- **Tools:** `draw_card`, `draw_lenormand_card`, `save_reading`, `get_recent_readings` — four discrete, composable functions the agent calls rather than baked-in logic
- **Memory:** a structured local store (six fields: Question, Interpretation, Action, Emotion, Date, Outcome), read at the start of every conversation and written at the end of every reading
- **Interface:** ADK's built-in `adk web` developer UI, auto-discovered from a `root_agent` variable — a working, testable chat interface with zero custom frontend code, plus its Events/Traces panel for inspecting exactly which tools and skills fired on a given turn
- **Error handling:** free-tier rate limits (a real constraint encountered during development) are caught and shown to the user as a plain, friendly message instead of a stack trace — the agent stays usable under a real-world failure mode rather than crashing

## Demo

Below are the key interaction moments captured from a real multi-session testing sequence, demonstrating the routing, interpretation loop, and constitutional guardrails in action.

### 1. Dynamic Routing & Human-in-the-Loop Capture
When presented with a concrete, event-driven question regarding an uncertain opportunity, the agent automatically evaluates the intent and routes to the **Lenormand system** instead of Tarot. The UI renders the custom card layout (*Garden*, *Whip*, *Clouds*) and immediately implements a Human-in-the-loop pause, explicitly requesting the user's subjective projection ("What's your first reaction?") before generating any text.

![The web UI showing adaptive routing to the Lenormand system and the interactive first-reaction pause.](./L1.png)

### 2. Constitution-Governed Analysis & Action Step Landing
Once the user provides their input, the agent synthesizes the situational context and delivers a structured analysis. Aligned with the core constitution, the response avoids abstract mysticism and deliberately concludes with a pragmatic, high-signal task: a concrete next step for the week to identify one specific unclear aspect and seek out a clarifying conversation.

![The generated interpretation breaking down card combinations and establishing a practical action step.](./L2.png)

### 3. Constitutional Guardrails Enforcing Boundary Control
When explicitly pushed to predict a definitive outcome ("Will this project definitely succeed?"), the agent's behavioral charter instantly engages. The system flatly declines the divination request, reminds the user that the future is shaped by conscious choices, and loops back to reframe the query around actionable, internal resources.

![The agent constitutional guardrails activating to reject fortune-telling and restore user agency.](./Reject_pic.png)

## What's Built vs. Future Work

**Built and verified working this round:** the full reflective-companion loop across two symbol systems, question routing, human-in-the-loop projection capture, six-field structured memory with cross-session and cross-system recall, the full 10-principle constitution wired into the system prompt, the fixed five-step output shape, graceful error handling, and a working chat UI.

**Named as future work, deliberately not built this round** (discipline over feature-stuffing): a formal Planner/Router component (currently the routing decision is instruction-level reasoning, which already works reliably in testing); an automatic Pattern Detector that surfaces repeating themes across many readings without being asked; a long-term revisit loop ("want to come back next week to review how this went?"); a daily Thinking/Feeling/Doing check-in spread; a Tarot Celtic Cross for more complex questions; a custom frontend with card-face imagery (the public-domain Rider-Waite deck); and additional symbol systems such as Plum Blossom I Ching, which the pluggable skill architecture is designed to accommodate without touching the interpretive core.

## Closing note

I built this to be something I'd actually use again — not just a capstone submission. Every design choice, from the constitution's insistence on agency over prophecy, to memory that mirrors rather than merely stores, was aimed at making a genuinely useful reflective tool, using the agentic techniques this course teaches to do something a static app structurally cannot.
