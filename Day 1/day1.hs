day1 :: [Int] -> Int
day1 xs = f' xs 0
    where f' [] acc = acc
          f' [x] acc = acc
          f' (x:y:xs) acc | x < y     = f' (y:xs) (acc+1)
                          | otherwise = f' (y:xs) (acc+0)

day1' :: [Int] -> Int 
day1' xs = day1 (slider xs)  
    where slider [] = []
          slider [x] = []
          slider [x,y] = []
          slider (x:y:z:xs) = (x+y+z) : slider (y:z:xs)
                             
newLinesToList :: String -> [Int]
newLinesToList s = reverse (f' s "" [])
    where f' :: String -> String -> [Int] -> [Int]
          f' []     stringAcc listAcc = stringToInt stringAcc : listAcc
          f' (x:xs) stringAcc listAcc | x == ' ' = f' xs "" (stringToInt stringAcc : listAcc)
                                      | otherwise = f' xs (stringAcc ++ [x]) listAcc

stringToInt :: String -> Int
stringToInt = read