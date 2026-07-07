"""
tools.py — the agent's card-drawing tool.

This is the simplest possible version: a small tarot deck (major arcana only,
for now) and a function that draws N random cards without replacement.
Later this can grow: add minor arcana, add Lenormand deck, load from a
JSON file instead of a hardcoded list, etc. Start simple, make it work first.
"""

import random
from card_images import get_tarot_image_path, get_lenormand_image_path

# --- Minimal tarot deck: the 22 Major Arcana ---
# (Expand later with Minor Arcana if you have time; Major Arcana alone
# is enough to build and test the whole pipeline.)
TAROT_MAJOR_ARCANA = [
    "The Fool", "The Magician", "The High Priestess", "The Empress",
    "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
    "Strength", "The Hermit", "Wheel of Fortune", "Justice",
    "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World",
]


def draw_card(num_cards: int = 1) -> list[dict]:
    """
    Draw `num_cards` random, non-repeating TAROT cards.
    Each card also gets a random orientation (upright / reversed) —
    a common tarot convention that adds interpretive nuance.

    Use this for inner-state, psychological, "what am I feeling / afraid
    of" type questions.

    Returns a list of dicts, e.g.:
        [{"name": "The Tower", "orientation": "upright"}]
    """
    if num_cards > len(TAROT_MAJOR_ARCANA):
        raise ValueError("Not enough unique cards in the deck for that many draws.")

    drawn_names = random.sample(TAROT_MAJOR_ARCANA, num_cards)
    orientations = [random.choice(["upright", "reversed"]) for _ in range(num_cards)]

    return [
        {"name": name, "orientation": orientation, "image": get_tarot_image_path(name)}
        for name, orientation in zip(drawn_names, orientations)
    ]


# --- Minimal Lenormand deck: the classic 36 cards ---
# Lenormand has no reversed-card convention (unlike tarot) — cards combine
# into a literal "sentence" read together, so no orientation field here.
LENORMAND_DECK = [
    "Rider", "Clover", "Ship", "House", "Tree", "Clouds", "Snake",
    "Coffin", "Bouquet", "Scythe", "Whip", "Birds", "Child", "Fox",
    "Bear", "Stars", "Stork", "Dog", "Tower", "Garden", "Mountain",
    "Crossroads", "Mice", "Heart", "Ring", "Book", "Letter", "Man",
    "Woman", "Lily", "Sun", "Moon", "Key", "Fish", "Anchor", "Cross",
]


def draw_lenormand_card(num_cards: int = 3) -> list[dict]:
    """
    Draw `num_cards` random, non-repeating LENORMAND cards.
    Lenormand cards have no reversed orientation — they combine into a
    literal sentence when read together.

    Use this for concrete, event-driven, "how will this unfold / what
    does this actually mean" type questions — NOT for inner emotional
    states (use draw_card / tarot for that instead).

    Returns a list of dicts, e.g.:
        [{"name": "Ship"}]
    """
    if num_cards > len(LENORMAND_DECK):
        raise ValueError("Not enough unique cards in the deck for that many draws.")

    drawn_names = random.sample(LENORMAND_DECK, num_cards)
    return [{"name": name, "image": get_lenormand_image_path(name)} for name in drawn_names]


# --- Quick manual test: run this file directly to sanity-check the tools ---
if __name__ == "__main__":
    print("Tarot — single card draw:")
    print(draw_card(1))

    print("\nTarot — three-card spread (Past / Present / Future):")
    result = draw_card(3)
    positions = ["Past", "Present", "Future"]
    for position, card in zip(positions, result):
        print(f"  {position}: {card['name']} ({card['orientation']})")

    print("\nLenormand — three-card combination:")
    lenormand_result = draw_lenormand_card(3)
    print("  " + " + ".join(card["name"] for card in lenormand_result))
