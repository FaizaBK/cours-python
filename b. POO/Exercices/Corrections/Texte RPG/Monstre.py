import random
from abc import abstractmethod

from Entity import Entity
from Objet import Objet
from Player import Player
from SmallPotion import SmallPotion


class Monstre(Entity):
    """
    Classe abtraite pour les méthodes réservées à tous les monstres
    """
    def __init__(self, points_de_vie_max, points_attaque):
        super().__init__(points_de_vie_max, points_attaque)
        self.__dropable_objects: [Objet] = [SmallPotion()]

    def drop(self, player: Player) -> None:
        objet = random.choice(self.__dropable_objects)
        nb_drop = random.randint(1, 3)
        player.ajouter_inventaire(objet, nb_drop)
        print(f"{self.__class__.__name__} a drop {nb_drop} {objet.nom}")
        print(f"Vous ramassez et mettez dans votre inventaire !")

    @abstractmethod
    def bruit(self) -> None:
        pass
