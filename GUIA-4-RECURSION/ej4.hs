--quiere que al pasarme un numero n, sume los primeros n impares
--ej: (input) 3 = 1 + 3 + 5 = 9 (output)

--estoy pensando primero en hacer una funcion que me diga la posicion de los impares

posicionImpares :: Int -> Int 
posicionImpares 1 = 1
posicionImpares n = posicionImpares (n-1) + 2

--osea 1 caso base pq primer impar 
--n-1 seria el anterior mas dos, al final lo que estas haciendo es sumarle de a dos al uno hasta llegar al numero que queres

sumaImpares :: Int -> Int 
sumaImpares 1 = 1
sumaImpares n = posicionImpares n + sumaImpares (n-1)

--aca lo que hago es:
--caso base = 1 porque 1 es el primer impar y es el solito sin sumarlo a nada
--con un n cualquiera suma la posicion del n en los impares y le suma la posicion del anterior hasta llegar a n =1
                  


