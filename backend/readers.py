
import random
from typing import List, Dict, Any, Tuple
from .models import TarotCard
from .spreads import CelticCrossSpread

def draw_cards(deck: List[TarotCard], count: int) -> List[TarotCard]:
    """draw a specific number of cards from the deck without replacement"""
    # creatin a copy of the deck to avoid modifying the original
    deck_copy = deck.copy()
    random.shuffle(deck_copy)
    return deck_copy[:count]

def create_celtic_cross_reading(deck: List[TarotCard]) -> Dict[str, Any]:
    """generate a complete Celtic Cross reading"""
    spread = CelticCrossSpread()
    positions = spread.get_positions()
    
  
    drawn_cards = draw_cards(deck, 10)
    
    card_orientations = [random.choice([False, True]) for _ in range(10)]
    
    # the reading:
    
    reading = {
        "spread_name": "Celtic Cross",
        "cards": []
    }
    
    for i, (card, is_reversed) in enumerate(zip(drawn_cards, card_orientations)):
        position = positions[i]
        meaning = card['meaningRev'] if is_reversed else card['meaningUp']
        
        reading["cards"].append({
            "position": position.name,
            "position_desc": position.description,
            "card": card["name"],
            "short_name": card["nameShort"],  # for image reference
            "reversed": is_reversed,
            "meaning": meaning,
            "x_pos": position.x_pos,
            "y_pos": position.y_pos
        })
    
    return reading
