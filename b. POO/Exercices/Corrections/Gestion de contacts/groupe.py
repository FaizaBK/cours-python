import csv
from dataclasses import dataclass
from contact import Contact

@dataclass
class Groupe:
    nom_groupe: str
    liste_contacts: [Contact]
    
    def ajouter_contact(self, contact: Contact) -> None:
        self.liste_contacts.append(contact)
            
    def supprimer_contact(self, contact: Contact) -> None:
        contact_index = self.liste_contacts.index(contact)
        self.liste_contacts.pop(contact_index)
            
    def lister_contacts(self) -> None:
        for contact in self.liste_contacts:
            print(contact.nom, contact.prenom, contact.mail, contact.tel)
            
    