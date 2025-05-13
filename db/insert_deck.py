import json
import psycopg2

with open("rider_waite_classic.json", "r") as f:
    cards = json.load(f)

conn = psycopg2.connect(dbname="yourdb", user="youruser", password="yourpass")
cur = conn.cursor()

for card in cards:
    cur.execute("""
        INSERT INTO cards (
            name_short, name, type, suit, value, position,
            meaning_up, meaning_rev, description, keywords,
            deck_id, image_url
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        card["name_short"],
        card["name"],
        card["type"],
        card["suit"],
        card["value"],
        card["position"],
        card["meaning_up"],
        card["meaning_rev"],
        card["description"],
        card["keywords"],
        card["deck_id"],
        card["image_url"]
    ))

conn.commit()
cur.close()
conn.close()
