#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
l = firstLine[1]
secondLine = [int(x) for x in input().split()]
secondLine.sort()

i = 1
maxDist = secondLine[0]
while i < n:
    dist = secondLine[i]-secondLine[i-1]
    if dist/2 > maxDist:
        maxDist = dist/2
    i = i+1

lastStep = l - secondLine[n-1]
if (lastStep > maxDist):
    maxDist = lastStep

print(maxDist)
