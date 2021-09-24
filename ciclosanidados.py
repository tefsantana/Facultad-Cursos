
"""suma = 0
for i in range(10):
    valor = int(input("Ingrese un número: "))
    suma = suma + valor
print(f"La suma de los números ingresados es: {suma}")


pregunta : str = input("Desea agregar un gato más? (SI/NO): ") #no hace falta aclarar el str porque ya lo inicializaste y los inputs son string
gatos : int = 0
while pregunta == "SI":
    gatos += 1
    pregunta = input("Desea agregar un gato más? (SI/NO): ")
print(f"La cantidad de gatos tirados a Timmy son: {gatos}")

numero : int = int(input("Ingrese un número: "))
maximo : int = 0 #puede ir cualquier num
minimo : int = 0 #puede ir cualquier num

while (numero != 0): #puede ir cualquier condicion, ese era el ejercicio
    if (numero > maximo):
        maximo = numero
    if (numero < minimo):
        minimo = numero
    numero : int = int(input("Ingrese un número: "))

print(f"El máximo ingresado fue {maximo}")
print(f"El mínimo ingresado fue {minimo}")

for i in range(3):
    password:str = input("Ingrese su password: ")
    if password == "secreta":
        print("Password correcta!")
        break
else:
    print("Hubo 3 intentos fallidos!")"""


"""Ejercicio ciclos anidados.
Se tienen 10 cursos de 30 alumnos de los cuales se quiere saber lo siguiente:
1. El promedio de cada curso
2. El curso que mayor promedio tiene
3. El nombre del alumno que mayor nota obtuvo (se supone único) y a que curso pertenece"""

#VARIABLES DE CURSO
cursos : int = 3
mejor_curso : int = 0

#VARIABLES DE ALUMNO
alumnos : int = 3
nombre_alumno : str = ""
mejor_alumno : str = ""

#VARIABLES DE NOTA Y PROMEDIO
mayor_nota : int = 0
mayor_promedio : float = 0

for curso in range(cursos):
    suma_notas : int = 0 
    promedio : float = 0

    for alumno in range(alumnos):
        print(f"Curso: {curso + 1} | Alumno: {alumno + 1}")
        nombre_alumno = input("Ingrese nombre del alumno: ")
        nota : int = int(input("Ingrese nota del alumno: "))
        suma_notas += nota
        if (nota > mayor_nota):
            mayor_nota = nota
            mejor_alumno = nombre_alumno
            curso_mejor_alumno : int = (curso + 1)
    
    promedio = (suma_notas / alumnos)

    print(f"El promedio del curso es: Curso {curso + 1} = {promedio}")

    if (promedio > mayor_promedio):
        mayor_promedio = promedio
        mejor_curso = (curso + 1)

print(f"La mayor nota es {mayor_nota} y pertenece a {mejor_alumno} el cual pertenece al curso {curso_mejor_alumno}")
print(f"El curso que mayor promedio tuvo es el: {mejor_curso}")

       
        
    


