from Monstre import Monstre


class Dragon(Monstre):
    """
    Définition d'un Dragon
    """
    def __init__(self):
        super().__init__(200, 30)

    def bruit(self) -> None:
        print("Roooaar")