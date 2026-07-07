"""
card_images.py — maps card names to image file paths.

Images are NOT included in this repo — you supply your own (see README for
public-domain sourcing suggestions, e.g. the Rider-Waite-Smith tarot deck).
Drop image files into:
    images/tarot/<filename>.jpg
    images/lenormand/<filename>.jpg
using the filenames below. Separate subfolders are required because a few
names collide between the two decks (Sun, Moon, Tower mean different cards
with completely different artwork in each system).

If an image file is missing, get_image_path() still returns the expected
path (frontend should handle a broken-image fallback gracefully — it just
means you haven't dropped that file in yet).
"""

import os

IMAGES_ROOT = os.path.join(os.path.dirname(__file__), "images")

TAROT_IMAGE_FILENAMES = {
    "The Fool": "the_fool.jpg",
    "The Magician": "the_magician.jpg",
    "The High Priestess": "the_high_priestess.jpg",
    "The Empress": "the_empress.jpg",
    "The Emperor": "the_emperor.jpg",
    "The Hierophant": "the_hierophant.jpg",
    "The Lovers": "the_lovers.jpg",
    "The Chariot": "the_chariot.jpg",
    "Strength": "strength.jpg",
    "The Hermit": "the_hermit.jpg",
    "Wheel of Fortune": "wheel_of_fortune.jpg",
    "Justice": "justice.jpg",
    "The Hanged Man": "the_hanged_man.jpg",
    "Death": "death.jpg",
    "Temperance": "temperance.jpg",
    "The Devil": "the_devil.jpg",
    "The Tower": "the_tower.jpg",
    "The Star": "the_star.jpg",
    "The Moon": "the_moon.jpg",
    "The Sun": "the_sun.jpg",
    "Judgement": "judgement.jpg",
    "The World": "the_world.jpg",
}

LENORMAND_IMAGE_FILENAMES = {
    "Rider": "rider.svg",
    "Clover": "clover.svg",
    "Ship": "ship.svg",
    "House": "house.svg",
    "Tree": "tree.svg",
    "Clouds": "clouds.svg",
    "Snake": "snake.svg",
    "Coffin": "coffin.svg",
    "Bouquet": "bouquet.svg",
    "Scythe": "scythe.svg",
    "Whip": "whip.svg",
    "Birds": "birds.svg",
    "Child": "child.svg",
    "Fox": "fox.svg",
    "Bear": "bear.svg",
    "Stars": "stars.svg",
    "Stork": "stork.svg",
    "Dog": "dog.svg",
    "Tower": "tower.svg",
    "Garden": "garden.svg",
    "Mountain": "mountain.svg",
    "Crossroads": "crossroads.svg",
    "Mice": "mice.svg",
    "Heart": "heart.svg",
    "Ring": "ring.svg",
    "Book": "book.svg",
    "Letter": "letter.svg",
    "Man": "man.svg",
    "Woman": "woman.svg",
    "Lily": "lily.svg",
    "Sun": "sun.svg",
    "Moon": "moon.svg",
    "Key": "key.svg",
    "Fish": "fish.svg",
    "Anchor": "anchor.svg",
    "Cross": "cross.svg",
}


def get_tarot_image_path(card_name: str) -> str:
    """Returns the relative image path for a tarot card, e.g. 'images/tarot/the_tower.jpg'."""
    filename = TAROT_IMAGE_FILENAMES.get(card_name)
    if filename is None:
        return ""
    return f"images/tarot/{filename}"


def get_lenormand_image_path(card_name: str) -> str:
    """Returns the relative image path for a lenormand card, e.g. 'images/lenormand/ship.jpg'."""
    filename = LENORMAND_IMAGE_FILENAMES.get(card_name)
    if filename is None:
        return ""
    return f"images/lenormand/{filename}"


# --- Quick manual test ---
if __name__ == "__main__":
    print("Tarot image path for 'The Tower':", get_tarot_image_path("The Tower"))
    print("Lenormand image path for 'Tower':", get_lenormand_image_path("Tower"))
    print("(different paths for the collision case — confirms no overlap)")
