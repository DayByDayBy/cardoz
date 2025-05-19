import requests
import os

BASE_URL = "https://steve-p.org/cards/pix/"
OUTPUT_DIR = "downloaded_tarot_cards_03"
os.makedirs(OUTPUT_DIR, exist_ok=True)

suits = {
    "T": [f"{i:02d}" for i in range(0, 22)],  
    "P": ["0A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "PG", "KN", "QU", "KI"],
    "C": ["0A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "PG", "KN", "QU", "KI"],
    "S": ["0A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "PG", "KN", "QU", "KI"],
    "W": ["0A", "02", "03", "04", "05", "06", "07", "08", "09", "10", "PG", "KN", "QU", "KI"],
}

def download_card(filename):
    url = f"{BASE_URL}{filename}"
    filepath = os.path.join(OUTPUT_DIR, filename)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filepath, "wb") as f:
                f.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Skipped (not found): {filename}")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

# constructiing filenames
for suit, ranks in suits.items():
    for rank in ranks:
        fname = f"RWSa-{suit}-{rank}.png"
        download_card(fname)

print("done")
