import random
from typing import Dict, Any
from sqlalchemy.orm import Session
from . import crud
from .spreads import CelticCrossSpread

def create_celtic_cross_reading(db: Session) -> Dict[str, Any]:
    """generate a complete Celtic Cross reading"""
    spread = CelticCrossSpread()
    positions = spread.get_positions()

    drawn_cards = crud.get_random_cards(db, 10)

    card_orientations = [random.choice([False, True]) for _ in range(10)]

    # the reading:

    reading = {
        "spread_name": "Celtic Cross",
        "cards": []
    }

    for i, (card, is_reversed) in enumerate(zip(drawn_cards, card_orientations)):
        position = positions[i]
        meaning = card.meaning_rev if is_reversed else card.meaning_up

        reading["cards"].append({
            "position": position.name,
            "position_desc": position.description,
            "card": card.name,
            "short_name": card.name_short,  # for image reference
            "reversed": is_reversed,
            "meaning": meaning,
            "x_pos": position.x_pos,
            "y_pos": position.y_pos
        })

    return reading