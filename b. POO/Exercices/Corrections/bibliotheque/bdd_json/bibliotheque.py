import json
from livre import Livre
from livre_empruntable import LivreEmpruntable


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def retirer_livre(self, titre):
        for livre in self.livres:
            if livre.titre == titre:
                self.livres.remove(livre)
                return
        print(f"Le livre avec le titre '{titre}' n'est pas dans la bibliothèque.")

    def lister_livres(self):
        for livre in self.livres:
            livre.afficher_details()

    def emprunter_livre(self, titre):
        for livre in self.livres:
            if (
                livre.titre == titre
                and isinstance(livre, LivreEmpruntable)
                and livre.disponible
            ):
                livre.disponible = False
                print(f"Le livre '{livre.titre}' a été emprunté.")
                return
        print(f"Le livre avec le titre '{titre}' n'est pas disponible pour l'emprunt.")

    def retourner_livre(self, titre):
        for livre in self.livres:
            if (
                livre.titre == titre
                and isinstance(livre, LivreEmpruntable)
                and not livre.disponible
            ):
                livre.disponible = True
                print(f"Le livre '{livre.titre}' a été retourné à la bibliothèque.")
                return
        print(f"Le livre avec le titre '{titre}' ne peut pas être retourné.")

    def charger_bibliotheque(self):
        try:
            with open("bibliotheque.json", "r") as fichier_json:
                data = json.load(fichier_json)
                for livre_data in data:
                    if livre_data["disponible"]:
                        livre = LivreEmpruntable(
                            livre_data["titre"],
                            livre_data["auteur"],
                            livre_data["annee_publication"],
                        )
                    else:
                        livre = Livre(
                            livre_data["titre"],
                            livre_data["auteur"],
                            livre_data["annee_publication"],
                        )
                    self.livres.append(livre)
        except FileNotFoundError:
            print(
                "Le fichier 'bibliotheque.json' n'existe pas. La bibliothèque est vide."
            )

    def sauvegarder_bibliotheque(self):
        data = []
        for livre in self.livres:
            livre_data = {
                "titre": livre.titre,
                "auteur": livre.auteur,
                "annee_publication": livre.annee_publication,
                "disponible": isinstance(livre, LivreEmpruntable) and livre.disponible,
            }
            data.append(livre_data)

        with open("bibliotheque.json", "w") as fichier_json:
            json.dump(data, fichier_json, indent=4)
