# Analyse de sentiment sur Twitter concernant les élections USA

## Problématique

Déterminer si un tweet est négatif ou positif, et concernant Biden ou Trump.

## Données

* Webscraping de tweets contenant "Trump" ou "Biden"

* Liste de mots négatifs et positifs

* Base de données déjà catégorisées contenant des tweets/textes avec une colonne "négatif ou positif"

## Démarche

* Nettoyage de la base webscrappée, attributation des tweets à Trump ou Biden.
(Par exemple, suppression des tweets comprenant à la fois Trump et Biden)

* ~~Première idée : Créer un score avec la proportion de mots positifs ou négatifs (grâce à une liste de mots) pour déterminer si un tweet est positif ou négatif~~ UPDATE : idée non performante


* Deuxième idée : Algorithme supervisé (régression logistique par exemple) à partir de la base de données déjà catégorisées

* Data visualisation (aire géographique, évolution au cours du temps)

## TO DO

* Preprocessing : utiliser TF IDF au lieu de CountProcessing

* Algorithme de classification : modèle naïf bayésien (random search puis gridsearch)

* Apprentissage semi-supervisé