#Ingreso al cine segun la edad

precio_de_niños = 8000
precio_de_adultos = 12000
precio_de_mayores = 9000


edad = int(input("Por favor ingresa tu edad: "))
if edad < 12 : 
    total = precio_de_niños 
    print("el precio de tu entrada es de:", total )

elif 12 <= edad <= 59 :
    total = precio_de_adultos
    print("el precio de tu entrada es de:", total )

elif edad >= 60 :
    total = precio_de_mayores
    print("el precio de tu entrada es de:", total )
