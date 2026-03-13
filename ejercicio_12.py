bajo = 0
medio = 0
alto = 0

for i in range(5):
    nombre = input("Nombre: ")
    dias = int(input("Días asistidos en la semana: "))

    if dias < 3:
        print("Bajo compromiso")
        bajo += 1
    elif dias <= 4:
        print("Compromiso medio")
        medio += 1
    else:
        print("Compromiso alto")
        alto += 1

print("Personas con bajo compromiso:", bajo)
print("Personas con compromiso medio:", medio)
print("Personas con alto compromiso:", alto)