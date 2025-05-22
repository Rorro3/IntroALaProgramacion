#1. Escribir una función que imprima los números del 1 al 10.
def del_1_al_10() -> None:
    i = 1
    while i <= 10:
        print(i)
        i += 1

del_1_al_10()
#osea la variable es local (pasada por valor???)

#2. Escribir una función que imprima los números pares entre el 10 y el 40.
def del_10_al_40_pares() -> None:
    i = 10
    while i <= 40:
        print(i)
        i += 2
    
del_10_al_40_pares()

def eco() -> None:
    i = 0
    while i < 10:
        print("eco")
        i += 1

eco()

#4. Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último “Despegue”.
def cuenta_regresiva(numero: int) -> None:
    i = numero
    while i > 0:
        print(i)
        i -= 1
    print("despegue")

cuenta_regresiva(40)

#RECUERDO QUE EL i NO ESTA PEGADO A LO QUE PONGO, CORTE NO ES EL MISMO NUMERO, YO LO IGUALO, PERO DESPUES AACTUA COMO NO SE, UN COMPAS ESOS DE MUSICA PARA MARCAR EL RITMO


#5. Hacer una función que monitoree un viaje en el tiempo. Dicha función recibe dos parámetros, “el año de partida” y
#“algún año de llegada”, siendo este último parámetro siempre más chico que el primero. El viaje se realizará de a saltos
#de un año y la función debe mostrar el texto: “Viajó un año al pasado, estamos en el año: <año>” cada vez que se
#realice un salto de año
def viaje_en_el_tiempo(ano_partida: int, ano_llegada: int) -> None:
    i = 1
    j = ano_partida - 1
    while i <= ano_llegada:
        print(f"viajo {i} anos al pasado, estamos en el ano {j}")
        i += 1
        j -= 1

viaje_en_el_tiempo(20,10)

#6. Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano
#al 384 a.C., donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada
#salto!
def viaje_aristoteles(ano_partida: int) -> None:
    i = ano_partida - 20 #pq quiero ya empiece a viajar, no pierdas tiempo!
    j = 20
    while i >= -384:
        print(f"viajaste {j} anos al pasado!, estamos en el ano {i}")
        i -= 20
        j += 20
    print("conociste a aristoteles")

viaje_aristoteles(20)
viaje_aristoteles(30)