--a)
--quiere que dada una lista sume el primero con el segundo, y a esa suma la sume con el tercero y asi...

sumaAcumulada :: (Num t) => [t] -> [t]
sumaAcumulada [] = []
sumaAcumulada [x] = [x]
sumaAcumulada (x:y:ys) = [x] ++ sumaAcumulada ((x+y):ys)

-------------------

--b)
--quiere que a cada numero de la lista lo descomponga en primos
--tengo que hacer cosas con primos primero
menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde n 2

menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde n m | n == m = n
                      | n/= m && mod n m == 0 = m
                      | otherwise = menorDivisorDesde n (m+1)

factoresPrimos :: Int -> [Int]
factoresPrimos 1 = []
factoresPrimos n = [menorDivisor n] ++ factoresPrimos (div n (menorDivisor n))

descomponerEnPrimos :: [Int] -> [[Int]]
descomponerEnPrimos [] = []
descomponerEnPrimos (x:xs) = [factoresPrimos x] ++ descomponerEnPrimos xs

--este fue divertido
--acordate de poner [] cuando metes algo para ++ (si no es la misma funcion aplicada a listas)