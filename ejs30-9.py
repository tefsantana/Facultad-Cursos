"""
Ejercicio 1:

Escribir un programa que permita cambiar todas las palabras que indique el usuario en un texto dado.
"""
"""
texto: str = input("Escriba un texto: ")

palabras_a_cambiar: str = input("Escriba las palabras a cambiar del texto: ")

palabras_nuevas: str = input("Ahora escriba las palabras con las que desea reemplazar las otras del texto dado: ")

print("Su nuevo texto ahora es:")
print(texto.replace(palabras_a_cambiar, palabras_nuevas))"""


"""
Ejercicio 2:

Escribir un programa que permita desencriptar un texto dado.
El encriptado del código es el siguiente
El mensaje está escrito cada 3 caracteres comenzando por el tercero.
Cada número corresponde a una vocal (1=a,2=e,3=i,4=o,5=u)
Los espacios se representan con “&”
Texto="avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"
"""

texto: str = "avFfe2rtlty3cvchg3yutui1olcpi3bv4qwnef2zxsza,zc&cvdjy4uimkm3lindg1qcnxa&wesxatqhrjr3xcnumgaqs"
texto_nuevo: str = ""

texto_nuevo1: str = texto.replace("1", "a")
texto_nuevo2: str = texto_nuevo1.replace("2", "e") 
texto_nuevo3: str = texto_nuevo2.replace("3", "i")
texto_nuevo4: str = texto_nuevo3.replace("4", "o")
texto_nuevo5: str = texto_nuevo4.replace("5", "u")
texto_nuevo6: str = texto_nuevo5.replace("&", " ")

print(texto_nuevo6[2::3])