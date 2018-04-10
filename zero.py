#!/usr/bin/env python3

input = open('zero.in')
output = open('zero.out', 'w+')

n = int(input.readline())
values = [int(x) for x in input.readline().split()]
values.reverse()
for value in values:
    output.write(str(value) + " ")
output.write("\n")
