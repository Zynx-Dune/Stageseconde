nombre = 1
while nombre<=20:
    nombre = nombre*7
    print(str(nombre))
    if nombre%3 == 0:
        print("*")
    nombre=nombre/7
    nombre=nombre + 1