# import csv
from contact import Contact
from groupe import Groupe

# les_groupes : [Groupe] = []

# def load_csv(fichier: str) -> None:
#     try:
#         with open(fichier, "r") as alias_file:  # ouvre le fichier csv en lecture
#             lecteur_csv = csv.reader(alias_file)  # definis ton reader pour lire correctement le csv
#             # next(lecteur_csv) # skip de l'en-tête
#             for ligne in lecteur_csv:
#                 nom_du_groupe: str = ligne[0]
#                 nom: str = ligne[1]
#                 prenom: str = ligne[2]
#                 mail: str = ligne[3]
#                 tel: str = ligne[4]
                
#                 contact: Contact = Contact(nom, prenom, mail, tel)  # très important
                
#                 for le_groupe in les_groupes:
#                     le_groupe: Groupe
#                     if le_groupe.nom_groupe == nom_du_groupe:
#                         le_groupe.liste_contacts.append(contact)  # ajouter le contact dans le groupe
#                     else:
#                         new_groupe: Groupe = Groupe(nom_du_groupe, [])
#                         les_groupes.append(new_groupe)
#                         new_groupe.liste_contacts.append(contact)  # ajouter le contact dans le groupe
#     except FileNotFoundError as alias_file_not_found:
#         print(alias_file_not_found)
            
# def save_csv(fichier: str) -> None:
#     with open(fichier, "w") as alias_file:  # ouvre le fichier csv en ecriture
#         ecriture_csv = csv.writer(alias_file)  # definis ton writer pour lire correctement le csv
#         for contact in self.liste_contacts:
#             ecriture_csv.writerow([self.nom_groupe, contact.nom, contact.prenom, contact.mail, contact.tel])
                
if __name__ == "__main__":
    mon_groupe = Groupe("groupe",[])
    mon_contact = Contact("nom", "prenom", "example@example.com", "0600000000")
    mon_groupe.ajouter_contact(mon_contact)
    mon_groupe.lister_contacts()
    mon_groupe.supprimer_contact(mon_contact)
    mon_groupe.lister_contacts()