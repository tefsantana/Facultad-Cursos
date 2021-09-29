"""
Ejercicio 3:
Crear una calculadora de 4 funcionalidades (+, −, /, ∗). Donde se le
pregunte al usuario que operación desea realizar y luego preguntarle por
dos números para realizar dicha operación. También debe de haber una
opción para cerrar el programa.
"""

mantener_programa_abierto: bool = True

while mantener_programa_abierto:
    respuesta_del_usuario = input("""
OPERACIONES:
1: SUMA
2: RESTA
3: MULTIPLICACIÓN
4: DIVISIÓN
5: SALIDA

Ingrese una opción: """)

    if respuesta_del_usuario == "5":
        print("Cerrando programa")
        mantener_programa_abierto = False
        
    elif respuesta_del_usuario == "1":
        numero1: int = int(input("Ingrese el primer número: "))
        numero2: int = int(input("Ingrese el segundo número: "))
        print(f"El resultado es {numero1 + numero2}")

    elif respuesta_del_usuario == "2":
        numero1: int = int(input("Ingrese el número al que se le va a restar el segundo: "))
        numero2: int = int(input("Ingrese el número que se restará con el primero: "))
        print(f"El resultado es {numero1 - numero2}")

    elif respuesta_del_usuario == "3":
        numero1: int = int(input("Ingrese el primer número: "))
        numero2: int = int(input("Ingrese el segundo número: "))
        print(f"El resultado es {numero1 * numero2}")
    
    elif respuesta_del_usuario == "4":
        numero1: float = float(input("Ingrese el número dividendo: "))
        numero2: float = float(input("Ingrese el número divisor: "))
        print(f"El resultado es {numero1 / numero2}")
    
    else:
        respuesta_del_usuario = input("Número incorrecto, ingrese otro: ")