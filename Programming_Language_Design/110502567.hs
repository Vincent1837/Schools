-- Practice A
isPalindrome :: Eq a => [a] -> Bool
-- please complete here

reverseList :: [a] -> [a]
reverseList [] = []
reverseList (x:xs) = reverseList xs ++ [x]

isPalindrome a = reverseList a == a

testcasesA :: [[Int]]
testcasesA = [[1,2,2,1], [1..30], [], [5..15], [999], [7,3,7]]

resultA :: [Bool]
resultA = map isPalindrome testcasesA 


-- Practice B
coolDiv :: [Double] -> Either String Double
-- please complete here
coolDiv xs
    | length xs < 2 = Left "Too short"
    | head xs == 0  = Left "Division by zero"
    | otherwise = Right (last (take 2 xs) / head xs )


testcasesB :: [[Double]]
testcasesB = [[], [5..15], [999], [33,9999], [0..9]]

resultB :: [Either String Double]
resultB = map coolDiv testcasesB


main :: IO ()
main = do
  print resultA -- [True,False,True,False,True,True]
  print resultB -- [Left "Too short",Right 1.2,Left "Too short",Right 303.0,Left "Division by zero"]