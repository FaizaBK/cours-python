from livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres : [Livre] = []

    def ajouter_livre(self, livre: Livre) -> None:
        self.livres.append(livre)
        

    def retirer_livre(self, livre: Livre) -> None:
        if livre in self.livres:
            self.livres.remove(livre)
        else:
            print(f"Le livre avec le titre '{self.titre}' n'est pas dans la bibliothèque.")
        

    def lister_livres(self):
        for livre in self.livres:
            # livre.afficher_details()
            print(livre)