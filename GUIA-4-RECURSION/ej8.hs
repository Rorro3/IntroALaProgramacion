--suma de digitos de un numero natural
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10


sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito n + sumaDigitos (sacoUltimoDigito n)

--osea el caso base va a ser cuando el numero tenga un solo digito porque no hay nada mas que sumar
--cuando tenga mas de un digito va a sumar el ultimo digito mas el numero sin ese digito,
--la recursion para cuando n tenga un solo digito