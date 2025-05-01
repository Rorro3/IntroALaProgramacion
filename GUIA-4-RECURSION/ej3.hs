--quiere que le diga si el primer numero es divisible por el segundo sin usar div ni mod
--para que un numero sea divisible por otro tiene que ser ese otro numero n veces, right?
--entonces puedo hacer una funcion que me vaya incrementando el segundo numero sumandolo hasta llegar a cierto numero
--la voy a llamar "multiplos"
multiplos :: Int -> Int -> Int -> Bool
multiplos _ 1 1 = True
multiplos n m l | n == m = True
                | m > n = False
                | m * l > n = False
                | n == m*l = True
                | otherwise = multiplos n m (l+1)

--aca le doy 3 inputs, uno va a ser mi numero que quiero saber si es divisible (n)
--el otro va a ser el numero que quiero saber si divide a n (m)
--el otro es un numero que se me cante al que lo voy a probar multiplicar por m (l)
--si l*m no divide a n, prueba con l+1 y asi hasta que m se vuelve mas grande que n

esDivisible :: Int -> Int -> Bool
esDivisible n m = multiplos n m 1

--esta es la funcion que me piden con la cantidad de parametros que me piden
--aca "l" en "multiplos" es siempre 1 ya que es el numero mas chico por el que puedo multiplicar a m