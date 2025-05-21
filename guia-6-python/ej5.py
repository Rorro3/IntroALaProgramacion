#devuelve el doble del número en caso de ser par y el mismo número en caso contrario.
def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        return numero * 2
    else:
        return numero
    
print(devolver_el_doble_si_es_par(3))
print(devolver_el_doble_si_es_par(2))

#devuelve el mismo número si es par, y si no, el siguiente. Analizar distintas formas de implementación (usando un if-then-else y dos if). ¿Todas funcionan?

def devolver_valor_si_es_par_si_no_el_que_sigue(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    else:
        return numero + 1
#esta con if else

def la_misma_pero_dosif(numero: int) -> int:
    if numero % 2 == 0:
        return numero
    if numero % 2 != 0:
        return numero + 1
#esta con dos ifs
    
print(devolver_valor_si_es_par_si_no_el_que_sigue(5))
print(devolver_valor_si_es_par_si_no_el_que_sigue(4))

print(la_misma_pero_dosif(5))
print(la_misma_pero_dosif(4))
#aca las dos sirven, pero supongo que en un caso en el que haya una tercera condicion en el de dos ifs, que incluya si es par o no 
#mas otra cosa, me devolveria lo que diga el primer if en el que se cumpla la condicion

#en otro caso, devolver el número original. Analizar distintas formas de implementación (usando un if-then-else, dos if, o alguna opción de operación lógica). ¿Todas funcionan? ¿Cuál es el resultado si la entrada es 18?
def devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 3 == 0: 
        return numero * 2
    elif numero % 9 == 0:
        return numero * 3
    else:
        return numero
    
print(devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiplo9(18))
#aca me dio el primero que le aparecio

def condosif(numero: int) -> int:
    if numero % 3 == 0:
        return numero * 2
    if numero % 9 == 0:
        return numero * 3
    else:
        return numero
    
print(condosif(18))
#aca tambien, supongo que en las dos, si pongo el %9 antes, me va a devolver numero*3

#peeero con un print, que no es algo que returnea:
def ejemplo_sin_return(numero: int) -> None:
    if numero % 3 == 0:
        print("Múltiplo de 3")
    if numero % 9 == 0:
        print("Múltiplo de 9")
    else:
        print("bleh")

ejemplo_sin_return(18)
# :O es porque leyo los dos ifs

def ejemplo_sin_return_con_elif(numero: int) -> None:
    if numero % 3 == 0:
        print("Múltiplo de 3")
    elif numero % 9 == 0:
        print("Múltiplo de 9")
    else: 
        print("bleh")

ejemplo_sin_return_con_elif(18)
#aca paro a penas vio uno que cumple

def lindo_nombre(nombre: str) -> None:
    if len(nombre) >= 5:
        print("tu nombre tiene muchas letras!")
    else:
        print("tu nombre tiene menos de 5 caracteres")

lindo_nombre("Rome")
lindo_nombre("Juanchotaso")

#imprime por pantalla “Menor a 5” si el número es menor a 5, “Entre 10 y 20” si el número está en ese rango y “Mayor a 20” si el número es mayor a 20.

def elRango(numero: int) -> None:
    if numero < 5:
        print("menor a 5")
    elif numero >= 10 and numero <= 20:
        print("entre 10 y 20")
    elif numero > 20:
        print("mayor a 20")
#uso elif porque hay un caso sin contemplar (entre 5 y  10) y si pongo todos ifs me iba a devolver mas de un resultado si habia algo que cumpliera mas de dos cosas (en este caso son todos disjuntos, pero bueno para practicar)

elRango(20)
elRango(67)
elRango(4)
elRango(9)

#6. En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan
#a los 65 años. Quienes son menores de 18 años se deben ir de vacaciones junto al grupo que se jubila. Al resto de
#las personas se les ordena ir a trabajar. Implemente una función que, dados los parámetros de sexo (F o M) y edad,
#imprima la frase que corresponda según el caso: “Andá de vacaciones” o “Te toca trabajar”.

def jubilados(edad: int, sexo: str) -> str:
    if edad < 18:
        return "anda de vacaciones"
    if sexo == "F" and edad >= 60:
        return "anda de vacaciones"
    if sexo == "M" and edad >= 65:
        return "anda de vacaciones"
    return "anda a trabajar"
#aca como use muchos ifs (porque eran casos disjuntos), tengo que usar return si solo quiero que me returnee una cosa
#no puedo usar un else en este caso porque solo se aplica al ultimo if (o el que tenga identado igual)
#si queria usar else, tenia que poner elif

print(jubilados(19, "M"))


    


