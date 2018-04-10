#!/usr/bin/env python3

input = open('yield.in')
output = open('yield.out', 'w+')

firstLine = [float(x) for x in input.readline().split()]
x = firstLine[0]
y = firstLine[1]

output.write(str(round(x+y, 4)) + "\n")
