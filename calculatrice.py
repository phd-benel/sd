def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : division par zéro"
    return a / b

def menu():
    print("=== Calculatrice ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")

while True:
    menu()
    choix = input("Choisis une opération (1-5) : ")

    if choix == "5":
        print("Au revoir !")
        break

    try:
        a = int(input("Entrez le 1er nombre : "))
        b = int(input("Entrez le 2e nombre : "))

        if choix == "1":
            print("Résultat :", addition(a, b))
        elif choix == "2":
            print("Résultat :", soustraction(a, b))
        elif choix == "3":
            print("Résultat :", multiplication(a, b))
        elif choix == "4":
            print("Résultat :", division(a, b))
        else:
            print("Choix invalide.")
    except ValueError:
        print("Erreur : veuillez entrer uniquement des nombres.")