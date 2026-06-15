nombre1 = int(input("Choisissez nombre1 : "))
nombre2 = int(input("Choisissez nombre2 : "))

def addition(nombre1, nombre2):
    print(nombre1 + nombre2)

def multiplication(nombre1, nombre2):
    print(nombre1 * nombre2)

def soustraction(nombre1, nombre2):
    print(nombre1 - nombre2)

def division(nombre1, nombre2):
    print(nombre1 / nombre2)

def menu():
    print("Choisissez une opération :")
    print("1. addition")
    print("2. multiplication")
    print("3. soustraction")
    print("4. division")
    return input("Entrez le numéro :")
while True:
    choix = menu()

    if choix == "1":
        addition(nombre1, nombre2)
        break
    elif choix == "2":
        multiplication(nombre1, nombre2)
        break
    elif choix == "3":
        soustraction(nombre1, nombre2)
        break
    elif choix == "4":
        if nombre2 == 0:
            print("Erreur division par zéro impossible")
        else:
            division(nombre1, nombre2)
        break
    else:
        print("Choix invalide, réessayez.")
        break