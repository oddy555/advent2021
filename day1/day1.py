#!/usr/bin/python
import sys
fileName = "input.txt"
if len(sys.argv) > 1:
    fileName = sys.argv[1]

f = open(fileName,"r")

prevVal = -1
numInc = 0 
i = 0
sum
for line in f.readlines():
    if prevVal == -1:
        prevVal = int(line)
        continue
    currVal = int(line)
    print str(currVal) + ">" + str(prevVal)
    if currVal > prevVal:
        numInc += 1
    prevVal = currVal
print numInc
