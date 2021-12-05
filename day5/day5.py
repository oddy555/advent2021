#!/usr/bin/python
import sys

coveredDict = {}

def addToDict(pos):
    if coveredDict.has_key(pos):
        coveredDict[pos] += 1
    else:
        coveredDict[pos] = 1
    return coveredDict

def part1(coordList):
    maxPos = 0

    loopStart = 0
    loopEnd = 0
    for ((x1,y1),(x2,y2)) in coordList:
        if (x1 == x2): #Vertical line
            if ((y1-y2) > 0):
                loopStart = y2
                loopEnd = y1
            elif ((y2-y1) > 0):
                loopStart = y1
                loopEnd = y2
            while loopStart <= loopEnd:
                tmpKey = (x1,loopStart)
                if coveredDict.has_key(tmpKey):
                    coveredDict[tmpKey] += 1
                else:
                    coveredDict[tmpKey] = 1
                loopStart += 1
        elif (y1 == y2): #Vertical line
            if ((x1-x2) > 0):
                loopStart = x2
                loopEnd = x1
            elif ((x2-x1) > 0):
                loopStart = x1
                loopEnd = x2
            while loopStart <= loopEnd:
                tmpKey = (loopStart,y1)
                if coveredDict.has_key(tmpKey):
                    coveredDict[tmpKey] += 1
                else:
                    coveredDict[tmpKey] = 1
                loopStart += 1
        else:
            yStart = 0
            xStart = 0
            yEnd = 0
            xEnd = 0
        if (x2-x1 > 0):
            xStart = x1
            xEnd = x2
            if (y2-y1 > 0):
                yStart = y1
                yEnd = y2
                while xStart <= xEnd:
                    addToDict((xStart,yStart))
                    xStart += 1
                    yStart += 1
            elif (y1-y2 > 0):
                yStart = y1
                yEnd = y2
                while xStart <= xEnd:
                    addToDict((xStart,yStart))
                    xStart += 1
                    yStart -= 1
        elif (x1-x2 > 0):
            xStart = x1
            xEnd = x2
            if (y2-y1 > 0):
                yStart = y1
                yEnd = y2
                while xStart >= xEnd:
                    addToDict((xStart,yStart))
                    xStart -= 1
                    yStart += 1
            elif (y1-y2 > 0):
                yStart = y1
                yEnd = y2
                while xStart >= xEnd:
                    addToDict((xStart,yStart))
                    xStart -= 1
                    yStart -= 1



    tmpSum = 0
    for key in coveredDict:
        if coveredDict[key] >= 2:
            tmpSum += 1
    print str(tmpSum)
                
def main():
    fileName = "input.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    f = open(fileName, "r")
    
    coordList = []
    for line in f.readlines():
        tmp = line.split()
        tmpStart = tmp[0].split(",")
        startCoord = (int(tmpStart[0]),int(tmpStart[1]))
        tmpEnd = tmp[2].split(",")
        endCoord = (int(tmpEnd[0]),int(tmpEnd[1]))
        coordList.append((startCoord,endCoord))
        
    part1(coordList)
if __name__ == '__main__':
    sys.exit(main())
