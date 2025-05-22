import math

#1 quiere que le diga si un int pertenece a una seq de int
def pertenece(lista: list[int], numero: int) -> bool:
    for i in lista:
        if numero == i: #coso, no hay que poner lista[i] porque ya sabe que estoy en lista xD
            return True
    return False

print(pertenece([1,2,3], 3))
print(pertenece([1,2,3], 4))

def pertenece2(lista: list[int], numero:int) -> bool:
    i = 0
    while i < len(lista): #no va <= porque el < te agarra todo
        if numero == lista[i]:
            return True
        i += 1 #por fuera del if, porque sino solo incrementaria si es true
    return False #fuera del while porque recorrio todo y no encontro nada, quiero que igual me devuelva algo

print(pertenece2([1,2,3], 4))
print(pertenece2([1,2,3], 3))

#la hizo chatgpt
def pertenece_while_sin_if(lista: list[int], numero: int) -> bool:
    i = 0
    while i < len(lista) and lista[i] != numero: #solo incrementa el indice cuando el numero es distinto
        i += 1
    return i < len(lista) 

#cuando el numero es igual, sale del while y returnea true (porque i < len(lista) es true),
#y si termino de recorrer toda la lista y no encontro que pertenezca, sale del while 
#y como i < len(lista) es falso (porque incremento un numero mas del lenght de la lista), returnea false

print(pertenece_while_sin_if([1,2,3], 3))
print(pertenece_while_sin_if([1,2,3], 4))

#si qiero usar solo ifs, puedo hacer una funcion recursiva, but that sounds like funcional and i dont have ganas

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#2 quiere que le diga si un int divide a todos los elementos de una lista de ints
def divide_a_todos(lista: list[int], numero:int) -> bool:
    for i in lista:
        if i % numero != 0:
            return False
    return True

print(divide_a_todos([2,4,6,8,10],2))
print(divide_a_todos([2,4,6,8,10],4))
#a penas encuentra un i que no sea divisible por numero, termina y da false, (PORQUE YO QUIERO QUE TODOS SEAN DIVISIBLES)
#si recorrio toda la lista y no returneo nada porque todos son divisibles, sale del for y devuelve true

def divide_a_todos_2(lista: list[int], numero:int) -> bool:
    i = 0
    while i < len(lista):
        if lista[i] % numero != 0:
            return False
        i += 1
    return True
#yo lo visualizo mejor asi, no se por que
#se sale del len de la lista y dice, "bueno, chequee todo, nunca devolvi false, debe ser true"

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#3 quiere que le diga la suma total de todos los elementos de la lista
def suma_total(lista: list[int]) -> int:
    #aca ya dejo de usar i y j porque me mareo
    total = 0
    for numero in lista:
        total += numero #con cada iteracion "total" se modifica (hasta que termine el for y returnee "total", luego al siguiente print vuelve a ser 0)
    return total

print(suma_total([2,3,4]))

#para mi sigue siendo mas facil usar un while
def suma_total_while(lista: list[int]) -> int:
    total = 0
    i = 0
    while i < len(lista):
        total += lista[i]
        i += 1
    return total

print(suma_total_while([1,2,3,4]))

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#4 quiere que le diga el maximo numero
def maximo(lista: list[int]) -> int:
    max_actual = lista[0] #antes habia puesto max_actual = 0, pero esto no me daba bien si era un numero negativo el primero
    for indice in lista:
        if indice >= max_actual:
            max_actual = indice
    return max_actual

print(maximo([3,4,1,5]))
print(maximo([3,4,1,1,1]))

#---------------------------------------------
#5 lo mismo pero con minimo
def minimo(lista: list[int]) -> int:
    min_actual = lista[0]
    for indice in lista:
        if indice <= min_actual:
            min_actual = indice
    return min_actual

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#6 quiere que le diga si los numeros de una lista estan ordenados de menor a mayor
def ordenados(lista: list[int]) -> bool:
    numero = lista[0] #primer numero
    for indice in range(1, len(lista)): #como quiere maximo estricto tengo que poner range, porque sino me va a comparar el primer elemento con el primer elemento y como son iguales va a dar false
        if lista[indice] <= numero: #tengo que poner lista[indice] porque dice FOR INDICE IN RANGE, no for indice in lista
            return False
        numero = lista[indice] #como esta fuera del if, si el return false no sucede, va a hacer esto (numero = lista[indice]) y vuelve a hacer el if porque esta detro del for
    return True #se fijo todo y nunca me dio false

print(ordenados([1,2,3,4,5]))
print(ordenados([1,2,3,5,4]))

#ahora con un while ^^
def ordenados_while(lista: list[int]) -> bool:
    i = 0
    while i < len(lista) - 1: #menos 1 porque estoy mirando tmb el i + 1
        if lista[i + 1] <= lista[i]:
            return False
        i += 1
    return True
#y ves que se ve mas lindo con el while en este caso? POR ESO HAY QUE APRENDER A USAR TODO

print(ordenados_while([1,2,3,4,5]))
print(ordenados_while([1,2,3,5,4]))
