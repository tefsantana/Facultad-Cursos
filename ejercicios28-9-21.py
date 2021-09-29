"""
Ejercicio 1:
a) Crear un programa que permita al usuario ingresar un número e
indicar si es un número deficiente. Un número es deficiente cuando
es MAYOR a la suma de todos sus divisores propios (exceptuándose
así mismo).
Por ejemplo:
14 es un número deficiente porque sus divisores
son: 1,2,7 → 10 < 14.
"""

numero: int = int(input("Ingrese un número: "))
posible_divisor: int = 0                                    
suma_divisores: int = 0                                   

for posible_divisor in range(1, numero):
    if ((numero % posible_divisor) == 0):
        suma_divisores = suma_divisores + posible_divisor

if (numero > suma_divisores):
    print("Es un número deficiente.")
else:
    print("Es un número eficiente.")

"""
b) Crear un programa que permita al usuario ingresar un número e
indicar si es un número abundante. Un número es abundante cuando
es MENOR a la suma de todos sus divisores propios (exceptuándose
así mismo).
Por ejemplo:
12 es un número abundante porque sus divisores
son: 1,2,3,4,6 → 16 > 12.
"""

numero: int = int(input("Ingrese un número: "))
posible_divisor: int = 0
suma_divisores: int = 0

for posible_divisor in range(1, numero):
    if ((numero % posible_divisor) == 0):
        suma_divisores = suma_divisores + posible_divisor

if (numero < suma_divisores):
    print("Es un número abundante.")
else:
    print("Es un número no abundante.")


"""
c) Crear un programa que permita al usuario ingresar un número e
indicar si es un número perfecto. Un número es perfecto cuando es
IGUAL a la suma de todos sus divisores propios (exceptuándose así
mismo).
Por ejemplo:
6 es un número perfecto porque sus divisores
son: 1,2,3 → 6 = 6.
"""

numero: int = int(input("Ingrese un número: "))
posible_divisor: int = 0
suma_divisores: int = 0

for posible_divisor in range(1, numero):
    if ((numero % posible_divisor) == 0):
        suma_divisores = suma_divisores + posible_divisor

if (numero == suma_divisores):                            
    print("Es un número perfecto.")
else:
    print("Es un número no perfecto.")


"""
d) Extra: Tomar uno de los incisos anteriores y verificar la condición
pedida para todos los números en un intervalo (1, 𝑛] donde 𝑛 es un
número ingresado por el usuario.
"""

numero: int = int(input('Ingresar número: '))            
suma_divisores: int = 0

for n in range(1, numero + 1):    

	suma_divisores: int = 0

	for posible_divisor in range(1, n) :       

		if (n % posible_divisor) == 0 :
			suma_divisores += posible_divisor

	if n > suma_divisores:
		print(f'El número {n} es deficiente')

	elif n == suma_divisores :
		print(f'El número {n} es perfecto')

	else:
		print(f'El número {n} es abundante')







    
