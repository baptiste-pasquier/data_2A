from selenium import webdriver
import time
import os
from bs4 import BeautifulSoup
import re

SEARCH_NAMES = ["biden", "trump"]
PAUSE_TIME = 1.5

if not os.path.exists("web"):
    os.makedirs("web")

driver = webdriver.Firefox()

for search in SEARCH_NAMES:
    url = f'https://twitter.com/search?q="{search}"%20until%3A2020-09-02%20since%3A2020-09-01&lang=en&f=live'
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")

    max_translateY = -1
    string = ""

    for i in range(100):
        print(i)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(PAUSE_TIME)

        page = BeautifulSoup(driver.page_source, 'lxml')
        centre = page.find("div", {"class": "css-1dbjc4n", "aria-label": "Timeline: Search timeline"}).contents[0]
        liste = centre.findAll("div", recursive=False)
        for elem in liste:
            translateY = int(re.findall("translateY\((.*)px\)", elem.attrs.get("style"))[0])
            if translateY > max_translateY:
                string += str(elem)
                max_translateY = translateY

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    with open(f"web/{search}.html", 'w') as f:
        f.write(string)

driver.quit()