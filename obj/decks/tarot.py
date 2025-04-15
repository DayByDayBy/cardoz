from obj.card import Card
from obj.deck import Deck

def get_tarot_deck():
    cards = []
    
    # Major Arcana
    major_names = [
        "The Fool", "The Magician", "The High Priestess", "The Empress", 
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot", 
        "Strength", "The Hermit", "Wheel of Fortune", "Justice", 
        "The Hanged Man", "Death", "Temperance", "The Devil", 
        "The Tower", "The Star", "The Moon", "The Sun", 
        "Judgement", "The World"
    ]
    for i, name in enumerate(major_names):
        cards.append(Card(name=name, suit="Major Arcana", rank=str(i), value=i, ordering=i))

    # Minor Arcana example
    suits = ["Wands", "Cups", "Swords", "Pentacles"]
    ranks = [("A", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5), 
             ("6", 6), ("7", 7), ("8", 8), ("9", 9), ("10", 10), 
             ("Page", 11), ("Knight", 12), ("Queen", 13), ("King", 14)]

    ordering_offset = len(major_names)
    for suit in suits:
        for idx, (rank, value) in enumerate(ranks):
            name = f"{rank} of {suit}"
            ordering = ordering_offset + idx + (suits.index(suit) * len(ranks))
            cards.append(Card(name=name, suit=suit, rank=rank, value=value, ordering=ordering))
    
    return Deck(cards)
