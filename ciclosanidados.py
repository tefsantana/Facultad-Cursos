'''Se tienen 10 cursos de 30 alumnos de los cuales se quiere saber lo siguiente:
a) El promedio de cada curso
b) El curso que mayor promedio tiene
c) El nombre del alumno que mayor nota obtuvo (se supone único) y a que curso pertenece'''

#VARIABLES DE CURSO
CANTIDAD_DE_CURSOS : int = 3            # constante
mejor_curso : int = 0

#VARIABLES DE ALUMNO
CANTIDAD_DE_ALUMNOS : int = 3         # constante
nombre_alumno : str = ""
mejor_alumno : str = ""

#VARIABLES DE NOTA Y PROMEDIO
mayor_nota : int = 0
mayor_promedio : float = 0

for curso in range(CANTIDAD_DE_CURSOS):
    suma_notas : int = 0 
    promedio : float = 0

    for alumno in range(CANTIDAD_DE_ALUMNOS):
        print(f"Curso: {curso + 1} | Alumno: {alumno + 1}")
        nombre_alumno = input("Ingrese nombre del alumno: ")
        nota : int = int(input("Ingrese nota del alumno: "))
        suma_notas += nota
        if (nota > mayor_nota):
            mayor_nota = nota
            mejor_alumno = nombre_alumno
            curso_mejor_alumno : int = (curso + 1)
    
    promedio = (suma_notas / CANTIDAD_DE_ALUMNOS)

    print(f"El promedio del curso es: Curso {curso + 1} = {promedio}")

    if (promedio > mayor_promedio):
        mayor_promedio = promedio
        mejor_curso = (curso + 1)

print(f"La mayor nota es {mayor_nota} y pertenece a {mejor_alumno} el cual pertenece al curso {curso_mejor_alumno}")
print(f"El curso que mayor promedio tuvo es el: {mejor_curso}")


