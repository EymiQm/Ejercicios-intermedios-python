cafe = 4000
te = 3500
jugo = 5000

print("1. cafe - 4000$")
print("2.  te - 3500$")
print("3. jugo - 5000$")

opcion = int(input("seleccione un producto: "))
selecciona = int(input("Cuantas unidades quieres: "))

if opcion == 1: 
    opcion = 4000
    print("seleecionaste cafe")

elif opcion == 2:
    opcion = 3500
    print("seleecionaste cafe")
elif opcion == 3:
    opcion = 5000
    print("seleecionaste cafe")

total = opcion * selecciona
print("El total es: ", total)