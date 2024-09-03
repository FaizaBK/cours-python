### **Partie 1 - Version MVP (Minimal Viable Product)**

1. Créez une classe de base appelée "Livre" avec les attributs : titre, auteur et année de publication. Cette classe devrait également inclure une méthode pour afficher les détails du livre.

2. Créez une classe "Bibliothèque" qui permet d'ajouter, retirer et lister les livres disponibles. Pour l'instant, vous pouvez utiliser des listes pour stocker les livres dans la bibliothèque.

3. Créez un programme principal qui vous permet de :
   - Ajouter un livre à la bibliothèque.
   - Retirer un livre de la bibliothèque.
   - Afficher la liste des livres disponibles dans la bibliothèque.

<br>

### **Partie 2 - Améliorations**

4. Ajoutez une classe dérivée "LivreEmpruntable" qui hérite de la classe "Livre". Cette classe devrait inclure un attribut "disponible" pour suivre l'état de l'emprunt (initialisé à True par défaut). La méthode d'affichage des détails devrait être mise à jour pour indiquer l'état de disponibilité.

5. Modifiez la classe "Bibliothèque" pour qu'elle prenne en charge les opérations d'emprunt et de retour de livres. Assurez-vous que la disponibilité des livres est correctement mise à jour.

6. Ajoutez un programme principal amélioré qui permet aux utilisateurs d'emprunter et de retourner des livres.

<br>

### **Partie 3 - Base de données de livres en JSON**

7. Créez un fichier JSON nommé "bibliotheque.json" pour stocker les informations sur les livres de la bibliothèque. Lorsque le programme démarre, il devrait charger les données du fichier JSON dans la bibliothèque.

8. À chaque modification de la bibliothèque (ajout, retrait, emprunt, retour), mettez à jour le fichier JSON pour refléter ces changements.

9. Ajoutez une fonctionnalité permettant de rechercher des livres par titre dans la bibliothèque en utilisant des données JSON.

10. Améliorez l'interface utilisateur du programme principal en ajoutant des options pour effectuer ces opérations.
