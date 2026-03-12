#Parqueadero cobro por horas

#Valor primera hora: 5000
#Valor hora adicional: 3000


horas = int(input("Ingrese cuántas horas estuvo el carro: "))

if horas == 1:
    total = 5000
else:
    total = 5000 + (horas - 1) * 3000

print("Total a pagar:", total)