import card_straightener


def main(deck):
    processed_deck = [card_straightener.straighten_and_crop(n) for n in deck]
    return processed_deck
