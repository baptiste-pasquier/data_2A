from selenium import webdriver
import time
import os

SEARCH_NAMES = ["trump"]
PAUSE_TIME = 3

if not os.path.exists("web"):
    os.makedirs("web")

driver = webdriver.Firefox()

for search in SEARCH_NAMES:
    url = f"https://twitter.com/search?q={search}&lang=en"
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")

    for i in range(5):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height

    with open(f"web/{search}.html", 'w') as f:
        f.write(driver.page_source)
