from livre import Livre


class LivreEmpruntable(Livre):
    def __init__(self, titre, auteur, annee_publication):
        super().__init__(titre, auteur, annee_publication)
        self.disponible = True

    def afficher_details(self):
        disponibilite = "disponible" if self.disponible else "emprunté"
        print(
            f"Titre: {self.titre} - Auteur: {self.auteur} - Année de publication: {self.annee_publication} - État: {disponibilite}"
        )
