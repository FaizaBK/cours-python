### Exercice : Citations d'un écrivain

---

```Python
from collections import Counter  
from quote import quote  
import re  

# LOGIQUE FONCTIONNELLE
def get_citations(author, limit=30):
	"""
	Permet d'avoir les citations de l'auteur {author} en quantité égale à {limit}
	"""
    return quote(author, limit=limit)  
  
  
def get_sorted_titles(citations):
	"""
	Trie la fréquence d'appartion des titres des citations dans l'ordre décroissant
	"""
    titles = [quote["book"] for quote in citations]  
    title_counts = Counter(titles)  
    sorted_titles = sorted(title_counts.items(), key=lambda x: x[1], reverse=True)  
    return [(title, count) for title, count in sorted_titles if title != ""]  
  
  
def get_sorted_words(citations, min_frequency=5):
	"""
	Trie la fréquence d'appartion des mots des citations dans l'ordre décroissant
	"""
    quotes = [quote["quote"] for quote in citations]  
    all_quotes = " ".join(quotes)  
    words = re.findall(r'\w+', all_quotes.lower())  
    word_counts = Counter(words)  
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)  
    return [(word, count) for word, count in sorted_words if count >= min_frequency]  

  
def display_titles(sorted_titles) -> None:
	"""
	Méthode d'affichage des titres
	"""
    for title, count in sorted_titles:  
        print(f"Titre : {title}, Fréquence : {count}")  
  
  
def display_words(sorted_words) -> None:
	"""
	Méthode d'affichage des mots
	"""
    for word, count in sorted_words:  
        print(f"Mot : {word}, Fréquence : {count}")


# AFFFICHAGE DES RESULTATS
# Définitions des variables  
author = "Edgar Allan Poe"  
  
# Obtenir les citations  
citations = get_citations(author)  
  
# Obtenir et afficher les titres triés par fréquence  
sorted_titles = get_sorted_titles(citations)  
display_titles(sorted_titles)  
  
# Obtenir et afficher les mots triés par fréquence  
sorted_words = get_sorted_words(citations)  
display_words(sorted_words)
```

<br>
<br>
<br>

### Exercice : Titanic

---

```python
import csv  
from typing import Dict  
  
# INITIALISATION DE L'ENVIRONNEMENT ET DES VARIABLES  
  
# Ouvrir le fichier CSV avec encodage UTF-8 pour prendre en charge les caractères spéciaux.  
# Le fichier 'titanic_survival.csv' doit se trouver dans le même répertoire que ce script.  
with open('titanic_survival.csv', encoding='utf-8') as csvfile:  
    # Créer un lecteur CSV pour parcourir les lignes.  
    reader = csv.reader(csvfile, delimiter=';')  
  
    # Ignorer la première ligne contenant les en-têtes du CSV.  
    next(reader)  
  
    # Initialiser les variables pour le calcul de la moyenne d'âge.  
    total_age: float = 0  
    ligne_count: int = 0  
  
    # Initialiser les variables pour le calcul de survie par classe.  
    class_counts: Dict[int, Dict[str, int]] = {1: {"total": 0, "survived": 0}, 
                                            2: {"total": 0, "survived": 0},  
                                            3: {"total": 0, "survived": 0}}  
  
    # Initialiser les variables pour le bateau qui a sauvé le plus de personnes.  
    bateau_dict: Dict[str, int] = {}  
  
    # LOGIQUE FONCTIONNELLE DU PROGRAMME  
  
    # Parcourir le CSV.
    for row in reader:  
        # Récupérer les données de la ligne actuelle.  
        pclass: int = int(row[0]) if row[0].isdigit() else 0  
        survived: int = int(row[1]) if row[1].isdigit() else 0  
        age: float = float(row[4]) if row[4] != '' else 0  
        bateau: str = row[11]  
  
        # Calcul de l'âge total.  
        if age:  
            total_age += age  
            ligne_count += 1  
  
        # Logique pour la survie par classe.  
        if pclass in class_counts:  
            class_counts[pclass]["total"] += 1  
            if survived == 1:  
                class_counts[pclass]["survived"] += 1  
  
        # Logique du bateau.  
        if bateau in bateau_dict:  
            bateau_dict[bateau] += 1  
        else:  
            bateau_dict[bateau] = 1  
  
    # AFFICHAGE DES RÉSULTATS  
  
    # Calculer la moyenne d'âge et l'afficher.    moyenne_age: float = total_age / ligne_count  
    print(f"Moyenne d'âge : {moyenne_age:.2f}")  
  
    # Calculer le pourcentage de survie par classe et l'afficher.  
    for pclass, counts in class_counts.items():  
        total: int = counts["total"]  
        survived: int = counts["survived"]  
        survival_percentage: float = (survived * 100) / total if total > 0 else 0  
        print(f"Survie de la classe {pclass} : {survival_percentage:.2f}%")  
  
    # Supprimer le champ vide avec les personnes qui n'ont pas pu être sauvées.  
    del bateau_dict['']  
    # Trouver la clé avec la plus grande valeur  
    cle_max: str = max(bateau_dict, key=bateau_dict.get)  
    # Afficher la clé avec la plus grande valeur  
    print(f"Le bateau qui a sauvé le plus de monde est {cle_max} avec un total de {bateau_dict[cle_max]} personnes sauvées.")
```

<br>
<br>
<br>

### Exercice supplémentaire : approfondissement de `quote`

---

```Python
from quote import quote  
import re  
import csv  
  
# Liste des auteurs  
authors = [  
    "Edgar Allan Poe",  
    "Victor Hugo",  
    "Gustave Flaubert",  
    "Ernest Hemingway",  
    "Agatha Christie",  
    "Friedrich Nietzsche",  
    "Arthur Schopenhauer",  
    "Simone De Beauvoir",  
    "Guy De Maupassant",  
    "Voltaire",  
    "Emile Zola",  
    "Georges Orwell",  
    "Frank Herbert",  
    "Isaac Asimov",  
    "Tolkien",  
    "William Shakespeare"  
]  
  
  
def count_the_in_citations(citations):  
    # Compte le nombre d'occurrences du mot "the" dans les citations  
    total_the_count = 0  
    for citation in citations:  
        total_the_count += citation["quote"].lower().count("the")  
    return total_the_count  
  
  
def get_authors_ranking_by_the_usage():  
    # Crée un dictionnaire pour stocker le nombre d'occurrences de "the" par auteur  
    the_counts = {}  
  
    # Obtenir le nombre d'occurrences de "the" pour chaque auteur  
    for author in authors:  
        citations = quote(author, limit=30)  
        the_counts[author] = count_the_in_citations(citations)  
  
    # Trier les auteurs par le nombre d'occurrences de "the" (classement décroissant)  
    sorted_authors = sorted(the_counts.items(), key=lambda x: x[1], reverse=True)  
  
    return sorted_authors  
  
  
def commons_author_words():  
    # Créer un ensemble pour stocker les mots en commun  
    common_words = set()  
  
    # Générer des citations pour chaque auteur et ajouter les mots à l'ensemble  
    for author in authors:  
        citations = quote(author, limit=30)  
        author_words = set()  
        for citation in citations:  
            words = re.findall(r'\w+', citation["quote"].lower())  
            author_words.update(words)  
        if not common_words:  
            common_words = author_words  
        else:  
            common_words = common_words.intersection(author_words)  
    return common_words  
  
  
def print_authors_ranking(sorted_authors):  
    print("Classement des auteurs par le nombre d'occurrences de 'the' :")  
    for author, count in sorted_authors:  
        print(f"Auteur : {author}, Occurrences de 'the' : {count}")  
  
  
def write_authors_ranking_to_csv(sorted_authors):  
    with open("authors_ranking.csv", mode="w", newline="") as csvfile:  
        fieldnames = ["auteur", "nombre d'occurrences du mot 'the'"]  
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)  
        writer.writeheader()  
        for author, count in sorted_authors:  
            writer.writerow({"auteur": author, "nombre d'occurrences du mot 'the'": count})  
  
  
# Exécution des fonctions  
# Exercice 1  
common_words = commons_author_words()  
print(common_words)  
  
# Exercice 2  
sorted_authors = get_authors_ranking_by_the_usage()  
print_authors_ranking(sorted_authors)  
  
# Exercice 3  
write_authors_ranking_to_csv(sorted_authors)
```
