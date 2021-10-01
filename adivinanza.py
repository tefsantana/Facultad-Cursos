"""
Ejercicio 2: 
Realizar un programa que permita jugar a adivinar un número entero.  
El participante A elige el número a adivinar, y luego hace jugar al 
participante B, el cual deberá intentar adivinarlo arriesgando números.  
El programa debe guiar al participante B indicándole, en cada intento, si el 
número arriesgado es mayor o menor al definido por el participante A. 
El juego debe concluir al acertar el número o superar los 20 intentos.  
Al acertar el número debe indicar la cantidad de intentos que fueron 
utilizados para lograrlo.  
En caso de no haber conseguido el objetivo, debe indicarle que ha superado 
los 20 intentos. 
"""
INTENTOS: int = 20
numero_A: int = int(input('PARTICIPANTE A | Ingresar número entero a adivinar por el PARTICIPANTE B: '))  
numero_B: int = -1 

while numero_A < 0:

    numero_A = int(input('PARTICIPANTE A | Número inválido. Ingresar número entero a adivinar por el PARTICIPANTE B: '))  

while INTENTOS!= 0 and numero_B != numero_A:

    numero_B = int(input(f"PARTICIPANTE B | Adivine el número entero del PARTICIPANTE A: "))

    INTENTOS-= 1

    if INTENTOS == 0:
        print("Se alcanzó el máximo de intentos permitidos. ¡PARTICIPANTE A gana!")
    
    elif (numero_A == numero_B):
        print(f"¡Felicidades PARTICIPANTE B! Ganaste con {20 - INTENTOS} intentos.")

    elif numero_A < numero_B:
      print(f"El número ingresado por el PARTICIPANTE B es mayor al numero ingresado por el PARTICIPANTE A. Le quedan {INTENTOS} intentos.")

    elif numero_A > numero_B:
      print(f"El número ingresado por el PARTICIPANTE B es menor al numero ingresado por el PARTICIPANTE A. Le quedan {INTENTOS} intentos.")

    else:
        print(f"Incorrecto. Siga intentando. A usted le quedan {INTENTOS} intentos restantes.")



    
    



