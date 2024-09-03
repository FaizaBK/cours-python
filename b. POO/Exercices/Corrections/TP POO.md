### Exercice 1
---

```Python
class Entreprise:  
    # Le SIRET est une string car théoriquement, le numéro de SIRET peut commencer par 0
    def __init__(self, nom, adresse, siret):
        self.nom     = nom
        self.adresse = adresse
        self.siret   = siret

    # GETTERS ET SETTERS
    @property
    def siret(self):
        return self.__siret

    @siret.setter
    def siret(self, nouveau_siret):
        if len(nouveau_siret) == 14 and nouveau_siret.isdigit():
            self.__siret = nouveau_siret
        else:
            print("Le numéro SIRET doit comporter exactement 14 caractères numérique.")

    # PRINT
    def __str__(self):
        return f"L'entreprise : {self.nom}, ayant son siège social au {self.adresse}, possède le numéro de SIRET : {self.siret}"


# Affichage console
entreprise = Entreprise("Diginamic", "40 rue Louis Lépine - 34470 Pérols", "81824197800050")  
print(entreprise)  
print(entreprise.nom)  
entreprise.siret = "12345678901234"  
print(entreprise.siret)
```

### Exercice 2
---

```python
from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class DatabaseConnection:
    __type_bdd: str
    __utilisateur: str
    __mot_de_passe: str
  
    # Utilisation de la méthode field pour créer une valeur par défaut
    __hote: str = field(default="localhost")
  
    # Création de notre propriété statique typé en ClassVar
    nb_instance: ClassVar[int] = 0
  
    # Incrémentation de notre nb_instance après chaque initialisation d'objet
    def __post_init__(self):
        DatabaseConnection.nb_instance += 1
  
    @staticmethod
    def get_nb_instance():
        return f"La classe DatabaseConnection possède actuellement {DatabaseConnection.nb_instance} instance(s)."
        
    @classmethod
    def make_instance(cls):
        return cls("mariadb", "root", "1234", "76.287.872.12")


db_conn = DatabaseConnection("postgresql", "test", "mot_de_passe")
print(db_conn)

instance = DatabaseConnection.make_instance()
print(instance)

print(DatabaseConnection.get_nb_instance())
```

### Exercice 3
---

```python
# Va nous être utile pour sortir les 4 lettres aléatoires de l'identifiant interne du compte bancaire  
import random  
  
# Va nous être utile pour faire des opérations sur la date de création du compte bancaire  
from datetime import date  
  
# Va nous être utile pour sortir la liste de toutes les lettres majuscules de l'alphabet latin  
import string  
  
  
class Client:  
  
    def __init__(self, nom: str, prenom: str, nir: str):  
       self.nom    = nom  
       self.prenom = prenom  
       self.nir    = nir  
  
    @property  
    def nir(self):  
       return self.__nir  
  
    @nir.setter  
    def nir(self, nouveau_nir):  
       if nouveau_nir.isdigit() and len(nouveau_nir) == 15:  
          self.__nir = nouveau_nir  
       else:  
          print("Instanciation de la classe impossible: NIR invalide !")  
  
  
class CompteBancaire:  
  
    # Notre propriété statique qui stockera la solde total de tous les clients  
    les_comptes = []  
      
    def __init__(self, date_creation: str, client: Client, solde: float):  
       # random.choices -> liste de k choix parmis une collection d'objets  
       # string.ascii_uppercase -> string contenant les lettres majuscules           # join de la liste pour obtenir une string
       random_letters = ''.join(random.choices(string.ascii_uppercase, k=4))  
         
       # Conversion de notre string reçu en objet date      
       self.date_creation = date.fromisoformat(date_creation)  
         
       # Formatage de la date pour l'id interne  
       formatted_date  = self.date_creation.strftime("%Y%m%d")  
       self.id_interne = random_letters + formatted_date  
       self.client     = client  
       self.solde      = solde  
  
       # Rajout de la solde du nouveau compte au total  
       CompteBancaire.les_comptes.append(self)  
  
    @staticmethod  
    def solde_total():  
       resultat = 0  
       for compte in CompteBancaire.les_comptes:  
          resultat += compte.solde  
       return resultat  
  
    # 2 comptes sont jugés égaux lorsqu'ils ont la même solde  
    def __eq__(self, other):  
       return self.solde == other.solde  
  
  
# Création de notre client  
client = Client("Hotton", "Robin", "782637654189203")  
  
# Création de notre premier comte bancaire  
compte_bancaire_1 = CompteBancaire("2022-06-27", client, 800.99)  
print(compte_bancaire_1.id_interne)  
  
# Notre second compte bancaire a le même client  
compte_bancaire_2 = CompteBancaire("2021-12-03", client, 700_000.01)  
print(compte_bancaire_2.id_interne)  
  
print(compte_bancaire_1 == compte_bancaire_2) # False car les soldes sont inégales  
  
print(CompteBancaire.solde_total())  # Somme de toutes les soldes  
  
compte_bancaire_2.solde = 1  # modification de la solde d'un compte  
  
print(CompteBancaire.solde_total())  # Somme de toutes les soldes
```

### Exercice 4
---

```python
# Notre classe Movie sera une dataclass
from dataclasses import dataclass  

# L'objet path vers le fichier de stockage des données sera une propriété statique parce que j'ai envie
from typing import ClassVar

# Va nous servir pour sortir les films par ordre croissant de date de sortie
from datetime import datetime

# Le package json nous permet de manipuler les fichier json en Python
import json 

# Pathlib nous permettra de gérer les fichiers
import pathlib 

# Nous permettra de faire des regex pour bien vérifier le format des dates en entrée
import re  
  
  
@dataclass  
class Movie:  
    titre: str  
    date_sortie: str  
    resume: str  
    data_file: ClassVar[pathlib.Path] = pathlib.Path().joinpath("data.json")  
  
    def __post_init__(self):  
        data = Movie.data_file  
        data.touch(exist_ok=True)  
        # Si data.json est vide on le rempli avec un premier film  
        if not bool(data.read_text()):  
            with open(data, "w") as file:  
                json.dump({"movies": [self.__dict__]}, file, indent=True)  
        # Sinon on ajout à la liste "movies  
        else:  
            with open(data, "rb") as file_read:  
                decoded = json.load(file_read)  
                # Contrôle des doublons  
                if self.__dict__ not in decoded["movies"]:  
                    decoded["movies"].append(self.__dict__)  
                    with open(data, 'w') as file_write:  
                        json.dump(decoded, file_write, indent=True)  
					print("Film créé avec succès !")  
                else:  
                    print("Film déjà présent !")  
  
    @staticmethod  
	def get_decoded_datas():  
        """  
        Retourne les données du json en lecture        
        """        
        with open(Movie.data_file, "rb") as file_read:  
            return json.load(file_read)  
  
    @staticmethod  
    def find_by_title(title: str) -> dict | bool:  
        """  
        Retourne un film recherché par son titre        
        :param title: le titre du film recherché        
        :return: le film trouvé ou False si le film est introuvable  
        """        
        decoded = Movie.get_decoded_datas()  
        
        for movie in decoded["movies"]:  
            # La recherche fonctionne en majuscule ou en minuscule  
            if movie["titre"].lower() == title.lower():  
                return movie  
            return False  
  
    @staticmethod  
    def find_all() -> None:  
        """  
        Affiche tous les films par ordre croissant de date de sortie        
        :return: None  
        """        
        decoded = Movie.get_decoded_datas()
        # Tri par date de sortie, conversion à la volée  
        sorted_datas = sorted(  
            decoded["movies"],  
            key=lambda mov: datetime.strptime(mov["date_sortie"], "%d/%m/%Y")  
        )  
        print(sorted_datas)  
  
    @staticmethod  
    def delete(title: str) -> bool:  
        """  
        Supprime un film en le recherchant par son titre        
        :param title: le titre du film que l'on veut supprimer        
        :return: True si l'opération a réussie, False sinon  
        """        
        decoded = Movie.get_decoded_datas()  
  
        for index, movie in enumerate(decoded["movies"]):  
            if movie["titre"].lower() == title.lower():  
                decoded["movies"].pop(index)  
                with open(Movie.data_file, 'w') as file_write:  
                    json.dump(decoded, file_write, indent=True)  
                print("Suppression réalisée avec succès !")  
                Movie.find_all()  
                return True  
	        else:  
	            print("Film introuvable !")  
	            return False  
  
    @staticmethod  
    def update(title: str, prop: str, value: str) -> bool:  
        """  
        Modifie un film en le recherchant par son titre        
        :param title: Le titre du film que l'on veut modifier        
        :param prop: La propriété du film que l'on veut modifier        
        :param value: La nouvelle valeur de la propriété que l'on souhaite        
        :return: True si l'opération a réussie, False sinon  
        """        
        decoded = Movie.get_decoded_datas()  
  
        for json_movie in decoded["movies"]:  
            if json_movie["titre"].lower() == title.lower():  
                if prop in json_movie:  
                    json_movie[prop] = value  
                    with open(Movie.data_file, 'w') as file_write:  
                        json.dump(decoded, file_write, indent=True)  
                    print(f"Modification de {prop} réussie !")  
                    print(json_movie)  
                    return True  
                print(f"Propriété {prop} n'existe pas.")  
                return False  
  

# INPUT CONTROLLER
while True:  
    action = input("Choisissez une action: create, read, update ou delete. Stop pour arrêter le script.")  
    match action.lower():  
  
        # CREATE  
        case "create":  
            title = input("Choisir un titre de film : ")  
            if Movie.data_file.is_file() and bool(Movie.find_by_title(title)):  
                print("Ce film est déjà présent dans les données sauvegardées !")  
                exit()  
            date_sortie = input("Choisir une date de sortie (au format dd/mm/YYYY) : ")  
            if not re.fullmatch(r'\d{2}/\d{2}/\d{4}', date_sortie):  
                print("Date au format invalide !")  
                exit()  
            resume = input("Choisir un résumé : ")  
            if bool(title) and bool(resume):  
                movie = Movie(title.title(), date_sortie, resume)  
            else:  
                print("Données vides interdites !")  
  
        # UPDATE  
        case "update":  
            title = input("Choisir le titre de film que vous voulez modifier : ")  
            if not bool(Movie.find_by_title(title)):  
                print("Film inexistant en base de données !")  
                exit()  
            prop = input("Choisir la propriété à modifier (titre, date_sortie, ou resume) : ")  
            match prop.lower():  
                case "titre":  
                    valeur = input("Choisir la nouvelle valeur du titre de film : ")  
                    Movie.update(title, prop, valeur)  
                case "date_sortie":  
                    valeur = input("Choisir la nouvelle date de sortie de film (format dd/mm/YYYY) : ")  
                    if not re.fullmatch(r'\d{2}/\d{2}/\d{4}', valeur):  
                        print("Date au format invalide !")  
                        exit()  
                    Movie.update(title, prop, valeur)  
                case "resume":  
                    valeur = input("Choisir le nouveau résumé du film : ")  
                    Movie.update(title, prop, valeur)  
  
        # DELETE  
        case "delete":  
            title = input("Choisir le titre de film que vous voulez supprimer : ")  
            Movie.delete(title)  
  
        # READ  
        case "read":  
            action = input("Lire tous les films ou un seul par titre ? (titre | tous)")  
            match action:  
                case "titre":  
                    title = input("Choisir le titre de film que vous voulez lire : ")  
                    if not Movie.find_by_title(title):  
                        print("Film inexistant en base de données !")  
                        exit()  
                    movie = Movie.find_by_title(title)  
                    print(movie)  
                case "tous":  
                    Movie.find_all()
```