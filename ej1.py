# Escribir una función que recibe una cadena y un numero n 
# y devuelve la cadena eliminando los caracteres en todas 
# las posiciones multiplos de n, contando las posiciones desde 1.
# Ejemplo: con la cadena 'abcdefghijk' y n=3 debe devolver 'abdeghjk'

# Escribir debajo de este comentario el código del ejercicio

def eliminar_multiplos(cadena, n):
    return "".join([cadena[i: i+n-1] for i in range(0, len(cadena), n)])
    
    

# Pruebas

assert eliminar_multiplos('abcdefghijk', 3) == 'abdeghjk'
assert eliminar_multiplos('abcdefghijk', 12) == 'abcdefghijk'
