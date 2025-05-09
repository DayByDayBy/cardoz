
from obj.decks.tarot.tarot_deck import tarot_deck as original_deck

updated_deck = [{**card, 'deck_index': i} for i, card in enumerate(original_deck)]


print("tarot_deck = [")
for card in updated_deck:
    print(f"    {card},")
print("]")