import csv
from contact import Contact
from groupe import Groupe

def ajouter_contact(contact: Contact, groupe: Groupe) -> None:
    groupe.liste_contacts.append(contact)
        
def supprimer_contact(contact: Contact, groupe: Groupe) -> None:
    contact_index = groupe.liste_contacts.index(contact)
    groupe.liste_contacts.pop(contact_index)
        
def lister_contacts(groupe: Groupe) -> None:
    for contact in groupe.liste_contacts:
        print(contact.nom, contact.prenom, contact.mail, contact.tel)
        
def load_csv(groupe: Groupe, fichier: str) -> None:
    try:
        with open(fichier, "r") as alias_file:
            lecteur_csv = csv.reader(alias_file)
            # next(lecteur_csv) Pas d'en-tête
            for ligne in lecteur_csv:
                nom = ligne[0]
                prenom = ligne[1]
                mail = ligne[2]
                tel = ligne[3]
                contact = Contact(nom, prenom, mail, tel)
                ajouter_contact(contact, groupe)
    except FileNotFoundError as alias_file_not_found:
        print(alias_file_not_found)
            
        
    
def save_csv(groupe: Groupe, fichier: str) -> None:
    with open(fichier, "w") as alias_file:
        writer = csv.writer(alias_file)
        for contact in groupe.contacts:
            # Convertir le contact en une liste de ses attributs
            contact_data = [contact.nom, contact.prenom, contact.mail, contact.tel]
            writer.writerow(contact_data)
        
# mon_groupe = Groupe("Mon groupe",[])
# mon_contact = Contact("Mon nom", "Mon prenom", "example@example.com", "0600000000")
# ajouter_contact(mon_contact, mon_groupe)


# sa permet d'uriliser le csv en tant que dictionnaire,
# mais il a forcément besoin de l'en-tête
# with open(csv_file, "r") as f:
#     read_contacts = csv.DictReader(f)
#     # skip l'en-tête seul
#     for contact in read_contacts:
#         Contact(
#             contact["nom"],
#             contact["prenom"],
#             contact["mail"],
#             contact["telephone"],
#         )