# Elegir un servicio

servicio_elegido = input("¿que servicio deseas? (masaje, facial, manicure): ").lower()

# Condicionales con elif para cada servicio

if servicio_elegido == "masaje":
    print("Perfecto el servicio de masaje está disponible.")
elif servicio_elegido == "facial":
    print("Genial, el servicio de facial está disponible.")
elif servicio_elegido == "manicure":
    print("Excelente el servicio de manicure está disponible.")
else:
    print(f"Lo sentimos, el servicio de {servicio_elegido} no está disponible.")