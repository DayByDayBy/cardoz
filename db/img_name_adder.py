
import json

with open("rider_waite_with_keywords.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for card in cards:
    card['image_url'] = f"{card['short_name']}.jpg"

with open("rider_waite_with_keywords.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

