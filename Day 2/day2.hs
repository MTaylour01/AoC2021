import System.IO

day2 = do
        content <- readFile "input.txt"
        let line = lines content
        return (day2' line 0 0)
            where day2' [] forwardAcc depthAcc = forwardAcc * depthAcc
                  day2' (('f':'o':'r':'w':'a':'r':'d':' ':x):xs) forwardAcc depthAcc = day2' xs (forwardAcc + readInt x) depthAcc
                  day2' (('d':'o':'w':'n':' ':y):xs)    forwardAcc depthAcc = day2' xs forwardAcc (depthAcc + readInt y)
                  day2' (('u':'p':' ':y):xs)      forwardAcc depthAcc = day2' xs forwardAcc (depthAcc - readInt y)

readInt :: String -> Int 
readInt = read

day2'' = do
          content <- readFile "input.txt"
          let line = lines content
          return (day2' line 0 0 0)
              where day2' [] forwardAcc depthAcc aim = forwardAcc * depthAcc
                    day2' (('f':'o':'r':'w':'a':'r':'d':' ':x):xs) forwardAcc depthAcc aim = day2' xs (forwardAcc + readInt x) (depthAcc + (readInt x * aim)) aim
                    day2' (('d':'o':'w':'n':' ':y):xs) forwardAcc depthAcc aim = day2' xs forwardAcc depthAcc (aim + readInt y)
                    day2' (('u':'p':' ':y):xs) forwardAcc depthAcc aim = day2' xs forwardAcc depthAcc (aim - readInt y)
