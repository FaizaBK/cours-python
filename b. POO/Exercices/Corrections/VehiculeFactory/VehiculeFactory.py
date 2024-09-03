from Moto import Moto
from Vehicule import Vehicule
from Voiture import Voiture


class VehiculeFactory:
    """Factory permettant d'instancier un véhicule.

    Raises:
        ValueError: erreur dans la console si le type de véhicule n'est pas valide.

    Returns:
        classe fille de Vehicule: instantiation du véhicule grâce à type_vehicule(str) de la méthode creer_vehicule, et de ses paramètres(*args, **kwargs).
    """
    @staticmethod
    def creer_vehicule(type_vehicule, *args, **kwargs) -> Vehicule:
        if type_vehicule.lower() == "voiture":
            return Voiture(*args, **kwargs)
        elif type_vehicule.lower() == "moto":
            return Moto(*args, **kwargs)
        else:
            raise ValueError("Type de véhicule non valide")
