import Data.Bifoldable (bifoldl1)
import Data.Bits (Bits(xor))
--tuplas :/
--a)
productoEntero :: (Float, Float) -> (Float, Float) -> Float
productoEntero (a1, b1) (a2, b2) = a1 * a2 + b1 * b2

otraforma :: (Float, Float) -> (Float, Float) -> Float
otraforma k l = fst k * fst l + snd k * snd l

--b) decide si cada coordenada de la primera tupla es menor a la coordenada correspondiente de la segunda tupla.

esparmenor :: (Float, Float) -> (Float, Float) -> Bool
esparmenor x y | fst x < fst y && snd x < snd y = True
               | otherwise = False

--c) distancia euclideana corte raiz de la diferencia de la diferenccia(?)
distancia :: (Float, Float) -> (Float, Float) -> Float
distancia (x1,y1) (x2,y2) = sqrt((x1-x2) ^ 2 + (y1-y2) ^2)

--d) suma terna
sumaterna :: (Int, Int, Int) -> Int
sumaterna (x,y,z) = x + y + z

--e) sumar solo los multiplos de un numero dado en una terna
sumarmultiplos :: (Int, Int, Int) -> Int -> Int
sumarmultiplos (a,b,c) numero | mod a numero == 0 && mod b numero == 0 && mod c numero == 0 = a + b + c
                              | mod a numero == 0 && mod b numero == 0 = a + b
                              | mod a numero == 0 && mod c numero == 0 = a + c
                              | mod b numero == 0 && mod c numero == 0 = b + c
                              | mod a numero == 0 = a
                              | mod b numero == 0 = b
                              | mod c numero == 0 = c
                              | otherwise = 0
--siento que hay una forma mas linda de hacer esto, 
--recuerdo igual que no tengo que poner el caso de /= porque las guardas se fijan de arriba a abajo
--con recursion seria mas lindo que en lugar de una tupla sea una lista

--f) dada una terna de enteros, devuelve la posicion del primer numero par si es que hay alguno,
-- o devuelve 4 si son todos impares.
posicionprimerpar :: (Int, Int, Int) -> Int
posicionprimerpar (x,y,z) | mod x 2 == 0 = x
                          | mod y 2 == 0 = y
                          | mod z 2 == 0 = z
                          | otherwise = 4

--g) crear par de cualquier tipo

crearpar :: a -> b -> (a,b)
crearpar a b = (a,b)

--h) invertir cualquier tipo de tuplas
invertir :: (a,b) -> (b,a)
invertir (a,b) = (b,a)