from Monstre import Monstre


class Goblin(Monstre):
    """
    Définition d'un Gobelin
    """
    def __init__(self):
        super().__init__(50, 10)

    def bruit(self) -> None:
        print("Kekeke")
