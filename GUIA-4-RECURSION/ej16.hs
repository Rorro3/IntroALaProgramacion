--a) menor divisor
menorDivisorAux :: Int -> Int -> Int
menorDivisorAux n i | mod n i == 0 = i
                    | otherwise = menorDivisorAux n (i+1)

menorDivisor :: Int -> Int
menorDivisor n = menorDivisorAux n 2
               
--LE TUVE QUE PREGUNTAR A CHATGPT, SI
--es que me cuesta cuando la recursion sube(??)
--aca lo importante es preguntarse, "si pongo (i+1), va a seguir infinitamente?"
--y justo en este caso no, porque si o si va a encontrar un numero
--en el peor caso es primo y es el mismo

esPrimo :: Int -> Bool
esPrimo n = menorDivisor n == n

--lo bueno es que ya puedo ver si un numero es primo
--lets go encriptacion(???)

--ahora con coprimos deberia hacer una recursion doble hmm
menorDosNumeros :: Int -> Int -> Int
menorDosNumeros x y | x >= y = y
                    | otherwise = x

coprimosAux :: Int -> Int -> Int -> Bool
coprimosAux n m i | i > menorDosNumeros n m = True 
                  | mod n i == 0 && mod m i == 0 = False
                  | otherwise = coprimosAux n m (i+1)
--lo mismo que la otra >:c
--mecuesta el caso base
--basicamente se fija si divide a los dos al mismo tiempo
--el caso base seria si es mayor al menor, que si me lo ponia a pensar yo nervioso en un parcial no me salia

coprimos :: Int -> Int -> Bool
coprimos n m = coprimosAux n m 2