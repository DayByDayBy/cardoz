
from obj.decks.tarot.tarot_deck import tarot_deck as original_deck

updated_deck = [{**card, 'deck_index': i} for i, card in enumerate(original_deck)]


print("tarot_deck = [")
for card in updated_deck:
    print(f"    {card},")
print("]")


#  this will add the idx to the dict/json thing

# tested it just to be sure, and it works as expected. might 
# build a couple more tools to shape it before i save 
# it/replace it with a final/to be used version. 
# tools or not it will need edited

# atm i think i want:  

# type,
# suit,
# value,
# nameShort,
# name,
# position,
# meaningUp,
# meaningRev,
# description

# and atm i think a spread_card object, sth like:

    # {
    # "type": "major",
    # "suit": None,
    # "value": None,
    # "nameShort": "ar01",
    # "name": "The Magician",
    # "position": 1,
    # "rev": False;
    # "meaning": "Skill, diplomacy, address, subtlety; sickness, pain, loss, disaster, snares of enemies; self-confidence, will; the Querent, if male.",
    # }

# those values can all be derived from the main object except rev, 
# which will be a product of the drawing of the card
# 
# for each card in spread:
#   type, etc = type, etc 
#   rev  = random.choice(True, False)
#   meaning = meainingRev if rev, else meaningUp