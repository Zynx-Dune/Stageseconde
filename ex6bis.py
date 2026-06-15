def somme(a, b):
    print(a + b)

def produit(a, b):
    print(a * b)

def difference(a, b):
    print(a - b)

def quotient(a, b):
    print(a / b)

while True:
    print("Choisissez une opération :")
    print("1. Somme")
    print("2. Produit")
    print("3. Différence")
    print("4. Quotient")
    print("5. Quitter")

    choix = input("Votre choix : ")

    if choix == "5":
        print("Au revoir !")
        break

    if choix not in ["1", "2", "3", "4"]:
        print("Choix invalide.")
        continue

    nombre1 = int(input("Choisissez nombre1 : "))
    nombre2 = int(input("Choisissez nombre2 : "))

    if choix == "1":
        somme(nombre1, nombre2)

    elif choix == "2":
        produit(nombre1, nombre2)

    elif choix == "3":
        difference(nombre1, nombre2)

    elif choix == "4":
        if nombre2 == 0:
            print("Erreur, impossible de diviser par zéro.")
        else:
            quotient(nombre1, nombre2)