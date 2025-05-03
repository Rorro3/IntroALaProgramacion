--quiere que le diga si un elemento pertenece a una lista
pertenece :: (Eq t) => [t] -> t -> Bool
pertenece [] _ = False
pertenece (x:xs) elemento | x == elemento = True
                          | otherwise = pertenece xs elemento

--recuerdo que eq t le dice a la compu que puede comparar elementos

------------
todosIguales :: (Eq t) => [t] -> t -> Bool
todosIguales [] _ = True
todosIguales (x:xs) numero | x == numero = todosIguales xs numero
                           | otherwise = False

------------
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [x] = True
todosDistintos (x:xs) | pertenece xs x = False
                      | otherwise = todosDistintos xs

-----------
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [] = False
hayRepetidos (x:xs) = not (todosDistintos (x:xs))

-----------
quitar :: (Eq t) => [t] -> t -> [t]
quitar [] _ = []
quitar (x:xs) elemento | elemento == x = xs 
                       | otherwise = x: quitar xs elemento

--no olvidar meter otra vez el que no es igual a elemento

----------
quitarTodos :: (Eq t) => [t] -> t -> [t]
quitarTodos [] _ = []
quitarTodos (x:xs) elemento | elemento == x = quitarTodos xs elemento
                            | otherwise = x : quitarTodos xs elemento

----------
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (quitarTodos xs x)

--lo que tiene la guia es que te da las funciones que necesitas para el siguiente problema
--cosa que en el parcial es mas dificil porque tiene que pensar uno
--como en la vida real (?)