# Ejercicio 1
for i in range(101):
    print(i)

# Ejercicio 2
for numero in range(2, 501, 2):
    print(numero)

# Ejercicio 3
for i in range(1, 101):
    if i % 10 == 0:
        print("baby")
    elif i % 5 == 0:
        print("ice ice")
    else:
        print(i)

# Ejercicio 4
suma = 0
for i in range(0, 500001, 2):
    suma += i
    print(suma)


# Ejercicio 5
for i in range(2024, -1, -3):
    print(i)

# Ejercicio 6
numInicial = 3
numFinal = 10
multiplo = 2
print("Multiplos usando for:")
for numero in range(numInicial, numFinal + 1):
    if numero % multiplo == 0:
        print(numero)
