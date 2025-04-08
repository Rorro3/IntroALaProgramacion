funcion :: Int -> Int
funcion n | n <= 7 = n*n
          | n > 7 = 2*n - 1

guncion :: Int -> Int
guncion n | mod n 2 == 0 = div n 2
          | otherwise = 3*n + 1

todosmenores :: (Int, Int, Int) -> Bool
todosmenores (x,y,z) | funcion x > guncion x && funcion y > guncion y && funcion z > guncion z = True
                     | otherwise = False