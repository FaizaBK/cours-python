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
