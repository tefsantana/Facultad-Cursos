from math import pi
def parcialito1_1():
    grados_usuario = 0
    grados_usuario = float(input("Cuantos grados?: "))
    
    while True:

        if 0 <= grados_usuario <= 360:
            radianes = grados_usuario * (pi / 180)
            return (f"{grados_usuario}°, son {radianes} radianes.")
        
        else:
            grados_usuario = float(input("Ingrese nuevamente un valor válido de grados entre 0 y 360: "))
            continue

    
#print(parcialito1_1())

def IPv4():
    IPv4 = input("Ingrese una dirección IPv4: ")
    ip = IPv4.split(".")
    while len(ip) != 4:            #0.0.0.0 --> 3 "." y 4 num
        IPv4 = input("Ingrese una dirección IPv4: ")
        ip = IPv4.split(".")
    for i in range(len(ip)):
        while not(1 <= len(ip[i]) <= 3) or not (0 <= int(ip[i]) <= 255):
            IPv4 = input("Ingrese una dirección IPv4: ")
    return IPv4

#print(IPv4())

#2) Escribir una función que reciba una cadena y un numero N y devuelva su encriptación en formato rotN. Para encriptar una cadena con rotN se debe reemplazar cada caracter por el caracter que se encuentra a N posiciones de distancia hacia la "derecha" en el abecedario. Asumir que la cadena incluye unicamente las 26 letras del alfabeto inglés en minúscula (la ñ no está incluída). N es un número entero que puede ser positivo o negativo. El abecedario es circular, es decir, luego de la "z" vuelva a empezar desde la "a" nuevamente.
#Ayuda: usar la constante ascii_lowercase del módulo string que contiene una cadena con las 26 letras en minúscula: "abcd...xyz".

#Ejemplo:
#rotN("abcde", 1) -> "bcdef"
#rotN("bcdef", -1) -> "abcde"
#rotN("zambia", 13) -> "mnzovn"
#rotN("mnzovn", -13) -> "zambia"
#rotN("mnzovn", 39) -> "zambia"
 

from string import ascii_lowercase

def encriptar_rotn(cadena, n):
    aux = ""
    for i in range(len(cadena)):
        indice = ascii_lowercase.index(cadena[i])
        aux += ascii_lowercase[(indice + n) % len(ascii_lowercase)]
    return aux

#print(encriptar_rotn("abcde", 1))
#print(encriptar_rotn("zambia", 13))
#print(encriptar_rotn("mnzovn", -13))

def cadena_con_rot13(cadena, n):
    lista_abecedario = list(ascii_lowercase)
    cadena_rot = ""
    for caracteres in cadena:
        #if not caracteres in lista_abecedario:
            #return ""
        cadena_rot += lista_abecedario[(lista_abecedario.index(caracteres) + n) % len(lista_abecedario)]
    return cadena_rot


def diferencia_listas(lista1, lista2):
    lista_nueva = []
    for elemento in lista1:
        if elemento not in lista2:
            lista_nueva.append(elemento)
    print(lista_nueva)

#diferencia_listas([15,49], [6,31])
#diferencia_listas([2,3,1,5], [2,5])

"BÚSQUEDA BINARIA"
# x = elemento a buscar  ; lista = lista donde se busca con elementos ordenados.
def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) + 1
    while izq <= der:
        medio = (izq + der) // 2
        #print(f"{medio} { lista[medio]}")
        if lista[medio] == x:
            return medio
        if k(lista[medio]) > k(x):
            der = medio - 1
        else:
            izq = medio + 1
    return -1


