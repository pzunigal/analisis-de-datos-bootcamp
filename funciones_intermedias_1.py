matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Actualiza los valores en diccionarios y listas
matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431

# Crea la función iterarDiccionario(lista)
print("\n")
def iterarDiccionario(lista):
    for diccionario in lista: 
        elementos = []
        for clave, valor in diccionario.items():
            elementos.append(f"{clave}: {valor}")
        print(", ".join(elementos))

iterarDiccionario(cantantes)

# Crea la función iterarDiccionario2(llave, lista)
print("\n")
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))

print("Nombres: ")
iterarDiccionario2("nombre", cantantes)
print("\nPaises:")
iterarDiccionario2("pais", cantantes)

chile = {
    "ciudades": ["Santiago", "Concepcion", "Temuco", "Valdivia"],
    "comidas": ["Completo", "Asado", "Casuela", "Empanada" , "Pastel de Choclo"],
}

# Crea la función imprimirInformacion(diccionario)
print("\n")
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"\n{len(lista)} {clave.upper()}")

        for item in lista:
            print(item)

imprimirInformacion(chile)