import requests
from bs4 import BeautifulSoup
import os
from urlib.parse import urljoin

BASE_URL = "https://steve-p.org/cards/pix/"
OUTPUT_DIR = "downloaded_tarot_cards_02"

os.makedirs(OUTPUT_DIR, exist_ok=True)

response = requests.get(BASE_URL)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

image_links = [
    urljoin(BASE_URL, a['href'])
    for a in soup.find_all('a', href=True)
    if a['href'].lower().endswith(".png")
]

print(f"found {len(image_links)} images")

for url in image_links:
    filename = url.split("/")[-1]
    filepath = os.path.join(OUTPUT_DIR, filename)
    if os.path.exists(filepath):
        print(f"already downloaded {filename}")
        continue
    
    print(f"downloading {filename}")
    img_response = requests.get(url)
    img_response.raise_for_status()
    
    with open(filepath, "wb") as f:
       f.write(img_response.content)
       
print("that's me done m8")