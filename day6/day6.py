#!/usr/bin/python
import sys

def main():
    fileName = "input.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    f = open(fileName, "r")
    fishList = []
    oldFishList = []
    i = 0
    for char in f.readline():
        if (char != '\n') and (char != ','):
            fishList.append(int(char))
            oldFishList.append(int(char))
    #print fishList
    i = 0
    while i < 80:
        babyFishList = []
        j = 0
        while j <  len(fishList):
            if fishList[j] == 0:
                babyFishList.append(8)
                fishList[j] = 6
            else:
                fishList[j] -= 1
            j += 1
        i += 1    
        fishList = fishList + babyFishList

    fishList = [0,0,0,0,0,0,0,0,0]
    for fish in oldFishList:
        fishList[fish] += 1
    fishT = 0
    while fishT < 256:
        nNewFish = fishList[0]
        i = 0
        while i < len(fishList):
            if (i+1 < len(fishList)):
                fishList[i] = fishList[i+1]
            i += 1
        fishList[8] = nNewFish
        fishList[6] += nNewFish
        fishT += 1
    print str(sum(fishList))
        
if __name__ == '__main__':
    sys.exit(main())
