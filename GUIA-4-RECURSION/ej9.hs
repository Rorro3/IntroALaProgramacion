--ver si un numero es capicua
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

primerDigito :: Int -> Int
primerDigito n | n < 10 = n
               | otherwise = primerDigito (sacoUltimoDigito n)

cantidadDigitos :: Int -> Int
cantidadDigitos n | n < 10 = 1
                  | otherwise = 1 + cantidadDigitos (sacoUltimoDigito n) 

sacarPrimeroYultimo :: Int -> Int
sacarPrimeroYultimo n = eliminarUnidades (mod n (10 ^ (cantidadDigitos n - 1)))

eliminarUnidades :: Int -> Int
eliminarUnidades x = div x 10


esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | ultimoDigito n == primerDigito n = True
            | otherwise = ultimoDigito n == primerDigito n && esCapicua (sacarPrimeroYultimo n)


--lo mas dificil de aca fue la funcion sacarPrimeroYultimo ngl
--basicamente porque no hice el ej2
            