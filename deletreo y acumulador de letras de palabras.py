"""Dada una lista de palabras, se debe construir una función que construya un diccionario que contenga la 
cantidad de ocasiones en que se repite cada una de las letras en todas las palabras de la lista.
Ej: [‘auto’,’papa’,’cota’]
La función debe devolver {‘a’:4,’u’:1,’t’:2,’o’:2,’p’:2,’c’:1}
Haga un programa principal donde se ejemplifique su uso"""

def main(lista_de_palabras: list) -> dict:
    diccionario: dict = {}

    for palabra in lista_de_palabras:
        list(palabra)
        for letra in palabra:
            if letra in diccionario:
                diccionario[letra] += 1
            else:
                diccionario[letra] = 1
    return diccionario

print(main(["auto","papa","cota"]))