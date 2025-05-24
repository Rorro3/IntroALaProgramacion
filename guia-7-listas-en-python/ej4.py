#Ejercicio 4. 
#Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. 
#Asumir que el saldo inicial es 0. 
#Las tuplas tienen una letra que nos indica el tipo de movimiento “I” para ingreso de dinero 
#y “R” para retiro de dinero, y ademas el monto de cada operacion. 
#Por ejemplo, si la lista de tuplas es [(‘‘I’’,2000), (‘‘R’’, 20),(‘‘R’’, 1000),(‘‘I’’, 300)] entonces el saldo actual es 1280.

#quiero hacer una funcion que solo agarre los ingresos (los numeros que acompanan a la I)
#y otra que solo agarre los retiros
#despues sumo todo

def solo_ingresos(lista_tuplas: list[tuple[str,int]]) -> list[int]:
    lista_final = []
    nueva_lista = []
    for ingreso in lista_tuplas:
        if ingreso[0] == "I":
            nueva_lista.append(ingreso)

    for I in nueva_lista:
        lista_final.append(I[1])
        
    return lista_final
print(solo_ingresos([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

def solo_retiros(lista_tuplas: list[tuple[str,int]]) -> list[int]:
    lista_final = []
    nueva_lista = []
    for retiro in lista_tuplas:
        if retiro[0] == "R":
            nueva_lista.append(retiro)

    for R in nueva_lista:
        lista_final.append(R[1])
        
    return lista_final
print(solo_retiros([("I",2000), ("R", 20),("R", 1000),("I", 300)]))

def saldo_actual(lista_tuplas: list[tuple[str,int]]) -> int:
    ingresos_totales = 0
    retiros_totales = 0
    ingresos = solo_ingresos(lista_tuplas)
    retiros = solo_retiros(lista_tuplas)
    for I in ingresos:
        ingresos_totales += I
    for R in retiros:
        retiros_totales += R
    return ingresos_totales - retiros_totales
print(saldo_actual([("I",2000), ("R", 20),("R", 1000),("I", 300)]))