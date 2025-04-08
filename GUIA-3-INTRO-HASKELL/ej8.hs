--una funcion que compara
--necesito una que me de la suma de los ultimos dos digitos porque quiero comparar esos
modulo :: Int -> Int
modulo n | n >= 0 = n
         | otherwise = - n

sumaultimosdosdigitos :: Int -> Int
sumaultimosdosdigitos x = mod (modulo x) 10 + mod (div (modulo x) 10) 10

comparar :: Int -> Int -> Int
comparar a b | sumaultimosdosdigitos a < sumaultimosdosdigitos b = 1
             | sumaultimosdosdigitos a > sumaultimosdosdigitos b = -1
             | sumaultimosdosdigitos a == sumaultimosdosdigitos b = 0
