"""
- Escribir una función que permita calcular la duración en segundos de un intervalo dado en horas, minutos y segundos.
- Usando la función del ejercicio anterior, escribir un programa que pida al usuario dos intervalos expresados en horas, minutos y segundos, sume sus duraciones, y muestre por pantalla la duración total en horas, minutos y segundos.
"""

def intervalo_a_segundos(horas: int, minutos: int, segundos: int) -> int:
    total_segundos: int = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos

def main() -> None:
    horas: int = int(input("Ingrese las horas: "))
    minutos: int = int(input("Ingrese los minutos: "))
    segundos: int = int(input("Ingrese los segundos: "))

    print(f"El total del intervalo es {intervalo_a_segundos(horas = horas, minutos = minutos, segundos = segundos)} segundos.")

main()

"""***********************************************************************************"""

def conversor (horas: int, minutos: int, segundos: int) -> int:
    segundos1 = (horas * 60) * 60
    segundos2 = minutos * 60
    segundos_totales = segundos1 + segundos2 + segundos
    return segundos_totales

def main() -> None:
    print("Ingrese el intervalo de tiempo en horas, minutos y segundos que va a ser convertido en segundos.")
    horas = int(input("Ingrese las horas: "))
    minutos = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    segundos_totales = conversor(horas, minutos, segundos)
    print(segundos_totales)

main()
