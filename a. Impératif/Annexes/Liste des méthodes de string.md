| Fonction | Exemple | Description |
|:---------|:--------|:------------|
| `capitalize()` | `texte = "exemple"`<br>`resultat = texte.capitalize()`<br><br>`# Résultat : "Exemple"`| Convertit le premier caractère de la chaîne en majuscule |
| `count()`      | `texte = "exemple exemple exemple"`<br>`compte = texte.count("exemple")`<br><br>`# Résultat : 3` | Retourne le nombre de fois que la chaîne spécifiée est trouvée |
| `encode()`     | `texte = "exemple"`<br>`encodage = texte.encode("utf-8")`<br><br>`# Résultat : b'exemple'` | Retourne une version encodée de la chaîne |
| `endswith()`   | `texte = "exemple"`<br>`resultat = texte.endswith("ple")`<br><br>`# Résultat : True` | Retourne `True` si la chaîne se termine par la valeur spécifiée  |
| `find()`       | `texte = "exemple"`<br>`index = texte.find("pl")`<br><br>`# Résultat : 4` | Cherche dans la chaîne de caractères la valeur spécifiée et retourne l'index correspondant |
| `format()`     | `texte = "Mon nom est {} et j'ai {} ans".format("Alice", 30)`<br><br>`# Résultat : "Mon nom est Alice et j'ai 30 ans"`       | Permet de formater une chaîne de caractères  |
| `index()`      | `texte = "exemple"`<br>`index = texte.index("pl")`<br><br>`# Résultat : 4` | Cherche dans la chaîne de caractères la valeur spécifiée et retourne l'index correspondant |
| `isalnum()`    | `texte = "exemple123"`<br>`est_alnum = texte.isalnum()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères dans la chaîne sont alphanumériques |
| `isalpha()`    | `texte = "exemple"`<br>`est_alpha = texte.isalpha()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères dans la chaîne sont des lettres de l'alphabet |
| `isdecimal()`  | `texte = "12345"`<br>`est_decimal = texte.isdecimal()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères dans la chaîne sont de type décimal |
| `isdigit()`    | `texte = "12345"`<br>`est_digit = texte.isdigit()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères dans la chaîne sont des nombres |
| `islower()`    | `texte = "exemple"`<br>`est_lower = texte.islower()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères sont en minuscule |
| `isnumeric()`  | `texte = "12345"`<br>`est_numeric = texte.isnumeric()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères sont numériques |
| `isupper()`    | `texte = "EXEMPLE"`<br>`est_upper = texte.isupper()`<br><br>`# Résultat : True` | Retourne `True` si tous les caractères sont en majuscule |
| `join()`       | `liste = ["a", "b", "c"]`<br>`texte = "-".join(liste)`<br><br>`# Résultat : "a-b-c"` | Joint avec le caractère spécifié tous les éléments d'un itérable passé en argument |
| `lower()`      | `texte = "Exemple"`<br>`resultat = texte.lower()`<br><br>`# Résultat : "exemple"` | Convertit la chaîne en minuscule |
| `replace()`    | `texte = "exemple"`<br>`resultat = texte.replace("e", "X")`<br><br>`# Résultat : "XxXamplX"` | Remplace un élément de la chaîne par un autre |
| `split()`      | `texte = "exempl1 exempl2 exempl3"`<br>`resultat = texte.split(" ")`<br><br>`# Résultat : ['exempl1', 'exempl2', 'exempl3']` | Sépare la chaîne de caractères sur les caractères passés en argument et retourne une liste |
| `startswith()` | `texte = "exemple"`<br>`resultat = texte.startswith("ex")`<br><br>`# Résultat : True` | Retourne `True` si la chaîne commence par la valeur spécifiée |
| `strip()`      | `texte = "   exemple   "`<br>`resultat = texte.strip()`<br><br>`# Résultat : "exemple"` | Supprime les caractères spécifiés du début et de la fin de la chaîne |
| `swapcase()`   | `texte = "eXeMpLe"`<br>`resultat = texte.swapcase()`<br><br>`# Résultat : "ExEmPlE"` | Change la casse (les majuscules deviennent minuscules et vice-versa) |
| `title()`      | `texte = "un exemple de titre"`<br>`resultat = texte.title()`<br><br>`# Résultat : "Un Exemple De Titre"` | Convertit la première lettre de chaque mot en majuscule                                    |
| `upper()`      | `texte = "exemple"`<br>`resultat = texte.upper()`<br><br>`# Résultat : "EXEMPLE"` | Convertit une chaîne en majuscule |
