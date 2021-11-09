"""5) Escribir un programa que primero solicite una palabra al usuario y luego le permita al usuario ingresar 5 palabras.
El sistema deberá calcular cuántas y cuáles palabras de las 5 ingresadas pueden escribirse exactamente con las letras
de la palabra ingresada al principio (utilizando todas las letras y sin repetir ninguna).
Ej: Palabra inicial: CASO
5 palabras: MAMA, CLASE, SACO, COSA, PEPE
EL sistema deberá devolver 2 palabras (SACO y COSA)."""

def main():
    palabra: str = input("Palabra inicial: ")
    list(palabra.lower())
    lista: list = []
    cinco_palabras: str = input("5 palabras: ")
    lista_cinco_palabras: list = (cinco_palabras.split(", "))
    sorted(lista_cinco_palabras)
    for una_palabra in lista_cinco_palabras:
        list(una_palabra.lower())
        if sorted(una_palabra) == sorted(palabra):
            lista.append(una_palabra)
    tupla_a_regresar: tuple = tuple(lista)

    return tupla_a_regresar

print(main())