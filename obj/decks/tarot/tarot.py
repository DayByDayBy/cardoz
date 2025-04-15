import json

with open("./tarot.json", "r", encoding="utf-8") as f:
    raw_cards = json.load(f)

class TarotCard:
    def __init__(self, data):
        self.name = data.get("name")
        self.suit = data.get("suit")
        self.type = data.get("type")
        self.meaning_up = data.get("meaningUp")
        self.meaning_rev = data.get("meaningRev")
        self.description = data.get("description")
        self.value = data.get("value")
        self.int_value = data.get("intValue")
        self.name_short = data.get("nameShort")

    def get_meaning(self, reversed=False):
        return self.meaning_rev if reversed else self.meaning_up

deck = [TarotCard(data) for data in raw_cards]