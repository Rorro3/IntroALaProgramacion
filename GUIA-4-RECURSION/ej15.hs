--lo mismo que el 13 pero con p/q

sumatoriaDentro :: Int -> Int -> Float
sumatoriaDentro n 1 = fromIntegral n
sumatoriaDentro n m = fromIntegral (div n m) + sumatoriaDentro n (m-1) 
--aca el caso base va en funcion de n

sumatoriaFuera :: Int -> Int -> Float
sumatoriaFuera 0 m = 0
sumatoriaFuera n m = sumatoriaDentro n m + sumatoriaFuera (n-1) m
--aca el caso base va en funcion de m