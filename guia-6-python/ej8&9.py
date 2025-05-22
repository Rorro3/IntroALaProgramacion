#Ejercicio 8. Realizar la ejecución simbólica de los siguientes códigos:

#1 
x1 = 5
y1 = 7
x1 = x1 + y1
print(x1)

#2
x2 = 5
y2 = 7
z2 = x2 + y2
y2 = z2 * 2
print(y2)

#3 
x3 = 5
y3 = 7
x3 = "hora"
y3 = x3 * 2
print(y3) #re otaku

#4
x4 = False
res = not(x4)
print(res)

#5 
x5 = False
x5 = not(x5)
print(x5)

#6 x=True ; y=False ; res=x and y; x = res and x
x6 = True
y6 = False
res6 = x6 and y6
x6 = res6 and x6
print(x6)


#Ejercicio 9. Sea el siguiente código:
def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g + 1
    return x + g

#1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
#yo supongo que sera 2
print(ro(1)) #yeyyy

#2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
#yo supongo que sera 2 al primer print
#al segundo 3
#al tercero 4
#como dice return, cada vez que imprima va a ser algo disitnto ^^
for _ in range(3):
    print(rt(1, 0))

#supuse mal! porque yo supuse que era por valor el resultado, y en realidad es por referencia!
#osea que cada vez que la funcion termina, no se guarda nada, y vuelve a empezar como nueva
#osea que siempre da 2 porque no se guarda el valor de g
