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

def pertenecesinnada(lista: list[int], numero: int) -> bool:
    return numero in lista
#re lol

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

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#7 quiere que si la lista es vacia, devuelva -1
#si la lsta no es vacia, le devuelvo la pisicion del numero mas alto, si se repite, pongo la primera aparicion

def posicion_maximo(lista: list[int]) -> int:
    if len(lista) == 0:
            return -1
    pos_max = 0
    indice = 1
    while indice < len(lista):
        if lista[indice] > lista[pos_max]:
            pos_max = indice
        indice += 1
    return pos_max

print(posicion_maximo([5,3,2,1]))
print(posicion_maximo([3,4,5,7]))
print(posicion_maximo([]))

def posicion_maximo_for(lista: list[int]) -> int:
    if len(lista) == 0:
        return -1
    pos_max = 0
    for indice in range(1, len(lista)):
        if lista[indice] > lista[pos_max]:
            pos_max = indice
    return pos_max
#lo mismo con un for, osea no tengo que incrementar el indice manualmente, again no puedo poner indice solo, tiene que ir acompaniado por lista[indice]
#porque es INDICE IN RANGE, no indice in lista

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#8 copio y pego pero con posicion_minimo
def posicion_minimo(lista: list[int]) -> int:
    if len(lista) == 0:
        return -1
    pos_min = 0
    for indice in range(1, len(lista)):
        if lista[indice] < lista[pos_min]:
            pos_min = indice
    return pos_min

#siempre hay que preguntarse "cual es el caso que de una me termina la funcion?"
#aca es len(lista) == 0 xd
#en el bucle me conviene poner que lo reemplace por indice cuando el indice es menor, vuelvo a hacer el bucle con ese nuevo numero
#si hubiera puesto que si el indice es mayor, no haga nada, tenia que poner un else
#y generalmente no me conviene tener una parte que "no haga nada"

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#9. Dada una lista de palabras (seq⟨seq⟨Char⟩⟩), devolver verdadero si alguna palabra tiene longitud mayor a 7. 
#Ejemplo: [“termo”, “gato”, “tener”, “jirafas”], devuelve falso.
def long_mayor_a_siete(lista: list[str]) -> bool:
    for palabra in lista:
        if len(palabra) > 7:
            return True
    return False

print(long_mayor_a_siete(["termo", "gato", "tener", "jirafas"]))
print(long_mayor_a_siete(["termo", "gato", "tener", "jirafas", "elefantes"]))
#aca yo ya se que a la primera con mas de 7 tengo que returnear algo, fin
#el return false es cuando no returnee nada antes

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#10. Dado un texto en formato string, devolver verdadero si es pal´ındromo (se lee igual en ambos sentidos), falso en caso
#contrario. Las cadenas de texto vac´ıas o con 1 s´olo elemento son pal´ındromo.
def es_palindromo(palabra: str) -> bool:
    if len(palabra) == 0 or len(palabra) == 1:
        return True
    ultima_letra = len(palabra) - 1 #el indice de la ""ultima letra"""
    primera_letra = 0 #el indice de la ""primera letra""
    while primera_letra < ultima_letra: #aca cuando el indice es igual, estaria en la letra del centro; cuando la pasa, ya esta
        if palabra[primera_letra] != palabra[ultima_letra]: #si la primera letra es != de la ultima, ya esta
            return False
        ultima_letra -= 1 #me resta un indice a la segunda ultima letra
        primera_letra += 1 #me suma un indice a la segunda letra
    return True #si nunca dio false, es true

print(es_palindromo("romor"))
print(es_palindromo("romeo"))
print(es_palindromo("romeemor"))

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#11. Recorrer una seq⟨Z⟩ y devolver verdadero si hay 3 n´umeros iguales consecutivos, en cualquier posici´on y 
#False en caso contrario
def tres_iguales_consecutivos(lista: list[int]) -> bool:
    for i in range(0, len(lista) - 2):  # menos 2 para no salir del rango cuando mira i+2 ((puedo sacar el 0, pero mas lindo asi(?)))
        if lista[i] == lista[i+1] == lista[i+2]:
            return True
    return False

#aca si era mas lindo usar for jeje, porque no tengo que incrementar nada a mano, y es lindo porque son consecutivos
#igual con un while lo unico que tenia que hacer era while i < lista -2

print(tres_iguales_consecutivos([3,3,2,3,3,3,4]))
print(tres_iguales_consecutivos([3,3,2,3,3,4,3,3,5]))

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#12. Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas y 
#False en caso contrario
vocales: str = "aeiouAEIOU"

def es_vocal(letra: str) -> bool:
    return letra in vocales
print(es_vocal("a"))
#queria ver si servia mi str de vocales

def vocales_distintas(palabra: str) -> bool:
    contador = 0
    for letra in palabra:
        if es_vocal(letra):
            contador += 1
    return contador >= 3

print(vocales_distintas("romeo"))
print(vocales_distintas("rome"))

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#13. Recorrer una seq⟨Z⟩ y devolver la posici´on donde inicia la secuencia de n´umeros ordenada m´as larga. 
#Si hay dos subsecuencias de igual longitud devolver la posici´on donde empieza la primera. La secuencia de entrada es no vac´ıa.
def pos_secuencia_mas_larga(lista: list[int]) -> int:
    mejor_inicio = 0
    mejor_longitud = 1

    inicio_actual = 0
    longitud_actual = 1

    for i in range(1, len(lista)):
        if lista[i] >= lista[i - 1]:  
            longitud_actual += 1 #le pongo la cantidad de numeros ordenados que hay en la primer secuencia
        else:
            if longitud_actual > mejor_longitud:
                mejor_longitud = longitud_actual #la mejor longitud va a ser la mas larga
                mejor_inicio = inicio_actual #el inicio sigue siendo el 0
            inicio_actual = i #aca se sale del if, es lo que pasa cuando el if no hace nada (me pone el i como nuevo inicio cuando haga lista[i])
            longitud_actual = 1 #porque si no es mas grande que la mejor sigue siendo 1
    if longitud_actual > mejor_longitud: #aca por si justo estaba al final de la lista, si pasa esto no entra ni siquiera en el else
        mejor_inicio = inicio_actual
    return mejor_inicio

print(pos_secuencia_mas_larga([1, 2, 2, 1, 3, 4, 5]))  
print(pos_secuencia_mas_larga([5, 4, 3, 2]))           
print(pos_secuencia_mas_larga([1, 2, 3, 1, 2, 3]))  

#---------------------------------------------
print("espacio entre ejercicios!!!!!!!!!!")
#14, quiere que le diga cuantos numeros impares hay
#ej: si la lista de n´umeros es [57, 2383, 812, 246], entonces el resultado esperado ser´ıa 5 
#(los d´ıgitos impares son 5, 7, 3, 3 y 1).
#voy a hacer una funcion que me parta los numeros primero

def separar_digitos(numero: int) -> list[int]:
    digitos = []
    if numero == 0:
        return [0]
    while numero > 0:
        digitos.append(numero % 10)
        numero = numero // 10
    return digitos #no me importa si me lo devuelve de atras para adelante

def lista_de_int_separados(secuencia_dada: list[int]) -> list[int]:
    lista_nueva = []
    for numero in secuencia_dada:
        numero_separado = separar_digitos(numero)
        for digito in numero_separado: #este nuevo for es para que no me devuelva una list[list[int]]
            lista_nueva.append(digito)
    return lista_nueva

print(lista_de_int_separados([56,67,69]))

def cantidad_impares(lista: list[int]) -> int:
    cantidad = 0
    for digito in lista_de_int_separados(lista):
        if digito % 2 != 0:
            cantidad += 1
    return cantidad

print(cantidad_impares([57, 2383, 812, 246]))
#yeyyy a la primera!
    
#---------------------------------------------
#fin

