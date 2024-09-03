*N'oubliez pas de faire un `main.py` pour créer vos objets et utiliser leurs méthodes afin d'être sur que votre code fonctionne.*

<br>

Le but de l'exercice est d'utiliser des dataclasses `Contact` et `Groupe`.

<br>

### **MVP - Création de Dataclasses**
---

- Créez une dataclass "Contact" avec les attributs suivants : `nom`, `prenom`, `mail` et `telephone`. Placez cette dataclass dans un fichier nommé `contact.py`.
- Créez une nouvelle dataclass "Groupe" avec les attributs `nom_groupe` et une `liste_contacts`. Placez cette dataclass dans un fichier nommé `groupe.py`.

> [!info] Bonus
> Assurez-vous que l'adresse e-mail est valide et que le numéro de téléphone suit un format correct.
> 
> Pour le mail avec le module re :
> ```python
> pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
> ```
> 
> Sinon, vérifiez que le mail possède un `@` et un `.`

- Créez des fonctions afin d'ajouter un `Contact` dans un `Groupe`, supprimer un `contact` d'un `groupe` et lister tous les `contacts` d'un `groupe`.

<br>

### Améliorations
---

- Ajoutez une fonction pour rechercher un contact par son nom ou son adresse e-mail dans la liste et afficher les informations du contact trouvé.
- Empêchez l'ajout d'un contact s'il existe déjà un contact avec le même nom ou la même adresse e-mail 
- Ajoutez une fonction pour supprimer un contact de la liste.
- (Optionnel) Ajoutez des fonctions pour exporter la liste de contacts dans un fichier CSV et importer des contacts à partir de ce fichier.
