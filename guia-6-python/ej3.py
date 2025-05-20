def alguno_es_0(numero1: int, numero2: int) -> bool:
    return numero1 == 0 or numero2 == 0

print(alguno_es_0(0,0))
print(alguno_es_0(2,2))
print(alguno_es_0(0,2))
print(alguno_es_0(2,0))

def ambos_son_0(numero1: int, numero2: int) -> bool:
    return numero1 == 0 and numero2 == 0
 
print(ambos_son_0(0,0))
print(ambos_son_0(2,2))
print(ambos_son_0(0,2))
print(ambos_son_0(2,0))

def es_nombre_largo (nombre: str) -> bool:
    return len(nombre) >= 3 and len(nombre) <= 8

print(es_nombre_largo("Ro"))
print(es_nombre_largo("Juanchotaso"))
print(es_nombre_largo("Romeo"))

# Recordar que un año es bisiesto si es múltiplo de 400, o bien es múltiplo de 4 pero no de 100.
def es_bisiesto(ano: int) -> bool:
    return ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0)

print(es_bisiesto(4))
print(es_bisiesto(400))
print(es_bisiesto(2004))
print(es_bisiesto(2025))

