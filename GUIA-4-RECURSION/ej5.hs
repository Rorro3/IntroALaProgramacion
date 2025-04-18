medioFact :: Int -> Int
medioFact n | n == 0 = 1
            | n == 1 = 1
            | otherwise = n * medioFact (n-2)

--es como el factorial pero aca hay dos casos base porque si voy restando de a dos llego al 1 o al 0