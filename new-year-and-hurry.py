#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
k = firstLine[1]

totalMinutes = 60*4 - k

currSum = 0
for i in range(1, n+1):
    currSum += i*5
    if(currSum > totalMinutes):
        print(i-1)
        exit(0)

print(i)
