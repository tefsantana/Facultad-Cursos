from vectores import diferencia
from vectores import norma
from vectores import producto_vectorial

def area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    Xab, Yab, Zab = diferencia(x1, y1, z1, x2, y2, z2)
    Xac, Yac, Zac = diferencia(x1, y1, z1, x3, y3, z3)
    a,b,c = producto_vectorial(Xab, Yab, Zab, Xac, Yac, Zac)
    return (norma(a,b,c))*0.5 


assert area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0) == 19.45507645834372
assert area_triangulo(1, 1, 1, 1, 1, 1, 1, 1, 1) == 0
assert area_triangulo(2, 2, 2, 3, 2, 2, 2, 2, 3) == 0.5

# Fórmula de área de un triángulo ABC :  Área = (|| AB x AC ||) / 2 
