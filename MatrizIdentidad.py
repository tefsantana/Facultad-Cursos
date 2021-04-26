# EJERCICIO DE PARCIAL --> 4.3 DE LA GUÍA

# Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.

# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

def imprimir_matriz_identidad(n):
    for columna in range(n): # de 0 a n, o sea se ejecuta n veces
        for fila in range(n): # de 0 a n, o sea se ejecuta n veces
            if columna == fila:
                print(1, end= ' ')
            else:
                print (0, end= ' ')
        print()

imprimir_matriz_identidad(3)