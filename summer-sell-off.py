#!/usr/bin/env python3

n = int(input())
secondLine = [int(x) for x in input().split()]
secondLine.sort()

ret = 0
prevX = 0
for x in secondLine:
    if(x >= prevX):
        diff = (prevX - x + 1)
        ret += diff
        x += diff
    prevX = x
print(ret)
