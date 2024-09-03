from Entity import Entity
from Objet import Objet


class Player(Entity):
    """
    Classe avec les accès et actions spécifique au joueur
    """

    def __init__(self, nom: str):
        super().__init__(100, 20)
        self.__niveau: int = 1
        self.__nom: str = nom
        self.__inventaire: [Objet] = []

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, valeur: str) -> None:
        self.__nom: str = valeur

    @property
    def niveau(self) -> int:
        return self.__niveau

    @niveau.setter
    def niveau(self, valeur: str) -> None:
        self.__niveau: str = valeur

    @property
    def inventaire(self) -> [Objet]:
        return self.__inventaire

    def ajouter_inventaire(self, objet: Objet, qte: int = 1) -> None:
        self.__inventaire.extend([objet] * qte)

    def utiliser_objet(self, objet: Objet) -> None:
        if objet in self.inventaire:
            objet.effet(self)
            print(f"{self.nom} a utilisé {objet.nom}. Il a maintenant {self.points_de_vie} HP !")
            self.inventaire.remove(objet)
        else:
            print(f"{self.nom} n'a pas cet objet dans son inventaire.")

    def level_up(self) -> None:
        self.__niveau += 1
        self._points_de_vie_max += 20
        self._points_de_vie += 20
        self._points_attaque += 5
        print(f"LEVEL UP !\nLe joueur est maintenant niveau {self.__niveau}")

    def bruit(self) -> None:
        print("LEEEEROOOOY JEEENKIIINS!")


# Player.methode_statique()

# mon_perso = Player("robin")
# mon_perso.methode_classe()