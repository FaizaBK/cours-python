from Entity import Entity
from Objet import Objet


class SmallPotion(Objet):
    """
    Soigne l'entité de 50 points de vie
    """
    def __init__(self):
        super().__init__("petite potion")

    def effet(self, entity: Entity) -> None:
        entity.points_de_vie += 50
