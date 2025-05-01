--quiere que le diga si todos los digitos de un numero n son iguales
--primero voy a hacer funciones que me saquen los digitos: el primero y el ultimo
--como que quiero ir achurando el numero por delante y por detras

ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

--digitosIguales :: Int -> Bool
--digitosIguales n | n < 10 = True
              --   | n >= 10 && n < 100 = ultimoDigito n == sacoUltimoDigito n
               --  | n > 100 = digitosIguales (sacoUltimoDigito n) 

--en esta funcion si le doy 11112 me dice true porque no se fija el ultimo digito
--para esto, pongo un && 

digitosIguales :: Int -> Bool
digitosIguales n | n < 10 = True
                 | n >= 10 && n < 100 = ultimoDigito n == sacoUltimoDigito n
                 | n > 100 = ultimoDigito n == ultimoDigito (sacoUltimoDigito n) && digitosIguales (sacoUltimoDigito n)
 