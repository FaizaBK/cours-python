from VehiculeFactory import VehiculeFactory

# CREATION DES VÉHICULES
# Initialisation de la factory
factory = VehiculeFactory()

# Initialisation des véhicules
print(f"Création d'instances de véhicules")
print("="*35)
print(f"Création d'une voiture")
voiture = factory.creer_vehicule("Voiture", "Toyota", "Camry", 2022, nombre_portes=4)
print(f"Création d'une moto")
moto = factory.creer_vehicule("Moto", "Harley-Davidson", "Sportster", 2023)


# METHODES DES VEHICULES
# Utilisation des méthodes de voiture
print("\nMéthodes de la voiture")
print("="*35)
print(voiture.demarrer())
print(f"la voiture roule à {voiture.vitesse} km/h")
voiture.accelerer()
print(f"la voiture accelere")
print(f"la voiture roule à {voiture.vitesse} km/h")
voiture.arreter()
print(f"la voiture s'est arreter")
print(f"la voiture roule à {voiture.vitesse} km/h")

# Utilisation des méthodes de moto
print("\nMéthodes de la moto")
print("="*35)
print(moto.demarrer())
print(f"la moto roule à {moto.vitesse} km/h")
moto.accelerer()
print(f"la moto accelere")
print(f"la moto roule à {moto.vitesse} km/h")
moto.arreter()
print(f"la moto s'est arreter")
print(f"la moto roule à {moto.vitesse} km/h")


# On peut stocker tous les objets dans une même liste
# Grâce à ça, tu peux faire un traitement généralisé
vehicules = [voiture, moto]

# Traitement généralisée ensemble
print("\nTous ensemble !")
print("="*35)
for vehicule in vehicules:
    print(vehicule.demarrer())
    print(f"la {vehicule.__class__.__name__} roule à {vehicule.vitesse} km/h")

for vehicule in vehicules:
    print(vehicule.accelerer())
    print(f"la {vehicule.__class__.__name__} roule à {vehicule.vitesse} km/h")

for vehicule in vehicules:
    print(vehicule.arreter())
    print(f"la {vehicule.__class__.__name__} roule à {vehicule.vitesse} km/h")


# Traitement généralisé l'un après l'autre
print("\nL'un après l'autre !")
print("="*35)
for vehicule in vehicules:
    name = vehicule.__class__.__name__
    print(vehicule.demarrer())
    print(f"la {name} roule à {vehicule.vitesse} km/h")
    vehicule.accelerer()
    print(f"la {name} roule à {vehicule.vitesse} km/h")
    vehicule.arreter()
    print(f"la {name} roule à {vehicule.vitesse} km/h")


# SUPPRESSION DES OBJETS
# On vide le stockage avant la fin du programme
print("\nLibération de l'espace mémoire")
print("="*35)
del voiture
del moto