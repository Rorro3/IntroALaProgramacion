--aproximar e
--sumatoria desde i = 0 hasta n de 1/i!
aproximAe :: Int -> Float
aproximAe 0 = 1
aproximAe n = 1/fromIntegral (factorial n) + aproximAe (n - 1)

factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial (n-1)

--osea no entiendo que estoy aproximando a e
--hice la sumatoria blindly

e :: Float
e = aproximAe 10