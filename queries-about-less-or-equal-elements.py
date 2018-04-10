#!/usr/bin/env python3

def howManyElemsUnder(x, ai, n):
    l = 0
    r = n-1
    while r > l + 1:
        m = round((l+r)/2)
        if ai[m] <= x:
            l = m
        else:
            r = m
    if ai[l] > x:
        return 0
    if ai[r] <= x:
        return r+1
    else:
        return l+1

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
m = firstLine[1]

secondLine = [int(x) for x in input().split()]
secondLine.sort()
thirdLine = [int(x) for x in input().split()]

for x in thirdLine:
    print(howManyElemsUnder(x, secondLine, n), end=' ')
print()
