#!/usr/bin/python
import sys
fileName = "input.txt"
if len(sys.argv) > 1:
    fileName = sys.argv[1]

f = open(fileName,"r")

sumArr = []
tmpArr = []
for line in f.readlines():
    tmpArr.append(int(line))
i = 0
while i < len(tmpArr):
    if (i+2) == int(len(tmpArr)-1):
        sumArr.append(tmpArr[i]+tmpArr[i+1]+ tmpArr[i+2])
        break;
    sumArr.append(tmpArr[i]+tmpArr[i+1]+ tmpArr[i+2])
    i += 1

prevVal = -1
numInc = 0 
for line in sumArr:
    if prevVal == -1:
        prevVal = int(line)
        continue
    currVal = int(line)
    if currVal > prevVal:
        numInc += 1
    prevVal = currVal
print numInc
