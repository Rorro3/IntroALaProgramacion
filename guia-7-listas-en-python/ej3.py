#1)Ejercicio 3. Implementar una funci´on para conocer el estado de aprobaci´on de una materia a partir de las notas obtenidas por un/a alumno/a
#la lista de notas es no vacia
#van del 0 al 10
#asegura: res = 1 si todas las notas son >= 4 and promedio >= 7
#res = 2 si todas las notas son >= 4 and promedio >= 4 and promedio < 7
#res = 3 si alguna nota es menor a 4 or el promedio es menor a 4
#def resultadoMateria(lista: list[int]) -> int:
 #   for nota in lista:

def promedio(lista: list[int]) -> int:
    suma_actual = 0
    cantidad_notas = 0
    for nota in lista:
        cantidad_notas += 1
        suma_actual += nota
    return suma_actual // cantidad_notas

print(promedio([7,7,7]))
print(promedio([7,10,7]))

def mayores_o_iguales_a_cuatro(lista: list[int]) -> bool:
    contador = 0
    for nota in lista:
        if nota >= 4:
            contador += 1
    return contador == len(lista)

print(mayores_o_iguales_a_cuatro([4,5,6,1]))
print(mayores_o_iguales_a_cuatro([4,5,6,8]))

def resultadoMateria(lista: list[int]) -> int:
    prom = promedio(lista) #esto es por si trabajaba con funciones con mucha sobrecarga, que no las evalue tantas veces
    if not(mayores_o_iguales_a_cuatro(lista)) or prom < 4:
        return 3
    elif prom < 7: 
        return 2
    else: 
        return 1
#en el elif solo pongo el caso que se "mantiene igual pero con unos cambios (prom)"
#porque se mantiene casi igual en el caso prom < 7, porque en el de arriba al ser < 4 siempre se cumplia
#no pongo en el elif que quiero prom >= 4, porque ya se cumple en el caso en el que mayores_o_iguales_a_cuatro sea true
#el de mayores_o_iguales_a_cuatro es disjunto, asi que ya no lo pongo
print(resultadoMateria([4,5,6,1,4]))
print(resultadoMateria([4,4,6,4,4]))       
print(resultadoMateria([7,7]))




