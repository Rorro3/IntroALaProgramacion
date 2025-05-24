#1) quiere que en las posiciones pares de la lista les ponga un 0, en las impares que no haga nada
#ES INOUT, OSEA LA MISMA LISTA SE MODIFICA

def ceros_en_pos_pares(lista: list[int]) -> None:
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista[i] = 0 #no hay else, porque en caso contrario no pasa nada
    #return lista no es necesario el return porque no returnea nada, osea cambia la lista nomas (en un parcial creo que cagaba)

lista = [9,8,92,9]
ceros_en_pos_pares(lista)
print(lista)


#2)lo mismo pero sin inout (esta la hice antes que la #1)
def ceros_en_pos_pares_2(lista: list[int]) -> list[int]:
    i = 0
    lista_nueva = []
    for i in range(0, len(lista)):
        if i % 2 == 0:
            lista_nueva.append(0)
        else:
            lista_nueva.append(lista[i]) 
    return lista_nueva

print(ceros_en_pos_pares_2([1,2,3,4]))


print("siguienteeeeeeeeeeeeeeeeeeeeeeeeee")
#3) Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. 
#No se agregan espacios, sino que borra la vocal y concatena a continuaci´on.
#vuelvo a traer la funcion es_vocal
vocales: str = "aeiouAEIOU"
def es_vocal(letra: str) -> bool:
    return letra in vocales

def sin_vocales(palabra: str) -> str:
    nueva_palabra = ""
    for letra in palabra:
        if not(es_vocal(letra)):
            nueva_palabra += letra
    return nueva_palabra

print(sin_vocales("romeo"))

print("siguienteeeeeeeeeeeeeeeeeeeeeeeeee")
#4) quiere que reemplace las vocales con un _
def reemplaza_vocales(palabra: str) -> str:
    nueva_palabra = ""
    for letra in palabra:
        if not(es_vocal(letra)):
            nueva_palabra += letra
        else:             #no uso elif porque ya cumpli todos los casos posibles: es vocal o no
            nueva_palabra += "_"
    return nueva_palabra

print(reemplaza_vocales("romeo"))

print("siguienteeeeeeeeeeeeeeeeeeeeeeeeee")
#4) quiere que le de vuelta la string
def da_vuelta_str(palabra: str) -> str:
    nueva_palabra = ""
    indice = -1
    contador = 0
    while contador < len(palabra):
        nueva_palabra += (palabra[indice])
        indice -= 1
        contador += 1
    return nueva_palabra

print(da_vuelta_str("romeo"))

#con un for era mas compacto PERO NO SE POR QUE SE ME HACE MAS FACIL EL WHILE

def da_vuelta_string_for(palabra: str) -> str:
    nueva_palabra = ""
    indice = -1
    for contador in range(0, len(palabra)):
        nueva_palabra += (palabra[indice])
        indice -= 1
    return nueva_palabra

print(da_vuelta_string_for("juanchotaso"))

print("siguienteeeeeeeeeeeeeeeeeeeeeeeeee")
#6) quiere que elimine las letras repetidas

#funcion pertenece
def pertenece_letra(letra: str, palabra: str) -> bool:
    return letra in palabra

def eliminar_repetidos(palabra: str) -> str:
    palabra_repuesto = ""
    palabra_nueva = ""
    for letra in palabra:
        if not(pertenece_letra(letra, palabra_repuesto)):
            palabra_repuesto += letra
            palabra_nueva += letra #else no hago nada
    return palabra_nueva

print(eliminar_repetidos("romeo"))

            
        
            





