enteroPositivo :: Float -> Float
enteroPositivo n | n >= 0 = n
                 | otherwise = - n
--quiere que sume las diferencias de cada coord de las tuplas
distanciaManhattan :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattan (x1, x2, x3) (y1, y2, y3) = enteroPositivo (x1 - y1) + enteroPositivo (x2 - y2) + enteroPositivo (x3 - y3)

