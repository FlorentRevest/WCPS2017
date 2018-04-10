#!/usr/bin/env python3

def adjustedVal(m, n, sub, ai, endVal):
    if(m+firstBookIndex >= n):
        return abs(ai[m+firstBookIndex-n]-sub+endVal)
    else:
        return abs(ai[m+firstBookIndex]-sub)

def howManyBooksUnder(x, ai, n, firstBookIndex, sub):
    l = 0
    r = n-1-firstBookIndex
    endVal = ai[n-1]

    while r > l + 1:
        m = round((l+r)/2)
        if adjustedVal(m, n, sub, ai, endVal) <= x:
            l = m
        else:
            r = m
    if adjustedVal(l, n, sub, ai, endVal) > x:
        return 0
    if adjustedVal(r, n, sub, ai, endVal) <= x:
        return r+1
    else:
        return l+1

firstLine = [int(x) for x in input().split()] # prices
n = firstLine[0]
t = firstLine[1]

ai = [int(x) for x in input().split()] # time per book
for i in range(1, n):
    ai[i] += ai[i-1]

maxBooks = 0
for firstBookIndex in range(n):
    sub = 0
    if(firstBookIndex > 0):
        sub = ai[firstBookIndex-1]
    newMax = howManyBooksUnder(t, ai, n, firstBookIndex, sub)
    if newMax > maxBooks:
        maxBooks = newMax

print(maxBooks)
