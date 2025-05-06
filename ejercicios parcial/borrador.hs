contarAparicionCiertoNumero :: Int -> [Int] -> Int
contarAparicionCiertoNumero _ [] = 0
contarAparicionCiertoNumero numero (x:xs) | numero == x = 1 + contarAparicionCiertoNumero numero xs
                                          | otherwise = contarAparicionCiertoNumero numero xs
                            
contarNumeroBla :: [Int] -> [Int] -> Int
contarNumeroBla _ [] = 0
contarNumeroBla [] _ = 0
contarNumeroBla [n] lista = n
contarNumeroBla (n1:n2:ns) lista | contarAparicionCiertoNumero n1 lista >= contarAparicionCiertoNumero n2 lista = contarNumeroBla (n1:ns) lista
                                 | otherwise = contarNumeroBla (n2:ns) lista


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