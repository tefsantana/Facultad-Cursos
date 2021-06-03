def imprimir_dos_primeros(cadena):
    """Dada una cadena de caracteres, imprime los dos primeros caracteres"""
    if len(cadena) < 2:
        return
    for i in range(2):
        print(cadena[i], end = '')
    print()

def imprimir_dos_primeros2(cadena):
    print(cadena[:2])

def imprimir_3_ultimos(cadena):
    print(cadena[-3:])

def imprimir_3_ultimos2(cadena):
    for i in range(len(cadena)-3, len(cadena)):
        print(cadena[i], end = '')
    print()

def imprimir_inverso(cadena):
    print(cadena[::-1])

