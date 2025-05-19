from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
from bs4 import BeautifulSoup

#  headless Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = "https://steve-p.org/cards/RWSa.html"
driver.get(url)

#  time to populate the page (may need tweaked if connection is slow)
time.sleep(5)

# full page source get
soup = BeautifulSoup(driver.page_source, 'html.parser')

# find imgs
imgs = soup.find_all('img')

# dir to store images
os.makedirs('tarot_cards', exist_ok=True)

# grab all images
for img in imgs:
    src = img.get('src')
    if not src:
        continue
    # if relative, make absolute
    if src.startswith('/'):
        src = url.rstrip('/') + src
    elif not src.startswith('http'):
        src = url.rstrip('/') + '/' + src

    filename = os.path.join('tarot_cards', os.path.basename(src))
    try:
        img_data = requests.get(src).content
        with open(filename, 'wb') as f:
            f.write(img_data)
        print(f"Downloaded {filename}")
    except Exception as e:
        print(f"Failed to download {src}: {e}")

driver.quit()
