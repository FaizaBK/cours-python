import random
from abc import ABC, abstractmethod


class Entity(ABC):
    """Représentation d'une entité du jeu (Interface)
    C'est une classe abstraite non instantiable qui a pour but de centralisées les données pour instaurer
    un design pattern factory afin de créer les différents monstres et le joueur
    """

    def __init__(self, points_de_vie_max: int, points_attaque: int):
        self._points_de_vie_max = points_de_vie_max
        self.points_de_vie = points_de_vie_max
        self._points_attaque = points_attaque
        self.nom = self.__class__.__name__

    # GETTERS / SETTERS

    @property
    def points_de_vie(self) -> int:
        return self._points_de_vie

    @points_de_vie.setter
    def points_de_vie(self, valeur: int) -> None:
        if valeur <= 0:
            self._points_de_vie = 0
        elif valeur >= self._points_de_vie_max:
            self._points_de_vie = self._points_de_vie_max
        else:
            self._points_de_vie: int = valeur

    @property
    def points_attaque(self) -> int:
        return self._points_attaque

    @points_attaque.setter
    def points_attaque(self, valeur: int) -> None:
        self._points_attaque: int = valeur if valeur > 0 else 0

    # METHODES

    def attaquer(self, cible) -> None:
        degats: int = random.randint(0, self.points_attaque)
        cible.points_de_vie -= degats
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts."
              f" Il lui reste {cible.points_de_vie} HP")

    def reset(self) -> None:
        self._points_de_vie = self._points_de_vie_max

    @abstractmethod
    def bruit(self) -> None:
        pass
