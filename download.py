"""
Webscraping de Twitter
"""


import os
import re
import time

from bs4 import BeautifulSoup
from selenium import webdriver


def download(*args, live=True, since=False, until=False, lang="en", pause_time=1.5, nb_scroll=100):
    """Téléchargement du code HTML de tweets issus d'une recherche

    Args:
        live (bool, optional): aller dans l'onglet "Récent" de Twitter. Defaults to False.
        since (bool, optional): date minimale de recherche au format YYYY-MM-DD. Defaults to False.
        until (bool, optional): date maximale de recherche au format YYYY-MM-DD. Defaults to False.
        lang (str, optional): langue des tweets. Defaults to "en".
        pause_time (float, optional): temps entre chaque scroll (à adapter en fonction de la connexion). Defaults to 1.5.
        nb_scroll (int, optional): nombre de scrolls max. Defaults to 100.

    """

    if not os.path.exists("web"):
        os.makedirs("web")

    driver = webdriver.Firefox()

    for search in args:
        url = f'https://twitter.com/search?q="{search}"'

        if until:
            url += f"%20until%3A{until}"
        if since:
            url += f"%20since%3A{since}"
        if lang:
            url += f"%20lang%3A{lang}"
        if live:
            url += "&f=live"

        driver.get(url)

        last_height = driver.execute_script(
            "return document.body.scrollHeight")

        max_translateY = -1
        string = ""

        for i in range(nb_scroll):
            print(i)
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)

            page = BeautifulSoup(driver.page_source, 'lxml')
            centre = page.find("div", {
                               "class": "css-1dbjc4n", "aria-label": "Fil d'actualités : Rechercher dans le fil"}).contents[0]
            liste = centre.findAll("div", recursive=False)
            for elem in liste:
                translateY = int(re.findall(
                    "translateY\((.*)px\)", elem.attrs.get("style"))[0])
                if translateY > max_translateY:
                    string += str(elem)
                    max_translateY = translateY

            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        with open(f"web/{search}.html", 'w') as f:
            f.write(string)

    driver.quit()


download("trump", lang='en', since='2012-12-05',
         until='2012-12-06', nb_scroll=1000, pause_time=1)
