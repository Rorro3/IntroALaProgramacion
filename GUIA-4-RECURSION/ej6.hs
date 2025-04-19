ultimoDigito :: Int -> Int
ultimoDigito n = mod n 10

sacoUltimoDigito :: Int -> Int
sacoUltimoDigito n = div n 10

todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      | otherwise = todosDigitosIguales (sacoUltimoDigito n) && ultimoDigito n == ultimoDigito (sacoUltimoDigito n)
    
--cuando hago todosDigitosIguales (sacoUltimoDigito n) se fija si el numero que queda es menor a 10
--cuando hago ultimoDigito n == ultimoDigito (sacoUltimoDigito n) se fija si el ultimo digito del numero es igual al que le seguiria si sigo sacando digitos
--la primera siempre se va a complir si sigo sacando digitos, por eso quiero que se cumplan las dos a la vez
    