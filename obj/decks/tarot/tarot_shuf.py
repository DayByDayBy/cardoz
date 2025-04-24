from .....cards_.machina import shuffles

import tarot_deck

deck = tarot_deck


def main(deck):
    shuf_deck=deck
    shuf_deck = shuffles.game_clean(deck)
    return shuf_deck
    
if __name__ == "__main__":
    main(deck)
    