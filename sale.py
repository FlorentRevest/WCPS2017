#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
m = firstLine[1]
secondLine = [int(x) for x in input().split()]
secondLine.sort()

ret = 0
nbExplored = 0
for x in secondLine:
    if nbExplored >= m:
        break
    if x < 0:
        ret -= x
    nbExplored += 1

print(ret)
