# Escribir una funcion `dar_vuelta` que reciba una lista de tuplas de numeros y que 
# devuelva una nueva lista de tuplas, donde la primer tupla tendra el primer elemento 
# de todas las tuplas originales; la segunda, los segundos, etc.

# Ejemplo: 
# [(1,2,3), (4,5), (6,), (7,8,9,10)]
#   => 
# [(1,4,6,7), (2,5,8), (3,9), (10,)]

# Nota: las tuplas originales no tienen todas la misma cantidad de elementos entre sí.
# Ayuda: Una tupla de un solo elemento se puede crear de la forma `t = (elem,)`

# Escribir debajo de este comentario el código del ejercicio

#def dar_vuelta(lista_tuplas):
    #lista_nueva = []
    #for tupla in range(len(lista_tuplas)):
        #lista_nueva.append(lista_tuplas[0])
    #return lista_nueva


def dar_vuelta(matriz):
    lista_nueva = []
    i = 0
    while True:
        nueva_fila = []
        for fila in matriz:
            if len(fila) < i + 1:
                continue
            nueva_fila.append(fila[i])
        if not nueva_fila:
            break
        lista_nueva.append(tuple(nueva_fila))
        i += 1
    return lista_nueva


def dar_vuelta2(tuplas):
    resultado = [[] for i in range(len(max(tuplas, key= len)))]
    for tupla in tuplas:
        for i in range(len(tupla)):
            resultado[i].append(tupla[i])
        return list(map(tuple, resultado))
        
# Pruebas

l_inicial = [(1,2,3), (4,5), (6,), (7,8,9,10)]
l_esperada = [(1,4,6,7), (2,5,8), (3,9), (10,)]
l_resultado = dar_vuelta(l_inicial)

for i in range(len(l_esperada)):
    assert list(l_esperada[i]) == list(l_resultado[i])
