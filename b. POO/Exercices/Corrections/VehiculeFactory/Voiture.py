from Vehicule import Vehicule


class Voiture(Vehicule):
    """Classe concrète Voiture. Classe fille de Véhicule.

    Attributs:
        marque (str): marque du véhicule.
        modele (str): modèle du véhicule.
        annee (int): année du véhicule.
        vitesse (int): vitesse du véhicule.
        (Optional) nombre_portes (int): nombre de portes de la voiture. Par défaut à 2.
        
    Méthodes:
        demarrer() -> None : permet de démarrer le véhicule.
        accelerer() -> None : permet d'accelerer le véhicule. 
        arreter() -> None : permet d'arrêter le véhicule.
    """
    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int = 3):
        super().__init__(marque, modele, annee)
        self.nombre_portes: int = nombre_portes

    # GETTERS / SETTERS

    @property
    def nombre_portes(self) -> int:
        return self.__nombre_portes

    @nombre_portes.setter
    def nombre_portes(self, valeur) -> None:
        if valeur > 2:
            self.__nombre_portes = valeur

    # METHODES

    def accelerer(self) -> None:
        self.vitesse += 10
        
    def __class__(self) -> str:
        return "Voiture"
