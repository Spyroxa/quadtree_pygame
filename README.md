# Création de Quadtree en Python
Projet d'Etude lors de ma troisième année en Bachelor IT à l'EPSI
## Arbre quaternaire
Un quadtree ou arbre quaternaire (arbre Q) est une structure de données de type arbre dans laquelle chaque nœud a quatre fils. Les quadtrees sont le plus souvent utilisés pour partitionner un espace bidimensionnel en le subdivisant récursivement en quatre nœuds. 
## Objectifs
A partir de fichier tel que files/quadtree.txt, générez le QuadTree associé.
Puis, réalisez une interface graphique en utilisant la classe TkQuadTree, permettant de la représenter.
Réaliser une série de test qui montre que tous fonctionne
## Installation
1)Cloner le dépot

2)Vérifier que toutes les dépendances soient installés avec :
```shell
pip install requirements.txt
```

Vérifier que la lecture du fichier se passe sans encombre, en lançant les tests unitaires :
```shell
python -m pytest tests/test_quadtree.py -x
```


