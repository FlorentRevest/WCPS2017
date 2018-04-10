#!/usr/bin/env python3

n = int(input())
secondLine = [int(x) for x in input().split()]

minPerf = secondLine[0]
maxPerf = secondLine[0]
ret = 0

for x in secondLine[1::]:
    if(x < minPerf):
        minPerf = x
        ret = ret+1
    elif(x > maxPerf):
        maxPerf = x
        ret = ret+1

print(ret)
