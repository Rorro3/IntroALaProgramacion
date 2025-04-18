--sumaImpares :: Integer -> Integer que sume los primeros n numeros impares. en N
--Por ejemplo: sumaImpares 3 ❀ 1+3+5 ⇝ 9.

sumaImpares :: Int -> Int
sumaImpares n = n*n

--porque justo me di cuenta xd
--yo quiero que sea recursiva

sumaImparesRecursiva :: Int -> Int
sumaImparesRecursiva n | n == 1 = 1
                       | otherwise = sumaImparesRecursiva (n-1) + 2*n - 1

--2*n - 1 seria como la formula cerrada para el n-esimo impar, porque es basicamente el n-esimo par, menos 1(?)

