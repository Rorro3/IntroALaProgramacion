type Anio = Int
type EsBisiesto = Bool

--ponele que para que un anio sea bisiesto tiene que ser divisible por 100 y 400, no solo por 100
--y tambien tiene que ser multiplo de 4 lols
bisiesto :: Anio -> EsBisiesto
bisiesto anio | mod anio 100 == 0 && mod anio 400 /= 0 || mod anio 4 /= 0 = False
              | otherwise = True