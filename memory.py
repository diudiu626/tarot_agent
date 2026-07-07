"""
memory.py — structured, persistent memory for past readings.

Storage format: a local JSON file (readings.json) holding a list of
records. Each record follows the six-field schema from the project design:

    Question | Interpretation | Action | Emotion | Date | Outcome

This is intentionally the simplest possible persistence — a JSON file,
not a database or MCP server. It's easy to upgrade to MCP later if there's
time; getting the "agent remembers" mechanic working end-to-end matters
more right now than which storage backend it uses.
"""

import json
import os
from datetime import date as _date

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "readings.json")


def _load_all() -> list[dict]:
    """Load all saved readings. Returns an empty list if none exist yet."""
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # File exists but is empty/corrupted — treat as no history.
            return []


def _save_all(readings: list[dict]) -> None:
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(readings, f, indent=2, ensure_ascii=False)


def save_reading(
    question: str,
    cards: str,
    user_reaction: str,
    interpretation: str,
    action: str,
    emotion: str,
) -> dict:
    """
    TOOL: Save a completed reading to long-term memory.

    Call this ONCE, after you have finished delivering the full reading and
    the concrete next-step action to the user — this is what lets you act
    as a mirror in future sessions.

    Args:
        question: The user's original question or dilemma, in their words.
        cards: The cards drawn and their positions, e.g.
            "Past: Strength (upright); Present: The Lovers (upright); Future: Justice (upright)".
        user_reaction: The user's stated first reaction to the cards.
        interpretation: A short (2-3 sentence) summary of the reading you gave.
        action: The single concrete next step you gave the user.
        emotion: The emotional tone you picked up from the user during this
            conversation (e.g. "hopeful", "anxious", "curious", "avoidant").

    Returns:
        A dict confirming what was saved.
    """
    readings = _load_all()
    record = {
        "date": _date.today().isoformat(),
        "question": question,
        "cards": cards,
        "user_reaction": user_reaction,
        "interpretation": interpretation,
        "action": action,
        "emotion": emotion,
        "outcome": None,  # filled in later, if the user revisits this reading
    }
    readings.append(record)
    _save_all(readings)
    return {"status": "saved", "record": record}


def get_recent_readings(limit: int = 5) -> list[dict]:
    """
    TOOL: Retrieve the user's most recent past readings, most recent first.

    Call this at the START of a conversation (or when relevant) so you can
    check whether the user has asked something similar before, and act as
    a mirror — e.g. "you drew a similar card for a similar question last
    month; back then you said X."

    Args:
        limit: Max number of past readings to return. Defaults to 5.

    Returns:
        A list of past reading records (possibly empty, if this is the
        user's first time).
    """
    readings = _load_all()
    return readings[-limit:][::-1]  # most recent first


# --- Quick manual test ---
if __name__ == "__main__":
    print("Before saving, recent readings:", get_recent_readings())

    result = save_reading(
        question="Will I win the lottery next time?",
        cards="Past: Strength (upright); Present: The Lovers (upright); Future: Justice (upright)",
        user_reaction="they are all upright which means it could be good signs?",
        interpretation="The cards point to inner resilience, a values-based choice, and future consequences tied to present decisions — not a lottery prediction, but an invitation to reflect on what you're really seeking.",
        action="Spend 15 minutes listing what 'winning the lottery' really represents for you beyond the money.",
        emotion="hopeful",
    )
    print("\nSaved:", result)

    print("\nAfter saving, recent readings:", get_recent_readings())
