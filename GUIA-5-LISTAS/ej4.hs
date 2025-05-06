--lo mismo pero con caracteres
--a)
sacarEspaciosRepetidos :: [Char] -> [Char]
sacarEspaciosRepetidos [] = []
sacarEspaciosRepetidos (x:[])= [x]
sacarEspaciosRepetidos (x:y:ys) | x == ' ' && y == x = sacarEspaciosRepetidos ys
                                | otherwise = x : sacarEspaciosRepetidos (y:ys)

----------------

--me gusta que me den las funciones en orden(?)
--b) 
contarPalabrasAux :: [Char] -> Int
contarPalabrasAux [] = 0
contarPalabrasAux [x] = 1
contarPalabrasAux (x:xs) | x == ' ' = 1 + contarPalabrasAux xs
                         | otherwise = contarPalabrasAux xs
--aca lo que pasa es que si pongo muchos espacios me cuenta al que sigue como palabra, 
--ademas si pongo un espacio antes de la primer palabra me lo cuenta como palabra

sacoPrimerEspacio :: [Char] -> [Char]
sacoPrimerEspacio [] = []
sacoPrimerEspacio (x:xs) | x == ' ' = sacoPrimerEspacio xs
                         | otherwise = (x:xs)

contarPalabras :: [Char] -> Int
contarPalabras (x:xs) = contarPalabrasAux (sacoPrimerEspacio (sacarEspaciosRepetidos (xs)))

--yey

----------------

--no habia entendido que queria
--quiere que si le doy "hola mundo" le devuelva "hola" "mundo"
--osea quiero ir sacando palabras y ponerlas, quiero sacar la primera palabra y meterla
--lo odio

--e)
--quiere que le concatene todo

aplanar :: [[Char]] -> [Char]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

--ej de imput >>>>"aplanar ["hola", "que", "tal"]<<<<

--f)
--quiere lo mismo pero que le meta un espacio entre palabras

aplanarConEspacios :: [[Char]] -> [Char]
aplanarConEspacios [] = []
aplanarConEspacios (x:xs) = x ++ [' '] ++ aplanarConEspacios xs

--lo dificil fue darme cuenta que tenia que ponerle corchete al ' '

--------------

--g)
--quiere que le meta n espacios
--para esto quiero que la compu sepa cuantos meter

nEspacios :: [Char] -> Int -> [Char]
nEspacios [' '] 1 = [' ']
nEspacios [' '] n = [' '] ++ nEspacios [' '] (n-1)

aplanarConNBlancos :: [[Char]] -> Int -> [Char]
aplanarConNBlancos [] n = []
aplanarConNBlancos (x:xs) n = x ++ nEspacios [' '] n ++ aplanarConNBlancos xs n


--es parecida solo que como los espacios no estoy un numero necesito una forma de cuantifucarlos
sumarN :: [Int] -> Int -> [Int]
sumarN [] n = []
sumarN (x:xs) n = (x+n) : sumarN xs n 
