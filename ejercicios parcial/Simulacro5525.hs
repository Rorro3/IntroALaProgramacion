module Simulacro5525 where
    
---ej1
hayQueCodificar :: Char -> [(Char,Char)] -> Bool
hayQueCodificar _ [] = False
hayQueCodificar c ((x,y):xs) | c == x = True
                             | otherwise = hayQueCodificar c xs

---ej2
--si hayQueCodificar es falso, rs = 0, sino la cantidad de veces que aparece c en frase
cuantasVecesHayQueCodificar :: Char -> [Char] -> [(Char,Char)] -> Int
cuantasVecesHayQueCodificar c frase mapeo | not (hayQueCodificar c mapeo) = 0
                                          | otherwise = contador c frase

contador :: Char -> [Char] -> Int
contador _ [] = 0
contador c (x:xs) | c == x = 1 + contador c xs
                  | otherwise = contador c xs

---ej3
--quiere que le diga la letra que mas aparece en frase
--el requiere lo cumple el usuario a mi no me importa
--laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char

--como siempre lo voy a hacer primero con numeros

contarAparicionCiertaLetra :: Char -> [Char] -> Int
contarAparicionCiertaLetra _ [] = 0
contarAparicionCiertaLetra letra (x:xs) | letra == x = 1 + contarAparicionCiertaLetra letra xs
                                        | otherwise = contarAparicionCiertaLetra letra xs

letraConMasApariciones :: [Char] -> [Char] -> Char
letraConMasApariciones _ [] = ' '
letraConMasApariciones [] _ = ' '
letraConMasApariciones [letra] frase = letra
letraConMasApariciones (letra1:letra2:ls) frase | contarAparicionCiertaLetra letra1 frase >= contarAparicionCiertaLetra letra2 frase = letraConMasApariciones (letra1:ls) frase
                                                | otherwise = letraConMasApariciones (letra2:ls) frase


laQueMasHayQueCodificar :: [Char] -> [(Char, Char)] -> Char
laQueMasHayQueCodificar (frase:xs) mapeo | hayQueCodificar (letraConMasApariciones (frase:xs) (frase:xs)) mapeo = letraConMasApariciones (frase:xs) (frase:xs)
                                         | otherwise = laQueMasHayQueCodificar xs mapeo


--me da bronca porque yo la habia hecho re linda pero falla el caso en el que la letra que mas aparece no esta en mapeo
--ahi lo arregle
--en la solucion del jtp lo hace en dos pasos !!!!!
--la mia esta bien pero el jtp lo hizo sin esas funciones auxiliares, solo usando las anteriores del examen
--moraleja(?) USAR LAS ANTERIORES
 

