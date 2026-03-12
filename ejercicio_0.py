Vainilla = 0
Fresa = 0
Chocolate = 0

while (Vainilla + Fresa + Chocolate) <5: 
    eleccion = input("elige un sabor: " )
    if eleccion == "Vainilla":
        Vainilla += 1

    elif eleccion == "Fresa":
        Fresa += 1

    elif eleccion  == "Chocolate":
        Chocolate += 1

print("La cantidad de Vainilla es: ", Vainilla)
print("La cantidad de Fresa es: ", Fresa)
print("La cantidad de Chocolate es: ", Chocolate)