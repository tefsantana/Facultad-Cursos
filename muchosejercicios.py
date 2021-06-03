# Escribir una función que reciba dos secuencias y devuelva una lista con los elementos comunes a ambas, sin repetir ninguno. Ejemplo: f([7, 9, 7, 1], [6, 9, 7]) → [7, 9]

def funcion_comun(a, b):
    lista_final = []
    for i in a:
        if (i not in lista_final) and (i in b):
            lista_final.append(i)
    return lista_final    

# print(funcion_comun([7, 9, 7, 1], [6, 9, 7])) ----> FUNCIONA, devuelve [7, 9]


# Escribir un programa que le pida al usuario que ingrese letras pidiendolas de a una, hasta que ingrese una cadena vacía. Si ingresa algo que no es una letra, o ingresa más de una, debe ignorarse esta entrada. Luego debe imprimir todas las letras ingresadas en orden alfabético.
# Ejemplo: Se ingresa "g", "n", "a", "v", "1", "n", "p", "aa", "n"; se debe imprimir agnnnpv.

def letras_orden():
    lista_final =[]
    while True:
        letra = input("Ingrese solamente una letra: ")
        if (letra.isalpha() == True) and (len(letra) == 1):
            lista_final.append(letra)
            continue
        elif letra == "":
            print("".join(sorted(lista_final)))
            break

#print(letras_orden())

#Escribir una función que recibe una cadena y devuelve la cadena eliminando los caracteres repetidos consecutivos.

def sin_repetir(cadena):
    if not cadena:
        return ""

    nueva = cadena[0]

    for i in range(1, len(cadena)):
        if cadena[i] != cadena[i - 1]:
            nueva += cadena[i]
    
    return nueva

#assert sin_repetir("") == ""
#print(sin_repetir("aaabbaac"))

#Escribir una función que pida cadenas al usuario hasta que ingrese una cadena vacía. Debe devolver una lista de las palabras ingresadas.

def pedir_palabras():
    palabra = input("Cadena: ")
    resultado = ""
    while palabra:
        resultado += palabra
        palabra = input("Cadena: ")
    return resultado.split(" ")

# Basicamente esta función primero te pregunta que ingreses una cadena, y el resultado no tiene ninguna. Una vez que entra en el ciclo while al encontrar una palabra (palabra == True), el resultado va agregándose palabras cada vez que que ingreses una palabra mediante el input. Primero va resultado += palabra en el while ya que tiene que agregar la palabra del primer input. Ya en return, devuelve el resultado separando las palabras mediante cadena en una lista.
"""
Cadena: hola co
Cadena: mo e
Cadena: stas ?
Cadena:
"""
#print(pedir_palabras())

#Ejercicio random: hacer una lista

def hacer_lista():
    elemento = input("Ingrese una palabra: ")
    lista = []
    while elemento:
        lista.append(elemento)
        elemento = input("Ingrese otra palabra: ")
    return lista

#print(hacer_lista())

#Escribir una función que dado un número entero n mayor a 0 y una lista de números enteros, devuelva una nueva lista con los divisores de n que se encuentren en la primera. Si n no cumple las condiciones pedidas, debe devolver una lista vacía. Ejemplo: f([1, 7, 2, -4, 6, 9], 8) → [1, 2, -4]

def lista_divisora(lista, n):
    lista_divisores_n = []
    if n > 0 and int(n):
        for numeros in lista:
            if n % numeros == 0:
                lista_divisores_n.append(numeros)
        return lista_divisores_n
                    
    else:
        return []
           

#print(lista_divisora([1, 7, 2, -4, 6, 9], 8))


#Escribir una función que reciba dos cadenas, texto y palabra, y devuelva una cadena igual a texto pero con todas las ocurrencias de palabras censuradas (es decir, reemplazados en sus caracteres por *). Ejemplo: censurar("Un tete a tete con Tete", "tete") --> "Un **** a **** con ****" (notar que tanto tete como Tete fueron censuradas).

def censurar(texto, palabra):
    lista_palabras = texto.split()
    palabra_censurada = ''
    for i in range(len(palabra)):
        palabra_censurada += '*'

    for i in range(len(lista_palabras)):
        if lista_palabras[i].lower() == palabra.lower():
            lista_palabras[i] = palabra_censurada
    
    return (' ').join(lista_palabras)

#print(censurar("Un auto pasea por mi casa y se llama Auto", "auto"))



#Escribir una función que recibe un número entero $n$ e imprime un tablero de ajedrez de tamaño $N \times N$. Por ejemplo, el tablero deberá imprimirse de la siguiente forma para un tablero de $N = 3$:
"""
b n b
n b n
b n b
"""
#Nota: b denota un casillero blanco, n denota un casillero negro.

def tablero_ajedrez(numero):
    for columna in range(numero): 
        for fila in range(numero): 
            if fila == columna:
                print("b", end= ' ')
            else:
                print ("n", end= ' ')
        print()

#print(tablero_ajedrez(4))

#Se desea escribir una nota de rescate recortando letras de una revista. Escribir una función que reciba por parámetro la nota que se desea escribir y el texto completo de la revista, y devuelva True si la revista contiene todas las letras necesarias para escribir la nota (ignorando mayúsculas y minúsculas), False en caso contrario.

#Ejemplo: Si la revista contiene "Algoritmos y Programacion", podemos escribir la nota "Gracias por la moto", pero no se puede escribir "Porotos amargos" (falta una s).

def rescate(nota_rescate, texto_revista):
    nota_rescate.lower()
    texto_revista.lower()
    nota_rescate.split(",")
    texto_revista.split(",")
    while True:
        for i in texto_revista:
            if i in nota_rescate:
                texto_revista.pop(texto_revista.index(i))
        

#print(rescate("Porotos amargos", "Algoritmos y Programacion"))

#Escribir una función validar_contraseña que reciba una palabra clave y un número de intentos n. Dicha función debe pedir al usuario que ingrese la contraseña un máximo de n veces. En caso de que la contraseña ingresada coincida con la recibida por la función, se devuelve True, caso contrario se devuelve False.

def validar_contraseña(clave, n):
    n = int(n)
    while n > 0:
        contraseña = input(f"Ingrese la contraseña en un máximo de {n} intentos: ")
        if clave != contraseña:
            n -= 1
            print(f"A usted le quedan {n} intentos.")
            continue
        if clave == contraseña:
            return True
    return False
        
#print(validar_contraseña("casa", 3))

#Escribir una función que reciba un número secreto (entero) y le pregunte un número al usuario. Si el número ingresado es distinto, debe indicarle si es mayor o menor al número secreto y volver a pedirle otro número. Si es igual, debe felicitar al usuario y mostrar en cuántos intentos adivinó. No hay un máximo de intentos pero el usuario debe adivinar para terminar el programa.

def funcion(n_secreto):
    intentos_realizados = 0
    n_secreto = int(n_secreto)
    n_ingresado = input("¿Qué número entero desea ingresar?: ")
    while True:
        n_ingresado = int(n_ingresado)

        if n_ingresado == n_secreto:
            intentos_realizados += 1
            print(f"¡Felicitaciones! Usted ha adivinado en {intentos_realizados} intentos.")
            break

        if n_ingresado != n_secreto:

            if n_ingresado < n_secreto:
                n_ingresado = input("El número ingresado es menor que el número secreto, vuelva a ingresar otro número: ")

            elif n_ingresado > n_secreto:
                n_ingresado = input("El número ingresado es mayor que el número secreto, vuelva a ingresar otro número: ")

            intentos_realizados += 1 


#print(funcion(727))

#Escribir una función que realice lo siguiente: 
# - Le pida al usuario que ingrese una contraseña. Luego debe validar que la misma: 
#       - Tenga al menos dos numeros, pero no tenga más números que letras (a-z, A-Z, no es necesario incluir letras acentuadas o especiales de otros idiomas que no sea el ingles). 
#       - Tenga alguno de estos caracteres ("!", "@", "~", "/", "#") pero no más de tres. 
# - Si no ingresa una contraseña válida debe volver a preguntarle hasta quedarse sin intentos. 
# - Cuando sea válida, se deben devolver la cantidad de intentos restante. Si se acaban los intentos, debe mostrar un mensaje por pantalla y devolver -1. La cantidad de intentos es recibida por parametro.

def contraseña(intentos):
    caracteres = "!@~/#"
    while intentos > 0:
        cantidad_numeros = 0
        cantidad_letras = 0
        cantidad_caracteres = 0
        clave = input("Ingrese una contraseña:")
        intentos -= 1
        if intentos == 0:
            print("Se te acabaron los intentos.")
            return -1
        for generico in clave:
            if generico.isnumeric():
                cantidad_numeros += 1
        for generico in clave:
            if generico.isalpha():
                cantidad_letras +=1
        for generico in clave:
            if generico in caracteres:
                cantidad_caracteres += 1
        if (cantidad_numeros < 2) or (cantidad_numeros > cantidad_letras) or (cantidad_caracteres > 3 or cantidad_caracteres < 1):
            print("Tiene que tener al menos 2 numeros pero no más numeros que letras, y tiene que tener por lo menos un caracter especial pero no mas de 3")
            continue
        if (cantidad_numeros >= 2) and (cantidad_numeros < cantidad_letras) and (1 <= cantidad_caracteres <= 3) and intentos > 0:
            return print(f"Te quedó {intentos} intento(s) restante(s)")

contraseña(4)


#Escribir una función que le pida al usuario que ingrese un número. Se debe luego validar la entrada del usuario según las siguientes condiciones:

#- Debe ser positivo
#Debe ser primo (considerar que está implementada la función es_primo(n))
#La función debe repetir este proceso hasta que el usuario ingrese un número válido o ingrese un caracter especial de fin (que se recibe por parámetro). La función debe devolver el número válido o -1 en caso de que haya ingresado el caracter de fin.
