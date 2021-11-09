"""
2) (4ptos)“@RumboCircular” es un emprendimiento que enseña a cuidar el medioambiente. Rumbo Circular además 
de dictar cursos de capacitación sobre medioambiente en empresas, lanzó un conjunto de cursos para la comunidad 
general.
Estos cursos son los siguientes:
- Aprendé a hacer tu propio compost (1 día de curso). Costo $950
- Los niños y el medioambiente (para padres e hijes) (2 días de curso). Costo $990
- Tu huerta orgánica (4 días de curso). Costo $2500
El gran éxito de de estos cursos hizo que RumboCircular nos consultara para que los asesoremos para la creación de 
un pequeño sistema que permita organizar la asistencia de los participantes.
Los requerimientos que nos solicitan son los siguientes:
a- Crear un menú que permita el acceso a los siguientes puntos.
b- Modificación de cursos. Se podrá modificar la siguiente infomación de los cursos. Nombre, cantidad de días, 
costo.
c- Listar todos los cursos cuyo costo sea superior a 1150 pesos.
d- Cargado de asistentes a los cursos definidos.
e- Mostrar el listado de todos los cursos y sus respectivos asistentes. Ordenados por nombre de curso en forma 
ascendente.

"""

def menu() -> None:
    print("""
    RUMBO CIRCULAR:
    ( 1 ) Modificación de cursos (nombre, cantidad de días, costo)
    ( 2 ) Listar cursos cuyo costo sea superior a 1150 pesos.
    ( 3 ) Cargado de asistentes a los cursos definidos.
    ( 4 ) Mostrar listado de todos los cursos con sus respectivos asistentes.
    ( 5 ) Salir de programa.
    """)

def modificar_nombre(curso: dict) -> None:
    nombre_nuevo: str = input("Ingrese el nombre nuevo: ")

    curso["Nombre"] = nombre_nuevo

def modificar_cantidad_dias_curso(curso: dict) -> None:
    cantidad_nueva_de_dias: int = int(input("Ingrese la cantidad de días que desee: "))

    while not int(cantidad_nueva_de_dias):
        cantidad_nueva_de_dias = int(input("Ingrese la cantidad de días que desee: "))
    
    curso["Cantidad de días"] = cantidad_nueva_de_dias

def modificar_costo(curso: dict) -> None:
    costo_nuevo: int = int(input("Ingrese el nuevo costo: "))

    while not int(costo_nuevo):
        costo_nuevo = int(input("Ingrese el costo nuevo: "))

    curso["Costo"] = costo_nuevo

def modificar_cursos(curso: dict) -> None:
    curso_pregunta: str = input("""
    OPCIONES:
    Ingrese 0 para modificar el nombre del curso.
    Ingrese 1 para modificar la cantidad de días del curso.
    Ingrese 2 para modificar el costo del curso.
    """)

    if curso_pregunta == "0":
        modificar_nombre(curso)
        
    elif curso_pregunta == "1":
        modificar_cantidad_dias_curso(curso)
        
    elif curso_pregunta == "2":
        modificar_costo(curso)

    else:
        curso_pregunta = input("Ingrese un valor válido comprendido entre 0 y 2 según corresponda.")

def listar_cursos_con_precio_mayor(curso: dict) -> None:
    if curso["Costo"] > 1150:
        print(f"- {curso['Nombre']}")

def cargar_asistentes(curso: dict) -> None:
    curso["Asistentes"] = []

    asistente: str = input(f"Ingrese nombre del asistente del curso '{curso['Nombre']}': ")

    curso["Asistentes"].append(asistente)

def ordenar_listado_cursos_con_asistentes(lista_cursos_con_nombres: list) -> list:   
    lista_ordenada = sorted(lista_cursos_con_nombres)

    return lista_ordenada
    
def main() -> None:
    continuar: bool = True
    curso_1: dict = {
        "Nombre": "Aprendé a hacer tu propio compost",
        "Cantidad de días": 1,
        "Costo": 950
    }

    curso_2: dict = {
        "Nombre": "Los niños y el medioambiente (para padres e hijes)",
        "Cantidad de días": 2,
        "Costo": 990
    }

    curso_3: dict = {
        "Nombre": "Tu huerta orgánica",
        "Cantidad de días": 4,
        "Costo": 2500
    }

    lista_cursos_con_nombres: list = [curso_1["Nombre"], curso_2["Nombre"], curso_3["Nombre"]]
    listado_diccionarios: list = [curso_1, curso_2, curso_3]

    while continuar:
        menu()
        opciones_menu: str = input("Ingrese el número que desee elegir: ")

        if opciones_menu == "1":
            modificar_curso: str = input("""Desea modificar la información de algún curso?
        Presione 1 para modificar el curso 'Aprendé a hacer tu propio compost'.
        Presione 2 para modificar el curso 'Los niños y el medioambiente (para padres e hijes)'
        Presione 3 para modificar el curso 'Tu huerta orgánica'.
        """)

            if modificar_curso == "1":
                modificar_cursos(curso_1)
    
            elif modificar_curso == "2":
                modificar_cursos(curso_2)
    
            elif modificar_curso == "3":
                modificar_cursos(curso_3)
    
            while 1 > int(modificar_curso) or int(modificar_curso) > 4 or not modificar_curso.isnumeric():
                modificar_curso = input("Ingrese un valor válido: ")

        if opciones_menu == "2":
            listar_cursos_con_precio_mayor(curso_1)
            listar_cursos_con_precio_mayor(curso_2)
            listar_cursos_con_precio_mayor(curso_3)
    
        elif opciones_menu == "3":
            cargar_asistentes(curso_1)
            cargar_asistentes(curso_2)
            cargar_asistentes(curso_3)
    
        elif opciones_menu == "4":
            if curso_1["Asistentes"] == [] or curso_2["Asistentes"] == [] or curso_3["Asistentes"] == []:
                print(f"No se puede cargar los asistentes de los cursos.")
            ordenar_listado_cursos_con_asistentes(lista_cursos_con_nombres)
            for curso in listado_diccionarios:
                print(f"Curso '{curso['Nombre']}':")
                print("Asistentes:")
                nombre_asistente = "".join(curso['Asistentes'])
                print(f"- {nombre_asistente}")

        elif opciones_menu == "5":
            continuar = False

main()