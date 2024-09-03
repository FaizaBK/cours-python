from bibliotheque import Bibliotheque
from livre import Livre


bibliotheque = Bibliotheque()
mon_objet_livre = Livre("Livre 1", "Auteur 1", 2020)

bibliotheque.ajouter_livre(mon_objet_livre)
bibliotheque.lister_livres()
bibliotheque.retirer_livre(mon_objet_livre)
bibliotheque.lister_livres()