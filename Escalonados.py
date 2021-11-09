"""5) Números escalonados: Un número es escalonado, si sus dígitos están en orden estrictamente creciente.
Por ejemplo, 359 es escalonado, 34 también, pero 5674 no es, y tampoco 5667.
Se recibe un número entero por parámetro N > 10 (lo cual se debe validar).
La salida debe decir si es un número escalonado o no lo es y a continuación indicar la cantidad de dígitos cuya secuencia
fue escalonada.
Datos de entrada:
Se recibe un parámetro con el número entero N.
Datos de salida:
El programa debe imprimir por pantalla en una línea, conteniendo un único número: la cantidad de números
escalonados que hay entre 10 y N, inclusive.
Ejemplo1: Entrada: 359 - Salida: “Es escalonado”, 3
Ejemplo2: Entrada: 24893471 - Salida: “No es escalonada”, 4 """

def main(numero: int) -> None:
    maximo: int = 0
    contador: int = 0
    if numero > 10: 
        for digito in str(numero):
            if int(digito) > maximo:
                maximo = int(digito)
                contador += 1
        if len(str(numero)) == contador:
            print(f"Entrada: {numero} - Salida: 'Es escalonado', {contador}")
        else:
            print(f"Entrada: {numero} - Salida: 'No es escalonado', {contador}")

main(24893471)
