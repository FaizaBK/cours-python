### Exercice 1 : Citations d'un écrivain

---

À l'aide du package [`quote`](https://pypi.org/project/quote/), obtenable avec [`pip`](https://pypi.org/project/pip/), extraire 30 citations de Edgar Allan Poe.

1. Concevoir un inventaire des titres de livres classés par fréquence d'apparition dans le résultat en ordre décroissant.

2. Dresser un inventaire des mots classés par ordre décroissant de présence dans les citations. Ne pas afficher les mots présents moins de 5 fois.

Au moins deux fonctions doivent être créées pour la conception de chacun de ces inventaires.

> :pushpin: - **Non obligatoire** - Formatage de chaîne de caractères  
> Le [module 're'](https://docs.python.org/fr/3.11/library/re.html) peut être utilisé pour les expression rationnelle. Exemple : enlever la ponctuation.

<br>

### Exercice 2 : Titanic

---

À l'aide du module `csv` uniquement, exploiter les données du fichier `titanic_survival.csv` situé dans le dossier "Annexes". Itérer sur les données et montrer les résultats suivants.

1. Moyenne d'âge des passagers _(~30 ans)_

2. Pourcentage de survie par classe de passager _(~62% pour la première classe, ~43% pour la deuxième classe, ~26% pour la troisième)_

3. Le bateau de sauvetage ayant sauvé le plus de passagers _(bateau n°13 avec 39 passagers sauvés)_

<br>

### Exercice supplémentaire : approfondissement de `quote`

---

| Auteur              |
| ------------------- |
| Edgar Allan Poe     |
| Victor Hugo         |
| Gustave Flaubert    |
| Ernest Hemingway    |
| Agatha Christie     |
| Friedrich Nietzsche |
| Arthur Schopenhauer |
| Simone De Beauvoir  |
| Guy De Maupassant   |
| Voltaire            |
| Emile Zola          |
| Georges Orwell      |
| Frank Herbert       |
| Isaac Asimov        |
| Tolkien             |
| William Shakespeare |

1. À partir de la liste des auteurs, et en utilisant uniquement les fonctionnalités natives de Python, générer 30 citations pour chacun de ces auteurs et générer un set des mots en commun à tous ces auteurs.

    **Exemple** : si le mot "concombre" est utilisé dans une des citations de Victor Hugo, alors si "concombre" est présent dans une des citations de TOUS les auteurs, il doit être présent dans ce set.

2. Faire un classement décroissant des auteurs par le nombre de fois qu'ils utilisent le mot "the" en affichant l'auteur et le nombre de fois que "the" est présent dans ses 30 citations.

3. Écrire ce classement dans un fichier csv avec pour noms de colonne "auteur" et "nombre d'occurrences du mot 'the'".

<br>

[Corrections: "TP Impératif"](Corrections/TP%20Impératif.md)
