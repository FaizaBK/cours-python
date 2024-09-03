L'objectif de cet exercice est d'appliquer les concepts de la Programmation Orientée Objet en utilisant le [design pattern Factory](https://refactoring.guru/fr/design-patterns/factory-method). Vous devrez créer quatre classes : `Vehicule`, `Voiture`, `Moto`, et `VehiculeFactory`.

> Ce design pattern sert à centraliser pléthore d'instanciation de classe différente grâce à une seule méthode.

Pour ce faire, on va implémenter petit à petit les concepts plutôt que faire tout d'un coup et se rendre compte que ça ne fonctionne pas. Cela nous fera perdre plus de temps que ce que l'on pourrait en gagner.
**Ceci est une méthode agile et permet d'avoir constamment une application fonctionnelle.**

> [!Info] Le typage
> Le typage est apparus avec python 3.0 pour les variables/attributs et en python 3.5 pour les retours de fonctions/méthodes.
>
> Il est fortement recommandé de l'utiliser, mais ne sert qu'à titre informatif.

> [!TIP] Documentation
> Comme dans tout travail, pensez à faire de la documentation.

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

### Création des classes

---

On va tout d'abord créer les 3 classes les plus basiques possibles au format [PascalCase](https://fr.wikipedia.org/wiki/Camel_case), c'est à dire avec la première lettre de chaque mot collé et en majuscule : `VehiculeFactory`

```python
class Vehicule:
 def __init__(self):
  pass
```

```python
class Voiture:
 def __init__(self):
  pass
```

```python
class Moto:
 def __init__(self):
  pass
```

<br>

### Héritage

---

Maintenant que nos classes sont créées, nous allons pouvoir leur instaurer de l'héritage qui aura pour but de réduire la duplication de code, et donc de faciliter la maintenance.

Il a aussi un autre gros avantage, c'est que grâce à l'héritage, on peut faire de la généralisation de traitement. Exemple : faire une boucle sur tous les véhicules pour tous leur faire faire la même méthode.

```python
class Voiture(Vehicule):
 def __init__(self):
  pass
```

```python
class Moto(Vehicule):
 def __init__(self):
  pass
```

<br>

### Abstraction

---

L'abstraction va de concert avec l'héritage afin de réduire la duplication de code, mais il a aussi une autre fonctionnalité majeure.
**Une classe abstraite ne peut pas être instancié.**
Le but de cela est de **ne pas pouvoir créer des objets amalgame qui n'ont pas de forme ou de représentation fixe** comme une voiture.

<br>

Pour définir en théorie une classe abstraite en python, il faut soit déclarer un héritage entre notre classe et la classe `abc.ABC`

```python
from abc import ABC

class Vehicule(ABC):
```

Soit, il faut déclarer une méthode avec l'annotation `@abstractmethod`

```python
from abc import abstractmethod

@abstractmethod
def accelerer(self) -> None:
 pass
```

Sauf qu'en pratique, si la classe n'a pas de méthode abstraite, et peut quand même être instanciée.

> Donc pour rendre une classe abstraite, elle dit absolument avoir au moins une méthode abstraite.

> [!TIP] Les retours de fonctions
> la partie `-> None` du code au-dessus permet de fixer ce que devra renvoyer la méthode.
>
> Ici, il renvoi un `None`, car dans mon code, je l'utilisais pour de l'affichage. Du coup, la méthode ne doit rien renvoyer.

<br>

### Attribut

---

Maintenant que 3 classes et leurs relations sont définis, on va pouvoir définir leurs attributs.  
  
Il faut se demander si l'attribut que l'on veut ajouter pourra se mettre dans Voiture et/ou dans Moto :

- Si on peut la mettre que dans une seule des 2, alors on l'a lui affecte.  
- Sinon on l'affecte à véhicule, car elle mutualise l'information.

<br>

Je veux ajouter les attributs que l'on écrit au format [snake_case](https://fr.wikipedia.org/wiki/Snake_case):
`marque`, `modele`, `annee`, `vitesse` et `nb_portes`

On se pose la question : Ou je mets mon attribut ?

Comme `marque`, `modèle`, `année` et `vitesse` peuvent être dans `Voiture` et `Moto`, alors je les mets dans `Vehicule`.

```python
class Vehicule(ABC):
 def __init__(self, marque: str, modele: str, annee: int):  
     self._marque: str = marque  
     self._modele: str = modele  
     self._annee: int = annee  
     self._vitesse: int = 0
```

> [!TIP] Les affectation d'attributs
> On peut décider d'affecter des informations à la création de l'objet en le mettant dans la signature de fonction : `def __init__(self, marque: str, modele: str, annee: int):`, ou alors de les affecter avec une valeur par défaut :  `self._vitesse: int = 0`.
>
> Il est aussi possible de laisser le choix de remplir un attribut à la création d'un Objet, mais avec une valeur par défaut, ce qui rend l'attribut optionnel pour créer l'objet : `def __init__(self, marque: str, modele: str, annee: int, vitesse: int = 0):`

Vous vous demandez pourquoi j'ai mis un '\_' devant mes attributs ?

> [!Info] La visibilité des attributs
> Ceci est une convention utilisé en python est consiste à laisser ou non l'accès à un attribut :
>
> ```python
> self.publique  # attribut accessible par tout le monde
> self._proctected  # attribut accessible uniquement par héritage
> self.__private  # attribut accessible uniquement par la classe qui la possède
> ```
>
> Dans d'autre langage, ce n'est pas une convention mais il est instaurer en dur avec des mots clé, comme en java.

<br>

Comme il n'y a que la voiture qui possède des portes, je lui affecte l'attribut

```python
class Voiture(Vehicule):  
    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int): 
        super().__init__(marque, modele, annee)  
        self.nombre_portes: int = nombre_portes
```

> [!Info] Le mot clé `super()`
> C'est la façon pour une classe fille qu'elle a pour utiliser une méthode de sa classe mère.
>
> Ici, elle appelle le `__init__()` de sa classe mère afin qu'elle fasse le traitement de ses attributs à sa place.

<br>

### Les méthodes

---

Les méthodes sont les actions que peux faire une classe.
Je veux que mes véhicules puissent `demarrer`, `accelerer` et `arreter`
Je veux aussi que ma moto puisse `faire_des_acrobaties` comme un Wheel-in.

```python
from abc import ABC, abstractmethod

class Vehicule(ABC):
 ...
 
 def demarrer(self) -> str:  
     return f"{self.marque} {self.modele} démarre."  

 @abstractmethod
 def accelerer(self) -> str:  
     pass
      
 def arreter(self) -> str:  
     self.vitesse = 0  
```

Comme on a déjà défini `demarrer`, `accelerer` et `arreter` dans la classe `Vehicule`, on aura plus besoin de les réécrire, sauf `accelerer` car elle est abstraite.

```python
class Voiture:
 ...

 def accelerer(self) -> None:  
     self.vitesse += 10
```

Pareil que pour la Voiture, sauf qu'on doit aussi ajouter la méthode `faire_des_acrobaties` qui est spécifique à la Moto

```python
class Moto:
 ...

 def accelerer(self) -> None:  
     self.vitesse += 30

 def faire_des_acrobaties(self) -> str:
  print("La Moto fais un wheel-in")
```

<br>

### L'encapsulation

---

L'encapsulation permet principalement de protéger les attributs et les méthodes `protected` et `private`.
Il a divers autre utilisation mais que je ne vais pas tout détailler.

> Les méthodes `accelerer` et `arreter` sont de l'encapsulation, car on ne donne qu'une quantitée limité d'action effectuable sur un attribut.

Une fonctionnalité de l'encapsulation est les `getters` et les `setters` :

```python
@property  
def marque(self) -> str:  
    return self._marque  
  
@marque.setter  
def marque(self, valeur) -> None:  
    self._marque = valeur
```

> [!info] getters / setters
> Il est très intéressant d'en mettre uniquement à partir du moment où on doit faire des traitements sur l'attribut.
>
> ```python
> @nombre_portes.setter  
> def nombre_portes(self, valeur) -> None:  
>  self.__nombre_portes = valeur if valeur > 2 else 2
> ```
>
> Ici, on ne peut pas créer une voiture avec moins de 2 portes, car sinon comment on entrerait dans la voiture ?

> [!TIP]
Vous pouvez utiliser getters et les setters dans le constructeur `__init__` afin de restreindre aussi à la création les restrictions des attributs, et que l'on ne puisse pas créer de voiture sans porte.
>
> ```python
> class Voiture(Vehicule):  
>    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int = 2):  
>        super().__init__(marque, modele, annee)  
>        self.nombre_portes: int = nombre_portes
>```
>
>on a remplacé le `self.__nombre_portes` par `self.nombre_portes`
>
> >Il est aussi possible de faire pareil pour les méthodes.

<br>

### Implémentation de la Factory

---

Maintenant que nos 2 Entités `Moto` et `Voiture` sont créées, on va pouvoir faire notre Factory.

La fabrique ne contiendra qu'une seule méthode statique qui aura pour but de créer le bon objet avec les bons attributs quand on l'appellera.

```python
class VehiculeFactory:

    @staticmethod
    def creer_vehicule(type_vehicule, *args, **kwargs) -> Vehicule:
        if type_vehicule.lower() == "voiture":
            return Voiture(*args, **kwargs)
        elif type_vehicule.lower() == "moto":
            return Moto(*args, **kwargs)
        else:
            raise ValueError("Type de véhicule non valide")
```

On peut maintenant l'appeler dans le `main.py` afin de créer des `Vehicules`.

```python
# Initialisation de la factory
factory = VehiculeFactory()
  
# Initialisation des véhicules
voiture = factory.creer_vehicule("Voiture", "Toyota", "Camry", 2022, nombre_portes=4)
moto = factory.creer_vehicule("Moto", "Harley-Davidson", "Sportster", 2023)

# Affichage des véhicules
print(voiture)
print(moto)
```

Maintenant que nos Véhicules sont créés, on peut utiliser leurs méthodes.

```python
vehicules = [voiture, moto]

for vehicule in vehicules:
    name = vehicule.__class__.__name__
    
    print(vehicule.demarrer())
    print(f"la {name} roule à {vehicule.vitesse} km/h")
    
    vehicule.accelerer()
    print(f"la {name} roule à {vehicule.vitesse} km/h")
    
    vehicule.arreter()
    print(f"la {name} roule à {vehicule.vitesse} km/h")
```
