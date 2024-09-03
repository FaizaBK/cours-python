L'objectif de cet exercice est d'appliquer les concepts de la Programmation Orientée Objet en utilisant le [design pattern Factory](https://refactoring.guru/fr/design-patterns/factory-method). Vous devrez créer quatre classes : `Vehicule`, `Voiture`, `Moto`, et `VehiculeFactory`.

<br>

### Représentation UML

---

<font color="green">Ⓒ</font> représente une classe
<font color="cyan">Ⓐ</font> représente une classe abstraite
<font color="red">□</font> représente un attribut privé
<font color="green">○</font> représente une méthode public

![representation_uml](umlVehiculeFactory.png)

>[!TIP] Visibilité d'attributs
>Quand on entend attribut privé, on pense getter et setter

<br>

### Classe Vehicule

---

La classe `Vehicule` doit avoir les caractéristiques suivantes :

- Attributs :
    - Marque
    - Modèle
    - Année
    - Vitesse (avec une valeur par défaut de 0)

- Méthodes :
    - `demarrer`
    - `freiner`

De plus, nous souhaitons que la méthode `accelerer` soit une méthode abstraite, c'est-à-dire qu'elle devra être implémentée dans les classes filles (`Voiture` et `Moto`).

<br>

### Classe Voiture

---

La classe `Voiture` hérite de la classe `Vehicule` et possède un attribut supplémentaire :

- Attribut :
    - Nombre de portes (`nb_portes`)

<br>

### Classe Moto

---

La classe `Moto` hérite également de la classe `Vehicule` et a une méthode spécifique :

- Méthode :
    - `faire_des_acrobaties`

<br>

### Classe VehiculeFactory

---

La classe `VehiculeFactory` est responsable de la création d'objets de type `Vehicule`. Elle possède une seule méthode statique :

- Méthode :
    - `creer_vehicule`
