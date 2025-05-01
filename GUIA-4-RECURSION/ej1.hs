--quiere que segun el numero que me den, les devuelva el numero en la serie de fibonacci que tiene esa posicion

fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = fibonacci (n-1) + fibonacci (n-2)
