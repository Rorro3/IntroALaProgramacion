--quiere el medio factorial, osea en vez de n-1, n-2
--quiero hacer la funcion factorial, que no la hice todavia
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1) 

medioFactorial :: Int -> Int
medioFactorial 0 = 1
medioFactorial 1 = 1
medioFactorial n = n * medioFactorial (n-2)
