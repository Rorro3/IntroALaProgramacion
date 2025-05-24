#vuelvo a pertenece
def pertenece(numero: int, lista: list[int]) -> bool:
    return numero in lista
print(pertenece(4,[6,7,4]))

#quiere que le diga si en una lista de listas (matriz), esta el numero en cada una de las filas con una lista de bool
#ejemplo: [[2,3],[3,4],[4,5]], 3 ->>>>>>>>>>>> [True, True, False]

def pertenece_a_cada_uno(matriz: list[list[int]], numero: int) -> list[bool]:
    res = []
    for fila in matriz:
        if pertenece(numero, fila):
            res.append(True)
        else:
            res.append(False)
    return res
print(pertenece_a_cada_uno([[2,3],[3,4],[4,5]], 3))

#la diferencia con la version 2 es un >= y un =
#la diferencia con la version 3 es que en la 3 la salida es distinta

