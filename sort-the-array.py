#!/usr/bin/env python3

n = int(input())

secondLine = [int(x) for x in input().split()]

increasing = None
nbChange = 0
prevX = secondLine[0]
for i in range(1, len(secondLine)):
    x = secondLine[i]
    if(x > prevX):
        if(increasing == False): 
            nbChange += 1
        increasing = True
    else:
        if(increasing == True): 
            nbChange += 1
        increasing = False

print(nbChange)
