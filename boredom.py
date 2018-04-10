#!/usr/bin/env python3

def removeElem(l, choice):
    l_cpy = []
    n = 0
    for val in l:
        if (val != choice-1 and val != choice+1 and val != choice):
            l_cpy.append(val)

    return l_cpy

def maxPoints(l):
    if(len(l) != 0):
        s = set(l)
        maxImpact = -100000000000000000
        maxPosImpact = 0
        goodChoice = 0
        for choice in s:
            impact = 0
            posImpact = 0
            for val in l:
                if (val == choice-1):
                    impact = impact - (choice-1)
                elif (val == choice+1):
                    impact = impact - (choice+1)
                elif (val == choice):
                    impact = impact + choice
                    posImpact = posImpact + choice
            
            if(impact > maxImpact):
                maxImpact = impact
                maxPosImpact = posImpact
                goodChoice = choice


        return maxPosImpact + maxPoints(removeElem(l, goodChoice))
    else:
        return 0

n = int(input())
secondLine = [int(x) for x in input().split()]
print(maxPoints(secondLine))
