ccono = 0
cvaso = 0
cbanana = 0


act = True
cadena = ""
cliente = 0


while act:
    opcion = input("desea registrar un nuevo cliente?\n si,no: ")
    if opcion == "si":
        cliente += 1
        producto = input("Escoge el producto: cono, vaso, bananasplit:")
        cantidad = int(input(f"Digite la cantidad de {producto} a comprar: "))
        if producto == "cono":
            ccono += 1
            total = 3000 * cantidad

        elif producto == "vaso":
            cvaso += 1
            total = 4000 * cantidad

        elif producto == "bananasplit":
            cbanana += 1
            total = 4000 * cantidad
        
        cadena = f"el cliente paga ${total} pesos" 

    else:
        act = False
        continue

    print(cadena)
else:
    print(f"En total se registraron {cliente} clientes")


