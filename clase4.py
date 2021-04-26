def es_par(n):
    return n % 2 == 0

def es_primo(n):
    """Dado un número entero n, indica si es primo o no."""
    for i in range (2,n):
        if n % i == 0:
            # o sea que no tiene resto, su resto es 0
            return False
    return True

def abs(n):
    """Escribir una implementación propia de la función abs que devuelva el valor absoluto de cualquier valor que reciba."""
    if n < 0:
        return -n
    return n

# Año bisiesto es si es divisible por 4 y no por 100

def es_bisiesto(anio):
    if anio % 4 != 0:
        return False
    if anio % 100 == 0 and anio % 400 != 0:
        return False
    return True

def es_bisiesto1(anio):
    if anio % 4 == 0 or (anio % 100 == 0 and anio % 400 != 0):
        return False
    return True

def es_bisiesto2(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

# Suponiendo que el 1er día del año fue lunes, escribir una función que reciba un num con el día del año (de 1 a 366) y le devuelva el día de la semana que le toca.
# Ej: Si recibe "3", debe devolver "miércoles", si recibe "9", debe devolver "martes".

def dia_semana(dia):
    dia = dia % 7
    if dia == 1:
        return 'Lunes'
    elif dia == 2:
        return 'Martes'
    elif dia == 3:
        return 'Miércoles'
    elif dia == 4:
        return 'Jueves'
    elif dia == 5:
        return 'Viernes'
    elif dia == 6:
        return 'Sábado'
    elif dia == 7:
        return 'Domingo'
    
print(dia_semana(8))

# EJERCICIO DE PARCIAL --> 4.3 DE LA GUÍA

# Ejercicio 4.3. Escribir una función que reciba por parámetro una dimensión n, e imprima la matriz identidad correspondiente a esa dimensión.

# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

def imprimir_matriz_identidad():
    for i in range(n): # de 0 a n, o sea se ejecuta n veces
        for j in range(n): # de 0 a n, o sea se ejecuta n veces
            print (0)


