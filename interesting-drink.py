#!/usr/bin/env python3

def howManyShopsUnder(x, ai, n):
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

n = int(input())
xi = [int(x) for x in input().split()] # prices
xi.sort()

q = int(input())
mi = [None] * q # available money
for i in range(q):
    mi[i] = int(input())

for m in mi:
    print(howManyShopsUnder(m, xi, n))
