import random

from Dragon import Dragon
from Goblin import Goblin
from Player import Player
from SmallPotion import SmallPotion

# création du joueur et de son inventaire
joueur = Player(input("Choisissez votre nom : "))
small_potion = SmallPotion()
joueur.ajouter_inventaire(small_potion, 5)

# création des ennemis possible
all_ennemis_type = [Dragon(), Goblin()]

# Affectation d'un nouvel ennemi aléatoire à chaque boucle
ennemi = random.choice(all_ennemis_type)
print(f"L'ennemi {ennemi.nom} est apparu !\n{ennemi.nom} a {ennemi.points_de_vie} HP")

continuer: str = ""
while joueur.niveau < 20:
    # boucle de combat
    while ennemi.points_de_vie > 0 and joueur.points_de_vie > 0:
        if joueur.points_de_vie <= 50 and joueur.inventaire.__contains__(small_potion):
            joueur.utiliser_objet(small_potion)
        else:
            joueur.attaquer(ennemi)
            if ennemi.points_de_vie <= 0:
                print(f"{ennemi.nom} est vaincu.")
                joueur.level_up()
                ennemi.drop(joueur)
            else:
                ennemi.attaquer(joueur)
                if joueur.points_de_vie <= 0:
                    print(f"Vous êtes vaincu.")
                    continuer = "N"

    # Input controller pour stopper ou continuer la partie
    if continuer != "N" and joueur.niveau < 20:
        continuer = input("Voulez-vous continuer le jeu ? (O/N): ").upper()
        if continuer == "O":
            ennemi.reset()
            ennemi = random.choice(all_ennemis_type)
            print(
                f"L'ennemi {ennemi.nom} est apparu !\n{ennemi.nom} a {ennemi.points_de_vie} HP"
            )
        elif continuer == "N":
            jouer = False
        else:
            print("Input incorrect")

if joueur.niveau == 20:
    print("VOUS AVEZ GAGNE !")
print("Fin du jeu.")
