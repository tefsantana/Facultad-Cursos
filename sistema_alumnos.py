"""
Cree un programa que permita al usuario elegir entre las siguientes opciones:
Agregar un alumno: debe solicitarse nombre,padron y nota.
Consultar aprobados: debe mostrar los alumnos con nota mayor a 4.
Cantidad de alumnos totales y promedio general.
Quitar a un  alumno.
Salir
"""

def elegir_opcion() -> None:
    print("""
OPCIONES:\n
( 1 ) Agregar alumno: ingresar nombre, padrón y nota,
( 2 ) Consultar aprobados (nota mayor a 4),
( 3 ) Cantidad de alumnos totales y promedio general,
( 4 ) Quitar un alumno,
( 5 ) Salir.\n""")

def agregar_alumno(lista_alumnos: list) -> None:
    """PRE CONDICIÓN: recibe una lista de alumnos ya existente.
POST CONDICIÓN: agrega a la lista de alumnos un alumno el cual tiene nombre, padrón y nota."""
    nombre: str = input("Ingrese el nombre del alumno: ")
    padron: int = int(input("Ingrese el padrón del alumno: "))
    while not int(padron):
        padron = int(input("Ingrese un padrón válido: "))
    nota: float = float(input("Ingrese la nota del alumno: "))
    while not float(nota):
        nota = float(input("Ingrese una nota válida: "))
    dict_alumno: dict = {
        "Nombre": nombre,
        "Padrón": int(padron),
        "Nota": float(nota),
    }
    lista_alumnos.append(dict_alumno)

def consultar_aprobados(lista_alumnos: list) -> None:
    """PRE CONDICIÓN: recibe una lista de alumnos para operar con ella.
POST CONDICIÓN: muestra todos los alumnos aprobados con una nota mayor a 4 que se encuentran en la lista de alumnos."""
    print("\nLos alumnos aprobados son:")
    for alumno in lista_alumnos:
        if alumno['Nota'] > 4:
            print(f"{alumno['Nombre']}: APROBADO con {alumno['Nota']}")

def consultar_alumnos_totales_y_promedio_general(lista_alumnos: list, contador_alumnos: int, suma_notas: float, promedio_notas: float) -> None:
    """PRE CONDICIÓN: recibe una lista de alumnos para operar con ella.
POST CONDICIÓN: muestra la cantidad de alumnos totales y el promedio general de las notas de todos ellos."""
    for alumno in lista_alumnos:
        suma_notas += alumno['Nota']
    promedio_notas = suma_notas / contador_alumnos
    print(f"\nLa cantidad total de alumnos es: {contador_alumnos}")
    print(f"\nEl promedio general de todos los alumnos es {promedio_notas}")

def quitar_alumno(lista_alumnos: list) -> None:
    """PRE CONDICIÓN: recibe una lista de alumnos para operar con ella.
POST CONDICIÓN: elimina el diccionario del alumno que coincida con el nombre ingresado."""
    alumno_a_eliminar: str = input("Ingrese el nombre del alumno a eliminar: ")
    posicion_lista: int = [i for i, diccionario in enumerate(lista_alumnos) if diccionario['Nombre'] == alumno_a_eliminar][0]
    lista_alumnos.remove(lista_alumnos[posicion_lista])

def main() -> None:
    continuar: bool = True
    lista_alumnos: list = []
    contador_alumnos: int = 0
    suma_notas: float = 0
    promedio_notas: float = 0
    existen_alumnos: bool = False

    while continuar:
        elegir_opcion()
        opcion: str = input("Elija una opción: \n")

        while not (int(opcion) >= 1 or int(opcion) <= 5) or not opcion.isnumeric():
            opcion = input("Elija una opción válida: \n")
        
        if opcion == "1":
            agregar_alumno(lista_alumnos)
            contador_alumnos += 1
            existen_alumnos = True
        
        elif opcion == "2":
            if existen_alumnos == False:
                print("No hay registros existentes de alumnos.\n")
            else:
                consultar_aprobados(lista_alumnos)

        elif opcion == "3":
            if existen_alumnos == False:
                print("No hay registros existentes de alumnos.\n")
            else:
                consultar_alumnos_totales_y_promedio_general(lista_alumnos, contador_alumnos, suma_notas, promedio_notas) 
        
        elif opcion == "4":
            if existen_alumnos == False:
                print("No hay registros existentes de alumnos.\n")
            else:
                quitar_alumno(lista_alumnos)
                contador_alumnos -= 1
                if contador_alumnos == 0:
                    existen_alumnos = False 
        
        elif opcion == "5":
            print("""\nSaliendo del programa ...\n""")
            continuar = False
        
main()




