import math

#quiero saludar a alguien
def hola_alguien (nombre: str) -> None:
    print("Hola,",nombre)

hola_alguien("Ro")
hola_alguien("Juanchotaso")

def raizcuadradade (numero: int) -> int:
    return math.sqrt(numero)

print(raizcuadradade(4))

def fahrenheit_a_celsius(temp_far: float) -> float:
    return ((temp_far - 32) * 5)/9

print(fahrenheit_a_celsius(32))
print(fahrenheit_a_celsius(40))

def imprimirdosveces(estribillo: str) -> None:
    print(estribillo * 2)

imprimirdosveces("It started with a whisper\nAnd that was when I kissed her\nAnd then she made my lips hurt\nI could hear the chit-chat\nTake me to your love shack\nMama's always gotta back-track\nWhen everybody talks back\n")

def esmultiploden(n: int, m: int) -> bool:
    return (n % m == 0)

print(esmultiploden(10,2))
print(esmultiploden(10,3))

def espar(n: int) -> bool:
    return n % 2 == 0

print(espar(4))
print(espar(7))

def cantidad_de_pizzas(comensales: int, min_cant_porciones: int) -> int:
    return math.ceil((comensales * min_cant_porciones)/8)

print(cantidad_de_pizzas(4,7))
print(cantidad_de_pizzas(4,2))
print(cantidad_de_pizzas(1,2))
#el ceil me lo rendondea arriba, porque no puedo comer 0 pizzas 

