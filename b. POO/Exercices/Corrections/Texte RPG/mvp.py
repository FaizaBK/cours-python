import random


class Personnage:
    def __init__(self, nom, points_de_vie, points_attaque):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.points_attaque = points_attaque

    def attaquer(self, cible):
        degats = random.randint(0, self.points_attaque)
        cible.points_de_vie -= degats
        print(f"{self.nom} attaque {cible.nom} et lui inflige {degats} points de dégâts."
              f" Il lui reste {cible.points_de_vie if cible.points_de_vie > 0 else 0} HP")


class Ennemi:
    def __init__(self, nom, points_de_vie):
        self.nom = nom
        self.points_de_vie = points_de_vie


# Création du personnage joueur
joueur = Personnage("Joueur", 100, 20)

# Boucle de jeu
while True:
    # Création d'un nouvel ennemi à chaque boucle
    ennemi = Ennemi("Sac à patate", 50)
    print(f"L'ennemi {ennemi.nom} est apparu !\n{ennemi.nom} a {ennemi.points_de_vie} HP")
    while ennemi.points_de_vie > 0:
        joueur.attaquer(ennemi)
    print(f"{ennemi.nom} est vaincu.")

    # Input controller pour stopper ou continuer la partie
    continuer = input("Voulez-vous continuer le jeu ? (O/N): ")
    if continuer.upper() != 'O':
        break

print("Fin du jeu.")
