# Programa en Python. Autor: profesor Martín Maulhardt, FIUBA
 
print("Programa que determina si las relaciones son reflexivas, simétricas y transitivas")
print("Matemática Discreta -FIUBA 2020")
 
 
# La matriz dentro del programa
matriz = [ 
  [1,0,0,0],
  [0,1,0,0],
  [0,0,1,0],
  [0,0,0,1],
]
reflexiva = True
simétrica = True
transitiva = True
 
# el loop de la reflexiva: O(n).
# Notemos que entra en el if si y solo si hay un cero en la posición [i][i] negando la reflexiva.
# Solo en ese caso la variable booleana reflexiva cambia su valor a false
for i in range (0,len(matriz[0])):
    if matriz[i][i] == 0:
        reflexiva = False
    i += 1
 
# el loop doblemente anidado de la simétrica: O(n^2).
# Notemos que entra en el if si y solo si hay una entrada [j][k] diferente de la entrada[k][j].
# Solo en ese caso la variable booleana simétrica cambia su valor a false
for j in range (0,len(matriz[0])):
    for k in range (0,len(matriz[0])):
        if matriz[j][k] != matriz [k][j]:
            simétrica = False
        k += 1
    j += 1
# el loop triplemente anidado de la transitiva: O(n^3).
# Notemos que entra en el if si y solo si hay una entrada [l][n] y simultáneamente [n][m] iguales a 1
# y además la entrada [l][m]=0. Esto indica lRn, nRm pero l (noR) m negando la transitiva.
# Solo en ese caso la variable booleana transitiva cambia su valor a false.
 
for l in range (0,len(matriz[0])):
    for m in range (0,len(matriz[0])):
        for n in range (0,len(matriz[0])):
            if matriz[l][n] == matriz[n][m] == 1 and matriz[l][m] == 0:
                transitiva = False
            n += 1
        m += 1
    l += 1
 
# Impresión de los resultados
 
print(matriz)
print("Reflexiva: ",reflexiva)
print("Simétrica: ",simétrica)
print("Transitiva: ",transitiva)