#!/usr/bin/env python3

def findPile(x, ai, n):
    l = 0
    r = n-1
    while r > l + 1:
        m = round((l+r)/2)
        if ai[m] <= x:
            l = m
        else:
            r = m
    if ai[l] >= x:
        return l
    else:
        return r

n = int(input())
ai = [int(x) for x in input().split()]

for i in range(1, n):
    ai[i] = ai[i] + ai[i-1]

m = int(input())
qi = [int(x) for x in input().split()]

for q in qi:
    print(findPile(q, ai, n)+1)
