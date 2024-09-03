#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fichier de correction de TP python impératif pour Diginamic

À l'aide du module csv uniquement, exploiter les données du fichier titanic_survival.csv situé dans le dossier "Annexes".
Itérer sur les données et montrer les résultats suivants.

Q1 : Moyenne d'âge des passagers (~30 ans)
Q2 : Pourcentage de survie par classe de passager (1ere classe: ~62%, 2nd classe: ~43%, 3eme classe: ~26%)
Q3 : Le bateau de sauvetage ayant sauvé le plus de passagers (bateau n°13 avec 39 passagers sauvés)
"""


import csv
from typing import Dict

# INITIALISATION DE L'ENVIRONNEMENT ET DES VARIABLES

# Ouvrir le fichier CSV avec encodage UTF-8 pour prendre en charge les caractères spéciaux.
# Le fichier 'titanic_survival.csv' doit se trouver dans le même répertoire que ce script.
with open("titanic_survival.csv", encoding="utf-8") as csvfile:
    # Créer un lecteur CSV pour parcourir les lignes.
    reader = csv.reader(csvfile, delimiter=",")

    # Ignorer la première ligne contenant les en-têtes du CSV.
    next(reader)

    # Initialiser les variables pour le calcul de la moyenne d'âge.
    total_age: float = 0
    ligne_count: int = 0

    # Initialiser les variables pour le calcul de survie par classe.
    class_counts: Dict[int, Dict[str, int]] = {
        1: {"total": 0, "survived": 0},
        2: {"total": 0, "survived": 0},
        3: {"total": 0, "survived": 0},
    }

    # Initialiser les variables pour le bateau qui a sauvé le plus de personnes.
    bateau_dict: Dict[str, int] = {}

    # LOGIQUE FONCTIONNELLE DU PROGRAMME

    # Parcourir le CSV.
    for row in reader:
        # Récupérer les données de la ligne actuelle.
        pclass: int = int(row[0]) if row[0].isdigit() else 0
        survived: int = int(row[1]) if row[1].isdigit() else 0
        age: float = float(row[4]) if row[4] != "" else 0
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

    # Calculer la moyenne d'âge et l'afficher.
    moyenne_age: float = total_age / ligne_count
    print(f"Moyenne d'âge : {moyenne_age:.2f}")

    # Calculer le pourcentage de survie par classe et l'afficher.
    for pclass, counts in class_counts.items():
        total: int = counts["total"]
        survived: int = counts["survived"]
        survival_percentage: float = (survived * 100) / total if total > 0 else 0
        print(f"Survie de la classe {pclass} : {survival_percentage:.2f}%")

    # Supprimer le champ vide avec les personnes qui n'ont pas pu être sauvées.
    del bateau_dict[""]
    # Trouver la clé avec la plus grande valeur
    cle_max: str = max(bateau_dict, key=bateau_dict.get)
    # Afficher la clé avec la plus grande valeur
    print(
        f"Le bateau qui a sauvé le plus de monde est {cle_max} avec un total de {bateau_dict[cle_max]} personnes sauvées."
    )
