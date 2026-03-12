cont_vainilla = 0 #contador de vainilla
cont_fresa = 0 #contador de fresa
cont_chocolate = 0 #contador de chocolate

for i in range(0,5,1):
    entrada = input("Selecciona un sabor: ")
    if entrada == "vainilla":
        cont_vainilla += 1

    elif entrada == "fresa":
        cont_fresa += 1

    elif entrada == "chocolate":
        cont_chocolate += 1

print("La cantidad de vainilla es: ", cont_vainilla)
print("La cantidad de fresa es: ", cont_fresa)
print("La cantidad de chocolate es: ", cont_chocolate)

