# data_2A

## Installation de l'environnement avec Anaconda

Clone the respository and run  : 
```bash
conda env create
```

## Webscraping de Twitter

Le script [download.py](download.py) permet de télécharger le code HTML de tweets issus de plusieurs recherches (`biden` et `trump` dans notre cas) sur une date donnée. 

:warning: La fonction ne télécharge pas exaustivement l'ensemble des tweets sur la date données, mais seulement un échantillon dont la longueur dépend du paramètre `nb_scroll`.

Le paramètre `pause_time` détermine le temps avant d'effectuer un scroll. Il doit être adapté en fonction de la connexion Internet.

Le script [download_multi.py](download_multi.py) effectue le webscraping en multithreading. 


## Téléchargement des données
Le dossier `data` contenant les données est téléchargeable à l'adresse suivante : https://genes-my.sharepoint.com/:f:/g/personal/bpasquier_ensae_fr/Eo1qlBv9IylGpSgVC4avtTkBycCMeotZkb6pKTU9HxhQ1Q?e=agWDPR
