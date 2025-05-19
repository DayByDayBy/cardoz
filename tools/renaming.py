import os
import re

#  single letter suit to double letter
suit_map = {
    "W": "wa",
    "S": "sw",
    "C": "cu",
    "P": "pe",
    "T": "ar",  # they say trumps, i say major arcana
}

#  mapping to my schema
rank_map = {
    "KI": "ki",
    "QU": "qu",
    "KN": "kn",
    "PG": "pg",
    "0A": "ac",
    "02": "02",
    "03": "03",
    "04": "04",
    "05": "05",
    "06": "06",
    "07": "07",
    "08": "08",
    "09": "09",
    "10": "10",
}

def rename_tarot_images(directory):
    for filename in os.listdir(directory):
        if not filename.lower().endswith(".png"):
            continue

        match = re.match(r"RWSa-([A-Z])-([0A-Z0-9]{2})\.png", filename)
        if not match:
            print(f"unrecognized file: {filename}")
            continue

        suit_letter, rank = match.groups()

        if suit_letter == "T":
            # maj arcana
            new_name = f"ar{rank}.png"
        else:
            suit_prefix = suit_map.get(suit_letter)
            rank_suffix = rank_map.get(rank)
            if not suit_prefix or not rank_suffix:
                print(f"Skipping unknown card mapping: {filename}")
                continue
            new_name = f"{suit_prefix}{rank_suffix}.png"

        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

rename_tarot_images("scraping/downloaded_tarot_cards_03")
