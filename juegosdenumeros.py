"""
Ejercicio 4: 
Se pide hacer un programa que ingrese 8 juegos de 𝑛 valores positivos 
cada uno. Considerar una condición de corte para el flujo de números. 
Calculando el promedio de cada juego, el máximo de cada juego y el 
mínimo de todos los juegos. 
Donde en cada juego se deberá calcular: 
• El máximo número ingresado. 
• El mínimo número ingresado. 
• El promedio de cada juego. 
• El mínimo de todos los juegos. 
"""

CANTIDAD_DE_JUEGOS: int = 8     #CONSTANTE

numero: int = 0
max_numero: int = 0
min_numero: int = 0
promedio_juego: float = 0
min_todos_juegos: int = 0
contador_numeros: int = 0
juego: int = 0

for juego in range(1, CANTIDAD_DE_JUEGOS + 1):   

    suma_numeros: int = 0
    contador_numeros = 0 

    numero: int = int(input('Ingresar número positivo: '))  

    max_numero = numero
    min_numero = numero

    while numero >= 0:       #condición de corte para el flujo de números = números inferiores a 0

        suma_numeros += numero

        contador_numeros += 1

        if numero > max_numero:
            max_numero = numero
        
        if numero < min_numero:
            min_numero = numero

        numero: int = int(input('Ingresar número positivo (número negativo para salir): ')) 
    
    if min_numero < min_todos_juegos or min_todos_juegos == 0:   #min_todos_juegos == 0 porque inicializa en 0, si es el primer juego entonces y queda así entonces ese es el mínimo
        min_todos_juegos = min_numero
        
    promedio_juego = (suma_numeros) / (contador_numeros) 
    
    print(f"""

* * * * * * * * * * * * * * * * * * * * * * * 
                                          
 JUEGO || {juego}                            
                                             
 El máximo numero ingresado es: {max_numero}                                             
                                             
 El mínimo número ingresado es: {min_numero}                                           
                                             
 El promedio del juego es: {promedio_juego}                                           
                                           
* * * * * * * * * * * * * * * * * * * * * * *

            """)
    
print(f"El mínimo de todos los juegos es: {min_todos_juegos}")
        