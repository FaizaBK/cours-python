from dataclasses import dataclass
import re

@dataclass
class Contact:
    nom: str
    prenom: str
    _mail: str
    _tel: str
    
    @property
    def mail(self) -> str:
        return self._mail
    
    @mail.setter
    def mail(self, new_mail) -> None:
        pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, new_mail):
            self.mail = new_mail
        else:
            print("Le mail n'est pas valide.")
    
    @property
    def tel(self) -> str:
        return self._tel
    
    @tel.setter 
    def tel(self, new_tel) -> None:
        if len(new_tel) == 10 and new_tel.isdigit():
            self.tel = new_tel
        else:
            print("Le téléphone n'est pas valide.")