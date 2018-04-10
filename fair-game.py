#!/usr/bin/env python3

counter = [0] * (101)

n = int(input())
for x in (range(n)):
    counter[int(input())] += 1

for x in range(len(counter)):
    for y in range(len(counter)):
        if x != y and counter[x] != 0 and counter[x] == counter[y]:
            if(counter[x]+counter[y] == n):
                print("YES")
                print(str(x) + " " + str(y))
            else:
                print("NO")
            exit(0)

print("NO")
