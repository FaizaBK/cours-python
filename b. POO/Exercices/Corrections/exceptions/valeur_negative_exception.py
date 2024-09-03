class ValeurNegativeException(Exception):
    def __init__(self, message="Une erreur personnalisée s'est produite."):
        super().__init__(message)
        

def verifier_valeur(valeur):
    if valeur < 0:
        raise ValeurNegativeException()
    else:
        print(valeur)  # Affiche la valeur valide


try:
    verifier_valeur(10)  # Valeur valide
    verifier_valeur(-5)  # Cette ligne devrait lever une exception
except ValeurNegativeException as alias_exception:
    print(alias_exception)  # Affiche "La valeur ne peut pas être négative."