"""4) Se debe crear UNA FUNCION que reciba un string con números, separados por espacios y calcule el máximo, mínimo
y por último; la suma de todos los números. Deberá devolver una tupla con dichos valores.
El string deberá ser de este tipo: "2 76 5 43 5 7 8 23"
La tupla que devuelve debe ser: (76,2,169)
Ejemplifique con una llamada a dicha función desde el main o programa principal."""

def main(numeros: str) -> tuple:
    lista_numeros_str: list = numeros.split(" ")
    suma_numeros: int = 0
    lista_numeros_int  = list(map(int,numeros.split(' ')))
    maximo: int = max(lista_numeros_int)
    minimo: int = min(lista_numeros_int)
    suma_numeros = sum(lista_numeros_int)
    tupla_numeros: tuple = (maximo, minimo, suma_numeros)

    return tupla_numeros

print(main("2 76 5 43 5 7 8 23"))

