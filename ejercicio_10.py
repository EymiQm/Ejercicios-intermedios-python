# Preguntar cantidad de clases asistidas
clases = int(input("¿Cuántas clases asististe este mes? "))

# Condicionales para clasificar la asistencia
if clases < 5:
    print("Tu asistencia es baja.")
elif 5 <= clases <= 8:
    print("Tu asistencia es media.")
else:  # significa 9 o más
    print("Tu asistencia es alta.")