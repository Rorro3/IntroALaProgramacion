--dados dos naturales ver si el primero es divisible por el segundo
--para que un numero sea divisible por otro ponele x por y
--x = y*q, con q entre 1 & x
--pero eso no me sirve >:(
--peeero sabemos que si x es multiplo de y, es y+y+y+y+y+...+y
--osea que si voy restando y's hasta que llegue a 0, es divisible

--le voy a pedir a mi cliente(?) que no ponga numeros negativos pq no quiero hacer la funcion valor absoluto

esDivisible :: Int -> Int -> Bool
esDivisible 0 _ = True
esDivisible x y | y > x || y == 0 = False 
                | x == 0 = True
                | x == 1 && y > 1 = False
                | otherwise = esDivisible (x-y) y
