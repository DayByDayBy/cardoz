import json

# Example deck loader (assumes preprocessed dict with shortcodes as keys)
def load_deck(path="./deck.json"):
    with open(path, "r") as f:
        return json.load(f)  # {"waac": {...}, "ar02": {...}}

# Get a single card by code
def get_card_by_code(code, deck_lookup):
    return deck_lookup.get(code)

# Expand shortcodes into full card metadata
def expand_reading(reading, deck_lookup):
    return {
        **reading,
        "cards": [get_card_by_code(code, deck_lookup) for code in reading["draw"]]
    }

# Optional parser for shortcodes with embedded reversal info
def parse_code_with_meta(code_str):
    if ":" in code_str:
        code, flag = code_str.split(":")
        return code, flag == "r"
    return code_str, False

# Expand codes with meta (reversal, position)
def expand_reading_with_meta(reading, deck_lookup):
    cards = []
    for i, code_str in enumerate(reading["draw"]):
        code, is_reversed = parse_code_with_meta(code_str)
        card = get_card_by_code(code, deck_lookup)
        card = {**card, "is_reversed": is_reversed, "position": i}
        cards.append(card)
    return {**reading, "cards": cards}