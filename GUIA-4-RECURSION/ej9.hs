--quiere que le diga si es capicua
ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

primerDigito :: Int -> Int
primerDigito n | n < 10 = n
               | n >= 10 && n < 100 = sacoUltimoDigito n
               | n > 100 = primerDigito (sacoUltimoDigito n)

sacoPrimerDigito :: Int -> Int
sacoPrimerDigito n | n < 10 = n
                   | otherwise = mod n (10 ^ (cantidadDigitos n - 1))

cantidadDigitos :: Int -> Int
cantidadDigitos n | n < 10 = 1
                  | otherwise = 1 + cantidadDigitos (div n 10)

--me robe todo esto de los ejs anteriores capaz lo uso

esCapicua :: Int -> Bool
esCapicua n | n < 10 = True
            | n >= 10 && n < 100 = primerDigito n == ultimoDigito n
            | otherwise = primerDigito n == ultimoDigito n && esCapicua (sacoPrimerDigito (sacoUltimoDigito n))

