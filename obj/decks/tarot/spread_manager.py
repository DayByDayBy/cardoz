import random 
import tarot_deck
from .....cards_.machina import selectors


deck = tarot_deck

def celtic_cross(deck):
    drawn_cards = selectors.draw_10(deck)
    spread = [(card, random.choice([False, True])) for card in drawn_cards]
    return spread


def assign(spread):
    for n in spread:
        short_name = spread[n][0]['nameShort']
        name = spread[n][0]['name']
        position = spread[n][0]['position']
        if spread[n][1]:
            meaning = spread[n][0]['meaningRev']
        else:
            meaning = spread[n][0]['meaningUp']
        