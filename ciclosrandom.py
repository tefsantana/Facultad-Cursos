suma = 0
for i in range(10):
    valor = int(input("Ingrese un número: "))
    suma = suma + valor
print(f"La suma de los números ingresados es: {suma}")


pregunta : str = input("Desea agregar un gato más? (SI/NO): ") #no hace falta aclarar el str delante del input porque ya lo inicializaste y los inputs son string
gatos : int = 0
while pregunta == "SI":
    gatos += 1
    pregunta = input("Desea agregar un gato más? (SI/NO): ")
print(f"La cantidad de gatos tirados a Timmy son: {gatos}")

numero : int = int(input("Ingrese un número: "))
maximo : int = 0 #puede ir cualquier num
minimo : int = 0 #puede ir cualquier num

while (numero != 0): #condición cualquiera que le pongo yo
    if (numero > maximo):
        maximo = numero
    if (numero < minimo):
        minimo = numero
    numero : int = int(input("Ingrese un número: "))

print(f"El máximo ingresado fue {maximo}")
print(f"El mínimo ingresado fue {minimo}")


#Ejemplo de else luego de un for
for i in range(3):
    password:str = input("Ingrese su password: ")
    if password == "secreta":
        print("Password correcta!")
        break
else:
    print("Hubo 3 intentos fallidos!")
