from Vehicule import Vehicule


class Moto(Vehicule):
    """Classe concrète Voiture. Classe fille de Véhicule.

    Attributs:
        marque (str): marque du véhicule.
        modele (str): modèle du véhicule.
        annee (int): année du véhicule.
        vitesse (int): vitesse du véhicule.
        
    Méthodes:
        demarrer() -> None : permet de démarrer le véhicule.
        accelerer() -> None : permet de accelerer le véhicule.
        arreter() -> None : permet d'arrêter le véhicule.
        faire_des_acrobaties() -> str : permet de faire des acrobaties.
    """
    def __init__(self, marque: str, modele: str, annee: int):
        super().__init__(marque, modele, annee)

    # METHODES

    def accelerer(self) -> None:
        self.vitesse += 30

    def faire_des_acrobaties(self) -> str:
        return f"{self.marque} {self.modele} fait des acrobaties. Wheel-in !"
