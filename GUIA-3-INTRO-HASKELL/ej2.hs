--una funcion que tome un numero entero y me de su valor absoluto
absoluto :: Int -> Int
absoluto x | x < 0 = -x
           | otherwise = x
--ojo en la terminar hay que poner el numero entre parentesis si es negativo, sino esta tomando otra cosa

--maximo absoluto que me tome dos enteros y me diga cual es mayor
maximoabsoluto :: Int -> Int -> Int
maximoabsoluto x y | x >= y = x
                   | otherwise = y

--maximo3 que me agarre tres enteros y me diga cual es el mayor
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x >= y && x >= z = x
              | y >= z = y
              | otherwise = z
--algo muy lindo de haskell y los lenguajes funcionales es que en el caso de las guardas, van de "arriba hacia abajo"

--ej d, me da dos numeros racionales y me dice si alguno es cero
algunoes0 :: Float -> Float -> Bool
algunoes0 x y | x == 0 || y == 0 = True
              | otherwise = False
--tengo dudas de si siempre hay que poner el otherwise
--con pattern matching seria funcion 0 x = true y lo mismo con los otros tres casos

--ej e
amboson0 :: Float -> Float -> Bool
amboson0 x y | x == 0 && y == 0 = True
             | otherwise = False

--ej f dos numeros reales me dicen si estan en los intervalos dados, ahora no entendi si tienen que estar en alguno de esos
--o justo en el mismo de esos
--lo hice como si estuvieran en el mismo de esos 3
mismointervalo :: Float -> Float -> Bool
mismointervalo x y | x <= 3 && y <= 3 = True
                   | 3 < x && x <= 7 && 3 < y && y <= 7 = True
                   | x > 7 && y > 7 = True
                   | otherwise = False

--ej g sumar enteros, pero si dos son iguales no los suma
sumadistintos :: Int -> Int -> Int -> Int
sumadistintos x y z | x == y && x == z = x
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = y + x
                    | otherwise = x + y + z
--otra vez no hay que hacer todos los casos con &&, solo con darle prioridad en las guardas a los que mas abarcan, basta

--ej h dos numeros naturales, si el primero es multiplo del segundo
esmultiplode :: Int -> Int -> Bool
esmultiplode x y | mod x y == 0 = True
                 | otherwise = False

--ej i dado un numero entero, extrae su digito de las unidades (osea el ultimo numero :p)
digitounidades :: Int -> Int
digitounidades x = mod (absoluto x) 10
--porque quiero la congruencia mod 10 que me va a dar un numero del 0 al 9 que es un numero que esta en las unidades

--ej j lo mismo pero con el digito de las decenas
digitodecenas :: Int -> Int
digitodecenas x = div (mod (absoluto x) 100) 10
--sirve porque el div toma la parte entera, osea con el mod estoy agarrando un numero del 0 al 99 
--y al dividirlo por 10 solo agarra "cuantos 10 necesito para llegar a ese numero"

