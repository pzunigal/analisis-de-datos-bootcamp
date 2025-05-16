numero1 = 70 # declaración de variable int
numero2 = 3.14 # declaración de variable float
booleano = False # declaración de variable bool
cadena = 'Hola Mundo' # declaración de variable string
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] # Tipo de dato compuesto lista
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} # Tipo de dato compuesto diccionario
frutas = ('guayaba', 'fresa', 'papaya') # Tipo de dato compuesto tupla
print(type(frutas)) # revisión de tipo de dato
print(ingredientes_pastel[2]) # acceso a un elemento de la lista
ingredientes_pastel.append('Mantequilla') # agregar un elemento a la lista
print(persona['nombre']) # acceso a un elemento del diccionario
persona['nombre'] = 'Kevin' # modificar un elemento del diccionario
persona['color_ojos'] = 'cafe' # agregar un elemento al diccionario
print(frutas[2]) # acceso a un elemento de la tupla

if numero1 > 45: # condicional if 
    print("Numero mayor") 
else: # condicional else
    print("Numero menor")

if len(cadena) < 5:
    print("Cadena corta")
elif len(cadena) > 15:
    print("Cadena larga")
else:
    print("Cadena perfecta")

for x in range(8):
    print(x)
for x in range(2,8):
    print(x)
for x in range(2,8,2):
    print(x)
x = 0
while(x < 8):
    print(x)
    x += 1

ingredientes_pastel.pop()
ingredientes_pastel.pop(1)

print(persona)
persona.pop('color_ojos')
print(persona)

for ingrediente in ingredientes_pastel:
    if ingrediente == 'Harina':
        continue
    print('Después de la primera sentencia')
    if ingrediente == 'Chocolate':
        break

def imprime_hola_10_veces():
    for numero in range(10):
        print('Hola')

imprime_hola_10_veces()

def imprime_hola_n_veces(n):
    for numero in range(n):
        print('Hola')

imprime_hola_n_veces(5)

def imprime_hola_n_o_diez_veces(n = 10):
    for numero in range(n):
        print('Hola')

imprime_hola_n_o_diez_veces()
imprime_hola_n_o_diez_veces(5)


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)