#!/usr/bin/python
import sys
import operator

def part1(measArr,nCol):
    nZeros = 0
    nOnes = 0
    i = 0
    j = 0
    gamma = 0
    epsilon = 0
    nShifts = nCol-1
    while i < nCol:
        while j < len(measArr):
            if int(measArr[j][i]) == 1:
                nOnes += 1
            else:
                nZeros += 1
            j += 1
        if nOnes > nZeros:
            gamma |= (0x1 << nShifts)
        else:
            epsilon |= (0x1 << nShifts)
        nOnes = 0
        nZeros = 0
        nShifts -= 1
        i += 1
        j = 0
        
    print "gamma: " + str(gamma)
    print "epsilon: " + str(epsilon)
    print "answer: " + str(gamma * epsilon)

def findOxygen(tmpList,pos,op):
    if len(tmpList) == 1:
        return int(tmpList[0],2)
    #elif pos > 4:
    #    return -1
    onesList = []
    zerosList = []
    ones = 0
    zeros = 0
    i = 0
    while i < len(tmpList):
        if (int(tmpList[i][pos]) == 1):
            onesList.append(tmpList[i])
            ones += 1
        else:
            zerosList.append(tmpList[i])
            zeros += 1
        i += 1
    if op(ones, zeros):
        return findOxygen(onesList,pos+1,op)
    else:
        return findOxygen(zerosList,pos+1,op)
                
def part2(tmpList, nCol):
    oxy = findOxygen(tmpList,nCol,operator.ge)
    scrub = findOxygen(tmpList,nCol,operator.lt)
    print str(int(oxy))
    print str(int(scrub))
    print str(int(oxy * scrub))
    #scrub = findScrubber()

def main():
    fileName = "input.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    f = open(fileName, "r")
    nCol = 0
    tmpArr = []
    for line in f.readlines():
        if nCol == 0:
            nCol = len(line) -1
            print nCol
        tmpArr.append(line.replace('\n',''))
    part1(tmpArr,nCol)
    print str(nCol)
    part2(tmpArr,0)
if __name__ == '__main__':
    sys.exit(main())
