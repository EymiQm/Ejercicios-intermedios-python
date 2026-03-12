#Ingreso por edad al Gym

edad = int(input("Por favor ingrese una edad: "))
if edad <13 :
    print("No puedes ingresar")
elif 13 <= edad <=17:
    print("Haces parte de la clase 'juvenil'")
elif 18<= edad <=19:
    print("Haces parte de la clase 'general'")
elif edad >=60 : 
    print("Haces parte de la clase 'senior'")
