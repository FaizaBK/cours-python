import random

from Dragon import Dragon
from Goblin import Goblin
from Monstre import Monstre
from Player import Player
from SmallPotion import SmallPotion


def battle(joueur: Player, ennemi: Monstre) -> bool:
    """
    Scénario de combat entre le monstre et le joueur
    :param joueur:
    :param ennemi:
    :return: True, si le joueur a gagné. False sinon.
    """
    potion = SmallPotion()
    while ennemi.points_de_vie > 0 and joueur.points_de_vie > 0:
        if joueur.points_de_vie <= 50 and joueur.inventaire.__contains__(potion):
            joueur.utiliser_objet(potion)
        else:
            joueur.attaquer(ennemi)
            if ennemi.points_de_vie <= 0:
                print(f"{ennemi.nom} est vaincu.")
                joueur.level_up()
                ennemi.drop(joueur)
                ennemi.reset()
                return True
            else:
                ennemi.attaquer(joueur)
                if joueur.points_de_vie <= 0:
                    print(f"Vous êtes vaincu.")
                    return False


def continuer_jouer() -> bool:
    """
    Controller afin de savoir si le joueur veut continuer ou non
    :return: True, s'il continue. False sinon.
    """
    continuer = input("Voulez-vous continuer le jeu ? (O/N): ").upper()
    if continuer == 'O':
        return True
    elif continuer == 'N':
        print("IL FAUT FAIRE UNE SAUVEGARDE")  # A faire
        return False
    else:
        print("Input incorrect")
        return continuer_jouer()


def create_player() -> Player:
    """
    Création du joueur.
    :return: Le joueur avec son inventaire.
    """
    player: Player = Player(input("Choisissez votre nom : "))
    small_potion = SmallPotion()
    player.ajouter_inventaire(small_potion, 5)
    return player


def scenario(joueur: Player, win_condition: int) -> None:
    # création des ennemis possible
    all_ennemis_type = [Dragon(), Goblin(), Goblin(), Goblin(), Goblin()]

    # Affectation d'un nouvel ennemi aléatoire à chaque boucle
    ennemi = random.choice(all_ennemis_type)
    print(f"L'ennemi {ennemi.nom} est apparu !\n{ennemi.nom} a {ennemi.points_de_vie} HP")

    # boucle de jeu
    continuer: bool = True
    while continuer:
        # battle entre le joueur et le monstre
        vainqueur: bool = battle(joueur, ennemi)
        # verifie les conditions de victoire
        if vainqueur and joueur.niveau < win_condition:
            # verifie si le joueur veut continuer
            continuer = continuer_jouer()
            if continuer:
                # s'il continue, fait réapparaitre un ennemi
                ennemi = random.choice(all_ennemis_type)
                print(f"L'ennemi {ennemi.nom} est apparu !\n{ennemi.nom} a {ennemi.points_de_vie} HP")
            else:
                break
        else:
            break


def fin_jeu(player: Player, win_condition: int):
    # Est-ce que le joueur à gagné ?
    if joueur.niveau == win_condition:
        print("VOUS AVEZ GAGNE !")
    print("Fin du jeu.")


if __name__ == "__main__":
    joueur: Player = create_player()
    win_condition: int = 5
    scenario(joueur, win_condition)
    fin_jeu(Player, win_condition)

