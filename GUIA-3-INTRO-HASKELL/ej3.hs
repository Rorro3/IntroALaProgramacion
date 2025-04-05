estanrel :: Int -> Int -> Bool
estanrel x y | mod (-x) y == 0 = True
             | otherwise = False

--quiero un k que cumpla esta igualdad
--como quiero cualquier k y no uno que de yo como entrada, lo escribo en terminos de los que si doy en la entrada
-- xx + xyk = 0
-- xyk = -xx
--k = -xx/xy
--k = -x/y
--como es lo mismo en los negativos y en los positivos lo del resto, lo podia dejar en positivo, pero queria mostrar el pensamiento(?)
