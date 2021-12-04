#!/usr/bin/python
import sys

def part1(inList):
    x = 0 #horizontal
    y = 0 #depth
    for line in inList:
        direction,delta  = line.split()
        if (direction == 'up'):
            y -= int(delta)
        elif (direction == 'forward'):
            x += int(delta)
        elif (direction == 'down'):
            y += int(delta)
        else:
            print "ERROR, wrong input"
    print "X: " + str(x) + " Y: " + str(y) + " Prod: " + str(x*y)

def part2(inList):
    x = 0 #horizontal
    y = 0 #depth
    aim = 0
    for line in inList:
        direction,delta = line.split()
        if (direction == 'up'):
            aim -= int(delta)
        elif (direction == 'down'):
            aim += int(delta)
        elif (direction == 'forward'):
            x += int(delta)
            y += aim * int(delta)
        else:
            print "ERROR, wrong input"
    print "X: " + str(x) + " Y: " + str(y) + " Prod: " + str(x*y)

def main():
    fileName = "input.txt"
    if len(sys.argv) > 1:
        fileName = sys.argv[1]
    f = open(fileName, "r")
    inList = f.readlines()
    part1(inList)
    part2(inList)
if __name__ == '__main__':
    sys.exit(main())
