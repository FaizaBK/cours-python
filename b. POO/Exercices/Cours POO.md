### Objectif

L'objectif de cet exercice est de créer une classe `Animal` en Python et d'explorer divers concepts de la programmation orientée objet.

### Étapes

**Étape 1 - Création de la classe**

- Créez une classe `Animal`.

**Étape 2 - Le constructeur**

- Ajoutez un constructeur (`__init__`) à la classe `Animal`. Le constructeur doit prendre deux attributs : `nom` et `age`.

**Étape 3 - Méthode**

- Ajoutez une méthode appelée `crier` à la classe `Animal`. Cette méthode peut rester vide pour le moment.

**Étape 4 - Propriété statique**

- joutez une propriété statique `population` à la classe `Animal`. Cette propriété doit être initialisée à zéro.

**Étape 5 - Méthode statique**

- Ajoutez une méthode statique appelée `nombre_animaux` à la classe `Animal`. Cette méthode doit renvoyer le nombre total d'animaux créés.

**Étape 6 - Méthode de classe**

- Ajoutez une méthode de classe appelée `esperance_vie` à la classe `Animal`. Cette méthode doit renvoyer une espérance de vie moyenne (par exemple, 10 ans).

**Étape 7 - Méthode magique**

- Ajoutez la méthode magique `__str__` à la classe `Animal`. Cette méthode doit renvoyer une chaîne de caractères décrivant l'animal, par exemple, "Nom (Âge ans)".

**Étape 8 - Héritage**

- Créez une sous-classe `Chien` de la classe `Animal`. La sous-classe doit hériter de la classe `Animal`.

**Étape 9 - Encapsulation**

- Dans la classe `Animal`, ajoutez un attribut privé (commençant par `_`) pour le nom (`_nom`) et l'âge (`_age`). Les attributs privés ne doivent pas être accessibles directement en dehors de la classe.

**Étape 10 - Surcharge**

- Dans la classe `Chien`, surchargez la méthode `crier`. La méthode `crier` de la classe `Chien` doit renvoyer "Woof!".

**Étape 11 - Abstraction**

- La classe `Animal` est actuellement abstraite, car la méthode `crier` est définie comme `pass`. Les sous-classes doivent la redéfinir pour devenir des classes concrètes.
