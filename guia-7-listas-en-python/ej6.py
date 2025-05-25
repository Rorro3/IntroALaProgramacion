#1) quiere que le diga si es matriz, osea ver las primeras componentes
#asegura: longitud lista > 0
#asegura: longitud de la lista de los primeros componentes de cada elemento de la lista > 0
#asegura: la longitud de todas las demas listas (|s[i]|) tiene que ser igual a la de s[0]
#osea no puede pasar esto: [003129] [213] [092334] porque el segundo elemento no tiene 6 elementos

def agarrar_columna(numero_columna: int, matriz: list[list[int]]) -> list[int]:
    columna = []
    for lista in matriz:
        columna.append(lista[numero_columna])
    return columna
print(agarrar_columna(0,[[2,3,5],[7,8,9],[9,8,7]])) #me agarra la primra
#no se por que hice esta funcion, pero la hice

def matriz_valida(matriz: list[list[int]]) -> bool:
    primerfila = len(matriz[0])

    if len(matriz) == 0 or primerfila == 0:
        return False
    
    for i in matriz:
        if primerfila != len(i):
            return False
    return True
print(matriz_valida([[2,3,5],[7,8,9],[9,8,7]]))
print(matriz_valida([[2,3,5],[7,8,9],[9,8]]))

#porque si (creo que es el 5))
def trasponer(matriz_original: list[list[int]]) -> list[list[int]]:
    filas = len(matriz_original)
    columnas = len(matriz_original[0])
    matriz_traspuesta = []
    for i in range(columnas): #osea para cada i del primer elemento de cada fila armo otro corchete(?)
        nueva_fila = [] #la creo aca, porque si la creaba arriba me iba a poner todos los numeros juntos
        for j in range(filas): #me fijo la fila original (matriz_original[j]) y agarro el elemento i de esa fila (matriz_original[j][i])
            nueva_fila.append(matriz_original[j][i]) #lo meto
        matriz_traspuesta.append(nueva_fila) #lo meto
    return matriz_traspuesta
print(trasponer([[2,3,5],[7,8,9],[9,8,7]]))

#########################################
#2) quiere que le diga si cada fila esta ordenada crecientemente en una lista de bools
#reciclo
def ordenados(lista: list[int]) -> bool:
    numero = lista[0] 
    for siguiente in range(1, len(lista)):
        if lista[siguiente] <= numero: 
            return False
        numero = lista[siguiente] 
    return True

def filas_ordenadas_con_else(matriz: list[list[int]]) -> list[bool]:
    lista_bool = []
    for fila in matriz:
        if not ordenados(fila):
            lista_bool.append(False)
        else:
            lista_bool.append(True)
    return lista_bool

def filas_ordenadas_sin_else(matriz: list[list[int]]) -> list[bool]:
    lista_bool = []
    for fila in matriz:
        if not ordenados(fila):
            lista_bool.append(False)
        lista_bool.append(True)
    return lista_bool

def filas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    lista_bool = []
    for fila in matriz:
        lista_bool.append(ordenados(fila))
    return lista_bool

print(filas_ordenadas([[1,2,3],[34,43,4]]))

#todas sirven

#########################################
print("siguiente")
#3) ya lo hice mas arriba jeje:
def agarrar_columna(numero_columna: int, matriz: list[list[int]]) -> list[int]:
    columna = []
    for lista in matriz:
        columna.append(lista[numero_columna])
    return columna
print(agarrar_columna(0,[[2,3,5],[7,8,9],[9,8,7]]))
print(agarrar_columna(1,[[2,3,5],[7,8,9],[9,8,7]]))
print(agarrar_columna(2,[[2,3,5],[7,8,9],[9,8,7]]))

#########################################
print("siguiente")
#4) quiere que le diga si las columnas estan ordenadas
def columnas_ordenadas(matriz: list[list[int]]) -> list[bool]:
    lista_bool = []
    for i in range(len(matriz[0])): #agarro el len de s[0] (la cantidad de columnas, porque el requiere necesitaba una matriz valida)
        columna = agarrar_columna(i,matriz) #hasta el final de s[0]
        lista_bool.append(ordenados(columna))
    return lista_bool

print(columnas_ordenadas([[1,2,3],[2,3,4],[3,4,5]]))

#########################################
print("siguiente")
#5) trasponer
#sin usar funciones previas
def trasponer(matriz_original: list[list[int]]) -> list[list[int]]:
    filas = len(matriz_original)
    columnas = len(matriz_original[0])
    matriz_traspuesta = []
    for i in range(columnas): #osea para cada i del primer elemento de cada fila armo otro corchete(?)
        nueva_fila = [] #la creo aca, porque si la creaba arriba me iba a poner todos los numeros juntos
        for j in range(filas): #me fijo la fila original (matriz_original[j]) y agarro el elemento i de esa fila (matriz_original[j][i])
            nueva_fila.append(matriz_original[j][i]) #lo meto
        matriz_traspuesta.append(nueva_fila) #lo meto
    return matriz_traspuesta

#usando "agarrar_columna"
def trasponer2(matriz_original: list[list[int]]) -> list[list[int]]:
    matriz_traspuesta = []
    for i in range(len(matriz_original[0])):
        matriz_traspuesta.append(agarrar_columna(i,matriz_original))
    return matriz_traspuesta

print(trasponer2([[2,3,4],[7,7,7],[6,7,8]]))

