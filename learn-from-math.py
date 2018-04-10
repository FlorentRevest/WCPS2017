#!/usr/bin/env python3

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n = int((input()))

for x in range(2, n):
    if(isPrime(x)):
        continue

    rest = n - x
    if(isPrime(rest)):
        continue

    print(str(x) + " " + str(rest))
    exit(0)
