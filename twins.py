#!/usr/bin/env python3

n = int(input())

secondLine = [int(x) for x in input().split()]
secondLine.sort(reverse=True)
total = sum(secondLine)

currSum = 0
ret = 0

for x in secondLine:
    currSum = currSum + x
    ret = ret + 1
    if(currSum > (total-currSum)):
        break

print(ret)
