module Filetolist (
    getList
)
where

import System.IO

getList (fName,tmpList) = do
    contents <- readFile fName
    let a = lines contents
    a
