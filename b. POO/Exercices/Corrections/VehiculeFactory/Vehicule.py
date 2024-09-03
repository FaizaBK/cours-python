from abc import ABC, abstractmethod


class Vehicule(ABC):
    """Classe abstraite représentant un véhicule.

    Attributs:
        marque (str): marque du vehicule.
        modele (str): modèle du vehicule.
        annee (int): année du vehicule.
        vitesse (int): vitesse du véhicule.
    
    Méthodes:
        demarrer() -> None : permet de démarrer le véhicule.
        accelerer() -> None : ABSTRAITE. permettra d'accelerer le véhicule. 
        arreter() -> None : permet d'arrêter le véhicule.
    """

    def __init__(self, marque: str, modele: str, annee: int):
        self.marque: str = marque
        self.modele: str = modele
        self.annee: int = annee
        self.vitesse: int = 0

    def __str__(self) -> str:
        return f"{self.__class__.__name__} de marque {self.marque}, de modèle {self.modele}, fabriqué en {self.annee}, roule à {self.vitesse} km/h"

    def __del__(self) -> None:
        print(f"Objet {self.__class__.__name__} est détruit.")
        
    # GETTERS / SETTERS

    @property
    def marque(self) -> str:
        return self._marque

    @marque.setter
    def marque(self, valeur) -> None:
        self._marque = valeur

    @property
    def modele(self) -> str:
        return self._modele

    @modele.setter
    def modele(self, valeur) -> None:
        self._modele = valeur

    @property
    def annee(self) -> int:
        return self._annee

    @annee.setter
    def annee(self, valeur) -> None:
        self._annee = valeur

    @property
    def vitesse(self) -> int:
        return self._vitesse

    @vitesse.setter
    def vitesse(self, valeur) -> None:
        self._vitesse = valeur

    # METHODES

    def demarrer(self) -> str:
        return f"{self.marque} {self.modele} démarre."

    @abstractmethod
    def accelerer(self) -> None:
        pass

    def arreter(self) -> None:
        self.vitesse = 0
