ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = todosDigitosIguales (sacoUltimoDigito n) && ultimoDigito n == ultimoDigito (sacoUltimoDigito n)