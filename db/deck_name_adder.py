
import json

# def extract_keywords(text, num_keywords=4):
#     tokens = word_tokenize(text)
#     words = [
#         word.lower()
#         for word in tokens
#         if word.isalpha() and word.lower() not in stop_words and len(word) > 2
#     ]
#     freq = Counter(words)
#     return [word for word, _ in freq.most_common(num_keywords)]

with open("rider_waite_with_keywords.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for card in cards:
    card['deck_id'] = "rider_waite_classic"

with open("rider_waite_with_keywords.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

