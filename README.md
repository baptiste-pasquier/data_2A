# data_2A

Ce projet a pour objectif de faire une analyse de sentiment sur des tweets pour effectuer une prédiction de type `Positive` ou `Negative`.

## Table des matières
* [A. Webscraping de Twitter](#A-Webscraping-de-Twitter)
* [B. Modélisation](#b-Modélisation)
* [C. Installation](#c-Installation)

## A. Webscraping de Twitter

Le script [download.py](download.py) permet de télécharger le code HTML de tweets issus de plusieurs recherches (`biden` et `trump` dans notre cas) sur une date donnée. 

:warning: La fonction ne télécharge pas exaustivement l'ensemble des tweets sur la date données, mais seulement un échantillon dont la longueur dépend du paramètre `nb_scroll`.

Le paramètre `pause_time` détermine le temps avant d'effectuer un scroll. Il doit être adapté en fonction de la connexion Internet.

Le script [download_multi.py](download_multi.py) effectue le webscraping en multithreading. 

Le notebook [parsing.ipynb](parsing.ipynb) créée un dataframe avec les tweets téléchargés.



## B. Modélisation

Nous réalisons un apprentissage de type supervisé en utilisant la base  [Sentiment140](http://help.sentiment140.com/) qui contient 1.6 millions de Tweets déjà catégorisés (`Positive` ou `Negative`).

### 1. Preprocessing

Le notebook [preprocessing.ipynb](preprocessing.ipynb) effectue le preprocessing sur la base Sentiment140 et les tweets webscrapés.

Méthodes utilisées : 
* Count Vectorizer
* TF-IDF
* N-grams

### 2. Statistiques descriptives

Le notebook [description.ipynb](description.ipynb) contient des statistiques descriptives sur la base Sentiment140 et les tweets webscrapés après preprocessing.

### 3. Modélisation

* Logistic Regression : [model-LR.ipynb](model-LR.ipynb)
* Gaussian/Multinomial Naive Bayes : [model-NB.ipynb](model-NB.ipynb)
* Multinomial Naive Bayes Semi-Supervised : [model-semi.ipynb](model-semi.ipynb)
* Neural Networks : [model-NN.ipynb](model-NN.ipynb)

### 4. Résultats

Le notebook [model-semi.ipynb](model-semi.ipynb) contient par ailleurs l'application finale du meilleur modèle sur l'ensemble des tweets webscrapés.

## C. Installation

* Installation de l'environnement d'exécution avec Anaconda

Cloner le répertoire puis exécuter à l'intérieur du répertoire : 
```bash
conda env create
```

* Lancement de JupyterLab ou Jupyter Notebook

Exécuter à l'intérieur du répertoire : 
```bash
conda activate data-2A
jupyter lab
```
ou : 
```bash
conda activate data-2A
jupyter notebook
```
