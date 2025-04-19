--sumatoria desde i=1 hasta n de la sumatoria desde j=1 hasta m de i^j
sumatoriaAdentro :: Int -> Int -> Int
sumatoriaAdentro n 1 = n
sumatoriaAdentro n m = sumatoriaAdentro n (m-1) + n^m

sumatoriaDoble :: Int -> Int -> Int
sumatoriaDoble 0 m = m
sumatoriaDoble n m = sumatoriaDoble (n-1) m + sumatoriaAdentro n m

--osea las sumatorias aca en vez de incrementar del 1 hasta el n
--van del n hasta el 1, corte n-1 + n-2 ...