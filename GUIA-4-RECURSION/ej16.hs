--a) menor divisor (que no sea 1, asi que si es primo, es el mismo)
--osea voy a buscar desde el 2 (el numero natural que le sigue al 1) y ver si lo divide
--si 2 divide, listo
--si 2 no divide, pasa al 3 y asi
--termina cuando llego al mismo numero que le paso
menorDivisorDesde :: Int -> Int -> Int
menorDivisorDesde numero divisor | numero == divisor = numero
                                 | numero /= divisor && mod numero divisor == 0 = divisor
                                 | otherwise = menorDivisorDesde numero (divisor + 1)

--y ahora es lo mismo que la anterior pero desde el 2, porque sino siempre me daria 1
menorDivisor :: Int -> Int
menorDivisor n = menorDivisorDesde n 2