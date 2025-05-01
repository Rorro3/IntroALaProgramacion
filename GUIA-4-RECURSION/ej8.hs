sumaDigitos :: Int -> Int
sumaDigitos n | n < 10 = n
              | otherwise = ultimoDigito n + sumaDigitos (sacoUltimoDigito n)
              
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

--nada, este fue facil