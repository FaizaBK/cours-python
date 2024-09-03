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
    data_file: ClassVar[pathlib.Path] = pathlib.Path().joinpath("../data.json")

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
    action = input("Choisissez une action: create, read, update ou delete. Stop pour arrêter le script.\n")
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
            action = input("Lire tous les films ou un seul par titre ? (titre | tous) : ")
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
