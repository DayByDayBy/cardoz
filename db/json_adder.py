import json
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def extract_keywords(text, num_keywords=4):
    tokens = word_tokenize(text)
    words = [
        word.lower()
        for word in tokens
        if word.isalpha() and word.lower() not in stop_words and len(word) > 2
    ]
    freq = Counter(words)
    return [word for word, _ in freq.most_common(num_keywords)]


with open("tdc1.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

for card in cards:
    meaning_text = f"{card.get('meaning_up', '')} {card.get('meaning_rev', '')}"
    keywords = extract_keywords(meaning_text)

    if not keywords:
        print(f"no keywords for {card.get('nameShort', 'unknown')}: {meaning_text}")
    
    card['keywords'] = keywords

with open("rider_waite_with_keywords.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, indent=2, ensure_ascii=False)

print("done")
