--sumatoria que suma todos los elementos de la lista

sumatoria :: (Num t) => [t] -> t
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:xs) = x + sumatoria xs

--productoria que te multiplica todos los elementos de la lista

productoria :: (Num t) => [t] -> t
productoria [] = 0
productoria [x] = x 
productoria (x:xs) = x * productoria xs

--maximo 
--como requiere una lista de long mayor a 0, no hago nada con el caso vacio

maximo :: [Int] -> Int
maximo [x] = x
maximo (x:y:ys) | x > y = maximo (x:ys)
                | otherwise = maximo (y:ys)

--sumar n en todos los elementos de la seq

sumarN :: [Int] -> Int -> [Int]
sumarN [] n = []
sumarN (x:xs) n = (x+n) : sumarN xs n 

--sumar el primer elemento

sumarElPrimero :: [Int] -> [Int]
sumarElPrimero [] = []
sumarElPrimero (x:xs) = sumarN (x:xs) x

--ahora sumar el ultimo

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo [] = []
sumarElUltimo (x:xs) = sumarN (x:xs) (ultimo xs)

ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--quiere que le devuelva una lista solo con los elementos pares

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

--lo mismo pero con multiplos de un n dado

multiplosDeN :: [Int] -> Int -> [Int]
multiplosDeN [] _ = []
multiplosDeN (x:xs) n | mod x n == 0 = x : multiplosDeN xs n
                      | otherwise = multiplosDeN xs n

--ordenarlos de menor a mayor

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar xs = minimo xs : ordenar (quitar xs (minimo xs))

--aca no estoy usando (x:xs) porque las otras dos funciones ya lo tienen en cuenta

minimo :: [Int] -> Int
minimo [x] = x
minimo (x:y:ys) | x < y = minimo (x:ys)
                | otherwise = minimo (y:ys)

quitar :: (Eq t) => [t] -> t -> [t]
quitar [] _ = []
quitar (x:xs) elemento | elemento == x = xs 
                       | otherwise = x: quitar xs elemento