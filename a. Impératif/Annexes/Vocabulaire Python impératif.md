# Vocabulaire langage de programmation

## Les fondamentaux

| Concept | Exemple | Description |
|:--------|:--------|:------------|
| Variable              | `x = 5`                          | Espace de stockage en mémoire pour les données, modifiable au fil du temps. |
| Instruction           | `a = b + c`                      | Action exécutée séquentiellement pour effectuer des tâches. |
| Boucle                | `for i in range(10):`            | Structure de contrôle pour répéter des instructions en fonction d'une condition. |
| Condition             | `if x > 0:`                      | Structure de contrôle pour exécuter des instructions en fonction d'une condition. |
| Fonction              | `def addition(a, b):`            | Bloc de code réutilisable pour effectuer une tâche avec des paramètres. |
| Paramètre             | `a` et `b` dans `addition(a, b)` | Variable de la signature d'une fonction qui va recevoir des valeurs lors de l'appel de cette même fonction. |
| Argument              | `a` et `b` dans `addition(a, b)` | Variable extérieur à la fonction que l'on passe en paramètre à la fonction. |
| Signature de fonction | `def addition(a, b) -> float:`   | L'ensemble des éléments d'une fonction avec son nom, ses paramètres avec leurs types et le type de retour de la fonction. |

<br>

## Les types primitifs

| Concept            | Exemple                    | Description                                                                                      |
|--------------------|----------------------------|--------------------------------------------------------------------------------------------------|
| int                | `x = 5`                    | Les entiers représentent des nombres entiers sans décimales.                                      |
| float              | `y = 3.14`                 | Les nombres à virgule flottante représentent des nombres avec décimales.                           |
| str                | `texte = "Bonjour"`        | Les chaînes de caractères représentent des séquences de caractères, souvent utilisées pour du texte.|
| bool               | `est_vrai = True`          | Les valeurs booléennes représentent la vérité (True) ou la fausseté (False).                       |
| list               | `liste = [1, 2, 3]`        | Les listes sont des collections ordonnées et modifiables d'éléments.                                 |
| tuple              | `tup = (1, 2, 3)`          | Les tuples sont des collections ordonnées immuables d'éléments.                                     |
| dict               | `dictionnaire = {'a': 1}`  | Les dictionnaires associent des clés à des valeurs, formant des paires clé-valeur.                |
| set                | `ensemble = {1, 2, 3}`     | Les ensembles sont des collections non ordonnées d'éléments uniques.                               |
| complex            | `z = 3 + 4j`               | Les nombres complexes sont utilisés pour représenter des nombres avec une partie imaginaire.       |
| NoneType           | `valeur = None`            | Le type None est utilisé pour représenter l'absence de valeur ou une valeur nulle.                 |
