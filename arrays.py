#!/usr/bin/env python3

firstLine = input()
secondLine = [int(x) for x in input().split()]
k = secondLine[0]
m = secondLine[1]

thirdLine = [int(x) for x in input().split()]
fourthLine = [int(x) for x in input().split()]

if max(thirdLine[:k]) < min(fourthLine[len(fourthLine)-m:]):
    print("YES")
else:
    print("NO")
