import System.IO
import Data.List (transpose)
import Data.Char

day3 = do
        content <- readFile "input.txt"
        let line = lines content
        return (day3' line)
            where day3' nums = bin2Int (map digitToInt (day3'' nums)) * bin2Int (map (digitToInt . bitFlip) (day3'' nums))
                  day3'' xss = map gamma (transpose xss)

day3_pt2 = do
          content <- readFile "input.txt"
          let line = lines content
          return (day3' line)
              where day3' line = bin2Int (map digitToInt (head (oxgen line 0))) * bin2Int (map digitToInt (head (co2 line 0)))
                    oxgen acc i | length acc == 1       = acc
                                | i > length (head acc) = error "FUCKING IDIOT"
                                | otherwise             = oxgen (filter (\x -> x!!i == mostCommon i acc) acc) (i+1)
                    co2 acc i   | length acc == 1       = acc
                                | i > length (head acc) = error "FUCKING IDIOT"
                                | otherwise             = co2 (filter (\x -> x!!i == leastCommon i acc) acc) (i+1)


bin2Int :: [Int] -> Int
bin2Int = foldl ((+) . (2*)) 0

readInt :: String -> Int
readInt = read

bitFlip :: Char -> Char
bitFlip '0' = '1'
bitFlip '1' = '0'
bitFlip _ = error "U SUCK"


count :: String -> Char -> Int
count [] _ = 0
count (x:xs) y | x == y    = 1 + count xs y
             | otherwise   = 0 + count xs y

gamma :: String -> Char
gamma s | count s '1' >= count s '0' = '1'
        | otherwise                  = '0'


mostCommon :: Int -> [String] -> Char
mostCommon i xss = gamma [xs!!i | xs <- xss]

leastCommon :: Int -> [String] -> Char
leastCommon i xs = bitFlip (mostCommon i xs)

oxgen :: [String] -> Int -> [String]
oxgen acc i | length acc == 1       = acc
            | i > length (head acc) = error "FUCKING IDIOT"
            | otherwise             = oxgen (filter (\x -> x!!i == mostCommon i acc) acc) (i+1)


co2 acc i | length acc == 1       = acc
          | i > length (head acc) = error "FUCKING IDIOT"
          | otherwise             = co2 (filter (\x -> x!!i == leastCommon i acc) acc) (i+1)
