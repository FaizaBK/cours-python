def calculatrice(a: float, b: float, operator: str) -> float | None:
    try:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b  # raise ZeroDivisionError si b == 0
        else:
            print("Erreur : Veuillez entrer une opération valide.")
    except ZeroDivisionError as zero_division_exception:
        print(zero_division_exception)

try:
    nombre1 = float(input("Entrez le premier nombre : "))
    nombre2 = float(input("Entrez le deuxième nombre : "))
    operator = str(input("Entrez le signe du nombre : "))
    resultat = calculatrice(nombre1, nombre2, operator)
    if resultat:
        print(f"Le résultat de {nombre1} {operator} {nombre2} = {resultat}")
except ValueError:
    print("Erreur : Veuillez entrer des paramètres valides.\nLes nombres sont des floats ou des int.")