--sumatoria de i = 1 hasta n de otra sumatoria de j = 1 hasta m de i a la j
sumatoriaDentro :: Int -> Int -> Int 
sumatoriaDentro numero 1 = numero
sumatoriaDentro numero m = numero ^ m + sumatoriaDentro numero (m-1)

sumatoria :: Int -> Int -> Int
sumatoria 1 m = sumatoriaDentro 1 m
sumatoria n m = sumatoriaDentro n m + sumatoria (n-1) m

--osea la sumatoria de adentro primero, que va variando el j seria
--y luego la meto en la otra donde va variando el i