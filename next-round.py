#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
k = firstLine[1]

secondLine = [int(x) for x in input().split()]
maxVal = secondLine[k-1]

ret = 0

for x in secondLine:
    if x >= maxVal and x > 0:
        ret = ret + 1
    else:
        break

print(ret)
