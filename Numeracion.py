"""
EXPLICACIÓN DE LOS EJERCICIOS DE NUMERACIÓN

1) Pase a base 16 el siguiente número expresado en base 2:
1101001111011,10100101

Justificación: Para pasar de base 2 a base 16 utilizo BP (bases que son potencia entre sí) ya que es el método más directo y rápido con menos margen de error entre estas bases.
De esta manera, al ser 2^4 = 16 esto significa que 4 números en base binaria representan 1 de la base 16.

BASE 2  |  BASE 16        (yendo de derecha a izquierda)
  0101  |   5
  1010  |   A
  1011  |   B
  0111  |   7
  1010  |   A
    1   |   1

Resultado final de la conversión: 1A7B.A5000

PD: Se agregan los 0 dependiendo de cuántos símbolos se le adjudique a la base menor en cuanto a la base mayor, por ejemplo, 4 simbolos de 2 equivalen a 1 de 16, siendo 0001 el primer número.
Entonces al final se le agrega tres 0. Si fuese de 2 a 8, seria 3 simbolos de 2 equivalen a 1 de 8, siendo 001 el primer número, entonces al final se le agrega dos 0.

2) Dado el nro 2019 (base 10), expréselo en base 4 y en base 2:

Justificación: Para convertir de base 10 a cualquier otra base (10 -> X) empleo el método "Divisiones y multiplicaciones sucesivas" (DS/MS), el cual consiste en dividir el número dado con la base a utilizar.

BASE 10 -> BASE 4:

            RESTOS
2019 / 4 =    3
504 / 4  =    0
126 / 4  =    2
31 / 4   =    3
7 / 4    =    3
1        =    1

Los restos componen el resultado final, yendo del 1 al primer resto calculado, siendo éste: 133203.

BASE 10 -> BASE 2:

            RESTOS
2019 / 2 =    1
1009 / 2 =    1
504 / 2  =    0
252 / 2  =    0
126 / 2  =    0
63 / 2   =    1
31 / 2   =    1
15 / 2   =    1
7 / 2    =    1
3 / 2    =    1
1        =    1

El resultado final es: 11111100011

3) a) Pase a base 10 el siguiente número expresado en base 6:
32442,51

b) Pasar el siguiente número en base 10 a base 9 con error menor o igual a 10-4:
6658,633

c) Pasar el siguiente número de base 4 a base 16 y justifique el método por el cual
decidió hacer la conversión:
1223,23

A) BASE 6 -> BASE 10:

Para realizar una conversión de base 6 a base 10 utilizo TFN (Teorema Fundamental de la Numeración) el cual consiste en la suma de cada dígito multiplicado por la potencia de la base correspondiente a la posición que ocupa en el número.

1 x 6^-2 + 5 x 6^-1 + "," + 2 x 6^0 + 4 x 6^1 + 4 x 6^2 + 2 x 6^3 + 3 x 6^4 = 4490.86111

B) BASE 10 -> BASE 9 con error menor o igual a 10-4:

Justificación: Para convertir de base 10 a cualquier otra base (10 -> X) empleo el método "Divisiones y multiplicaciones sucesivas" (DS/MS), el cual consiste en dividir el número dado con la base a utilizar.

            RESTOS
6658 / 9 =    7
739 / 9  =    1
82 / 9   =    1
9 / 9    =    0
1        =    1

PARTE FRACCIONARIA:

0.633 x 9 = 5.697 -> tomo el 0.697
0.697 x 9 = 6.273 -> tomo el 0.273
0.273 x 9 = 2.457 -> tomo el 0.457
0.457 x 9 = 4.113

En este caso el margen de error es 10^-4 por ende solamente tomamos 4 números que están atrás de la coma (5624)

Resultado final: 10117.5624

C) BASE 4 -> BASE 16:

BP -> Bases que son potencia, ya que 4^2 = 16, o sea que 2 símbolos de base 4 equivalen a 1 de base 16. Método directo, preciso y sin margen de error.

1223,23 -> 6B.B



PD: PARA HACER LAS CONVERSIONES SE RECOMIENDA TENER LAS TABLAS PRE HECHAS A MANO
"""