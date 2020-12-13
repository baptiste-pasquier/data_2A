# data_2A

Ce projet a pour objectif de faire une analyse de sentiments sur des tweets pour effectuer une prédiction de type `Positive` ou `Negative`.

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

## Modélisation

Nous réalisons un apprentissage de type supervisé en utilisant la base  [Sentiment140](http://help.sentiment140.com/) qui contient 1.6 millions de Tweets déjà catégorisés.

Modèles utilisés : 

* Logistic Regression : [model-LR.ipynb](model-LR.ipynb)
* Gaussian/Multinomial Naive Bayes : [model-NB.ipynb](model-NB.ipynb)
* Multinomial Naive Bayes Semi-Supervised : [model-semi.ipynb](model-semi.ipynb)
* Neural Networks : [model-NN.ipynb](model-NN.ipynb)
