--se fija si un numero pertenece a fibonacci
--fibonacci
fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)

esFibonacciAux :: Int -> Int -> Bool
esFibonacciAux n i | fibonacci i > n = False -- me habbia faltado esto
                   | n == fibonacci i = True
                   | otherwise = esFibonacciAux n (i+1)

--hay dos casos base, uno para que sepa cuando parar a la i
--si no pongo el primer caso, cuando es falso se cuelga porque sigue hasta el inf
--si no pongo el segundo caso no tengo la igualdad que me pide

esFibonacci :: Int -> Bool
esFibonacci n = esFibonacciAux n 0

--empieza del 0 porque el 0 es el menor de fibonacci