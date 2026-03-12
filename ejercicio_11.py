ccono = 0
cvaso = 0
cbanana = 0


act = True
cadena = ""
cliente = 0

while(act) :
    producto = (input("Escoge el producto: cono, vaso, bananasplit:"))

    if producto == "cono" :
        ccono+=1
        cliente+=1

    elif producto == "vaso" :
        cvaso+=1
        cliente+=1

    elif producto == "bananasplit" :
        cbanana+=1
        cliente+=1
        

    ag = (input("Desea agregar otro cliente: "))
    if ag == "1" :
        total = ccono*3000 + cvaso*4000 + cbanana*4000 
    else:
        act = False
        continue
       
    cadena = f"el cliente Nro {cliente} paga {total} pesos" 
    print(cadena)
else: print("ya no mas pedidos")


