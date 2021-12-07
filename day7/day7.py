#!/usr/bin/python
import sys
import math 

def main():
    fileName = "input.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    f = open(fileName, "r")
    l = []
    splitS = f.readline().split(",")
    for c in splitS:
        if (c != '\n'):
            l.append(int(c))
    medianIdx = 0
    sortedL = sorted(l)
    val = 0
    if len(sortedL) % 2 == 0:
        tmpIdx = len(sortedL)//2
        val = (sortedL[tmpIdx] + sortedL[tmpIdx-1])//2
    else:
        tmpIdx = len(sortedL)//2
        val = sortedL[tmpIdx]
    print val 
    fuelSum = 0
    for i in sortedL:
        fuelSum += abs(val-i)
    val = math.floor(float(sum(sortedL))/float(len(sortedL)))
    print fuelSum
    print val
    fuelSum = 0
    for i in sortedL:
        n = int(abs(val-i))
        fuelSum += (n*(n+1))/2
    print fuelSum
if __name__ == '__main__':
    sys.exit(main())
