funcionefe :: Int -> Int
funcionefe 1 = 8
funcionefe 4 = 131
funcionefe 16 = 16


funcionge :: Int -> Int
funcionge 8 = 16
funcionge 16 = 4
funcionge 131 = 1

funcionhache :: Int -> Int
funcionhache x = funcionefe(funcionge(x))
