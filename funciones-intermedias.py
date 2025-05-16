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

matriz[1][0] = 6
print(matriz)

cantantes[0]["nombre"] = "Enrique Martin Morales"

ciudades["México"][2] = "Monterrey"
print(ciudades)

coordenadas[0]["latitud"] = 9.9355431

print("\n")
def iterarDiccionario(cantantes):
    for diccionario in cantantes: 
        elementos = []
        for clave, valor in diccionario.items():
            elementos.append(f"{clave}: {valor}")
        print(", ".join(elementos))

iterarDiccionario(cantantes)

print("\n")
def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        print(diccionario.get(llave))

print("Nombres: ")
iterarDiccionario2("nombre", cantantes)
print("\nPaises:")
iterarDiccionario2("pais", cantantes)

costa_rica = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

