#!/usr/bin/env python3

import math

n = int(input())

secondLine = [int(x) for x in input().split()]
secondLine.sort()

ret = 0
xind = 0
for x in secondLine:
    i = 1
    xind += 1
    for y in secondLine[xind:]:
        ret += i * (y - x)
        i *= 2

print(ret % (100000007))
