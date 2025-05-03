--a) menor divisor (que no sea 1, asi que si es primo, es el mismo)
--osea voy a buscar desde el 2 (el numero natural que le sigue al 1) y ver si lo divide
--si 2 divide, listo
--si 2 no divide, pasa al 3 y asi
--termina cuando llego al mismo numero que le paso
menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde numero divisor | numero == divisor = numero
                                 | numero /= divisor && mod numero divisor == 0 = divisor
                                 | otherwise = menorDivisorDesde numero (divisor + 1)

--y ahora es lo mismo que la anterior pero desde el 2, porque sino siempre me daria 1
menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde n 2

--b) ver si un numero es primo
esPrimo :: Int -> Bool
esPrimo 1 = False
esPrimo n = menorDivisor n == n

--c) ver si dos numeros son coprimos osea (n:m) = 1
--tengo casos:
--caso n == m = False
--caso n y m primos = True
--caso n primo y n no divide a m (o viceversa) = True
--caso mas dificil

coprimos :: Int -> Int -> Bool
coprimos n m | n == 1 || m == 1 = True
             | esPrimo n && esPrimo m = True
             | mod n m == 0 || mod m n == 0 = False
             | mod m (menorDivisor n) == 0 = False
             | mod n (menorDivisor m) == 0 = False
             | otherwise = coprimos n (div m (menorDivisor m))

--creo que esta todo cubierto
--el caso base para la recursion seria cuando algun numero es 1, pq todo numero es coprimo con 1

--d) quieren el n-esimo primo
--no puedo hacer una formulita asi simple como para los impares que seria sumarle de a 2 al 1
--entonces hago una funcion que haga esto, osea me de el primo que sigue
siguientePrimo :: Int -> Int
siguientePrimo n | esPrimo (n+1) = n + 1
                 | otherwise = siguientePrimo (n+1)

nesimoPrimo :: Int -> Int
nesimoPrimo 1 = 2
nesimoPrimo n = siguientePrimo (nesimoPrimo (n-1))

--osea hago el siguiente primo del anterior que seria el mismo