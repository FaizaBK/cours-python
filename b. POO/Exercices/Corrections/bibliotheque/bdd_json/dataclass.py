class Contact:
    
    def __init__(self, nom, prenom, mail, tel, security) -> None:
        self.nom: str = nom,
        self.prenom: str = prenom,
        self.mail: str = mail,
        self.__tel: str = tel,
        self.security: str = security
    
    @property
    def tel(self) -> str:
        return self.__tel
    
    @tel.setter
    def tel(self, tel: str):
        if condition_longueur_10(security):
            self.__tel = tel
            
    @property
    def security(self) -> str:
        return self.__security
    
    @security.setter
    def security(self, security: str):
        if condition_longueur_10(security):
            self.__security = security
            
    def condition_longueur_10(self, attribut) -> bool:
        return len(self.attribut) == 10
            
            
contact = Contact("robin", "hotton", "ychag@example.com", "0123456789")
print(contact)