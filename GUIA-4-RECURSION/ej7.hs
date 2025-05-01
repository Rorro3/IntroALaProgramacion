--quiere que dado un numero n y una posicion m, le devuelva el numero de n que esta en la posicion m
--ej: 2234 3 = 3
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

--en realidad estoy pensando en sacarle el primer digito tantas veces como me lo pida
primerDigito :: Int -> Int
primerDigito n | n < 10 = n
               | n >= 10 && n < 100 = sacoUltimoDigito n
               | n > 100 = primerDigito (sacoUltimoDigito n)

--no me sirve pero me la guardo para despues

cantidadDigitos :: Int -> Int
cantidadDigitos n | n < 10 = 1
                  | otherwise = 1 + cantidadDigitos (div n 10)


sacoPrimerDigito :: Int -> Int
sacoPrimerDigito n | n < 10 = n
                   | otherwise = mod n (10 ^ (cantidadDigitos n - 1))

--esta no se me ocurriria xd, osea 10^3 = 1000, 10^4 = 10000 :o

--y pero ahora que hago??!???!?
--voy achurando n hasta que se iguale a la cantidad de digitos que me pide m 
iesimoDigito :: Int -> Int -> Int
iesimoDigito n m | cantidadDigitos n == m = ultimoDigito n
                 | otherwise = iesimoDigito (sacoUltimoDigito n) m

--la tipica