"""
Webscraping de Twitter / multiprocessing
"""


import datetime
import os
import re
import shutil
import threading
import time
from multiprocessing.pool import ThreadPool

import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


def download(*args, live=False, since=False, until=False, date=False, lang="en", pause_time=1.5, nb_scroll=100, path='', driver=webdriver.Firefox()):
    """Téléchargement du code HTML de tweets issus d'une recherche

    Args:
        path (str): destination des fichiers téléchargés.
        live (bool, optional): aller dans l'onglet "Récent" de Twitter. Defaults to False.
        since (bool, optional): date minimale de recherche au format YYYY-MM-DD. Defaults to False.
        until (bool, optional): date maximale de recherche au format YYYY-MM-DD. Defaults to False.
        date (bool, optional): date de recherche au format YYYY-MM-DD. Defaults to False.
        lang (str, optional): langue des tweets. Defaults to "en".
        pause_time (float, optional): temps entre chaque scroll (à adapter en fonction de la connexion). Defaults to 1.5.
        nb_scroll (int, optional): nombre de scrolls max. Defaults to 100.
        driver (selenium.webdriver, optional)

    """
    if date and (since or until):
        raise ValueError()

    if date:
        since = date
        until = datetime.datetime.strptime(
            since, '%Y-%m-%d') + datetime.timedelta(days=1)
        until = until.strftime('%Y-%m-%d')

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
        compteur = 0

        for _ in range(nb_scroll):
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(pause_time)

            page = BeautifulSoup((driver.page_source).encode('utf-8'), 'lxml')
            centre = page.find("div", {
                               "class": "css-1dbjc4n", "aria-label": "Fil d'actualités : Rechercher dans le fil"}).contents[0]
            liste = centre.findAll("div", recursive=False)

            for elem in liste:
                translateY = int(re.findall(
                    "translateY\((.*)px\)", elem.attrs.get("style"))[0])
                if translateY > max_translateY:
                    max_translateY = translateY

                    if not live:
                        # Pour enlever les profils qui apparaissent en haut de la page (pas tout le temps...)
                        if compteur >= 6:
                            string += str(elem) + '\n\n\n\n'
                        compteur += 1
                    else:
                        string += str(elem) + '\n\n\n\n'

            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        if date:
            file = os.path.join(path, f"{search}-{date}.html")
        else:
            file = os.path.join(path, f"{search}.html")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(string)


# Pour économiser le temps d'ouverture du navigateur, on utilise un unique webdriver pour chaque thread. On va donc associer un webdriver à chaque thread.

threadLocal = threading.local()     # Permet d'avoir un identifiant pour chaque thread.


def get_driver():
    """Renvoie l'unique webdriver de chaque thread

    Returns:
        selenium.webdriver
    """
    driver = getattr(threadLocal, 'driver', None)
    nb = getattr(threadLocal, 'nb', None)
    if driver is None:
        driver = webdriver.Firefox()
        setattr(threadLocal, 'driver', driver)
        setattr(threadLocal, 'nb', 1)
    elif nb == 10:
        driver.close()
        driver = webdriver.Firefox()
        setattr(threadLocal, 'driver', driver)
        setattr(threadLocal, 'nb', 1)
    else:
        setattr(threadLocal, 'nb', nb + 1)
    return driver


PATH = os.path.join('data', 'web', 'html')


def f(date):
    """
    Fonction d'une seule variable pour le multithreading
    """
    print(date)
    return download("trump", "biden", lang='en', live=False, date=date, nb_scroll=20, pause_time=1.75, path=PATH, driver=get_driver())


if __name__ == '__main__':

    if not os.path.exists(PATH):
        os.makedirs(PATH)

    shutil.rmtree(PATH)     # On supprime les fichiers existants
    os.makedirs(PATH)

    LIST_DATES = pd.date_range(
        start='2019-01-01', end='2019-12-31', periods=100).to_pydatetime().tolist()
    LIST_DATES = [date.strftime('%Y-%m-%d') for date in LIST_DATES]

    NB_THREADS = 2
    a = time.time()
    ThreadPool(NB_THREADS).map(f, LIST_DATES)
    print(time.time() - a)
