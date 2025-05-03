--longitud de una lista
longitud :: [t] -> Int
longitud [x] = 1
longitud (x:xs) = 1 + longitud xs

--va sumando 1 hasta que la longitud de la cola sea 1, ahi para

----------------------

--quiere el ultimo elemento de la lista
ultimo :: [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs

--osea va recortando la lista hasta quq quede uno solo

----------------------

--quiere toda la lista menos el ultimo elemento
principio :: [t] -> [t]
principio [x] = []
principio (x:xs) = x : principio xs

--osea le meto el primer elemento y asi hasta que quede uno solo (a ese no lo meto)

---------------------

--dar vuelta la lista
reverso :: [t] -> [t]
reverso [x] = [x]
reverso (x:xs) = reverso xs ++ [x]

--osea meto el principio atras y el principio de la lista sin ese principio mas atras

--------------------


