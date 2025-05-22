#Ejercicio 7. Implementar las funciones del ejercicio 6 utilizando for num in range(i,f,p):. Recordar que la función
#range para generar una secuencia de números en un rango dado, con un valor inicial i, un valor final f y un paso p. 

#1. Escribir una función que imprima los números del 1 al 10.
def del_1_al_10() -> None:
    for i in range(1,11): #el 11 no se incluye
        print(i) #no es necesario poner +=, el for se encarga de eso

del_1_al_10()


#2. Escribir una función que imprima los números pares entre el 10 y el 40.
def del_10_al_40_pares() -> None:
    for i in range(10,41,2): #en la de arriba el numero "p", era 1, aca lo aclaro pq quiero que vaya de dos en dos
        print(i)
    
del_10_al_40_pares()


#3. Escribir una función que imprima la palabra “eco” 10 veces.
def eco() -> None:
    for i in range(0,10):
        print("eco")

eco()


#4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último “Despegue”.
def cuenta_regresiva(numero: int) -> None:
    for i in range(numero, 0, -1): #porque quiero que vaya "bajando" de a uno
        print(i)
    print("despegue")

cuenta_regresiva(10)


#5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y
#“algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
#de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se
#realice un salto de año
def viaje_en_el_tiempo(ano_partida: int, ano_llegada: int) -> None:
    for i in range(ano_partida - 1, ano_llegada - 1, -1): #ano_partida -1 pq quiero que no se cuente, ano_llegada - 1 pq quiero que se cuente, -1 pq voy "bajando" de a uno
        print(f"viajo 1 ano al pasado, estamos en el ano {i}")

viaje_en_el_tiempo(20,10)


#6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
#al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada
#salto!
def viaje_aristoteles(ano_partida: int) -> None:
    for i in range(ano_partida - 20, -384 - 1, -20): #el ano_partida - 20 es porque quiero ya empezar viajando, el -384-1 (-385) es porque quiero que si llego al -384, lo incluya; y el -20 es prque voy de a 20 para abajo
        print(f"viajaste 20 anos, estamos en el ano {i}")
    print("conociste a aristoteles")

viaje_aristoteles(20)
viaje_aristoteles(16)


