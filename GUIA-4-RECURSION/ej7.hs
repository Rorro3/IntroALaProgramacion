--tengo un numero n que puede ser 1293892, pongo un numero i que indica la posicion de un numero,
--quiero que me devuelva el numero en esa posicion
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

cantidadDigitos :: Int -> Int
cantidadDigitos n | n < 10 = 1
                  | otherwise = 1 + cantidadDigitos (sacoUltimoDigito n) 


iesimoDigito :: Int -> Int -> Int
iesimoDigito n i | i == cantidadDigitos n = ultimoDigito n
                 | otherwise = iesimoDigito (sacoUltimoDigito n) i

--voy sacando digitos hasta que la longitud de n sea igual a i