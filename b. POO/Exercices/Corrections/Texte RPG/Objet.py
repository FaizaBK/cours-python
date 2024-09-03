from abc import ABC, abstractmethod

from Entity import Entity


class Objet(ABC):
    """
    Classe abtraite pour les méthodes réservées à tous les objets
    """
    def __init__(self, nom: str):
        self._nom = nom

    @abstractmethod
    def effet(self, entity: Entity):
        pass

    @property
    def nom(self) -> str:
        return self._nom

    @nom.setter
    def nom(self, valeur) -> None:
        self._nom = valeur
