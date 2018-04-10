#!/usr/bin/env python3

firstLine = [int(x) for x in input().split()]
n = firstLine[0]
t = firstLine[1]

secondLine = [int(x) for x in input().split()]

pos = 0
dest = t-1

while pos != dest and pos < n-1:
    pos = pos + secondLine[pos]


if(pos == dest):
    print("YES")
else:
    print("NO")
