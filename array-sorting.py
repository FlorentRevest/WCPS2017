#!/usr/bin/env python3

def my_merge(a, b):
    c = [None] * (len(a)+len(b))
    i = 0
    j = 0
    k = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c[k] = a[i]
            i=i+1
        else:
            c[k] = b[j]
            j=j+1
        k=k+1
    while i < len(a):
        c[k] = a[i]
        i = i+1
        k = k+1
    while j < len(b):
        c[k] = b[j]
        j = j+1
        k = k+1
    return c

def my_merge_sort(a):
    if(len(a)) > 1:
        m = round(len(a)/2)
        a[0:m] = my_merge_sort(a[0:m])
        a[m:len(a)] = my_merge_sort(a[m:len(a)])
        a = my_merge(a[0:m], a[m:len(a)])
    return a

firstLine = [int(x) for x in input().split()]
sortedLine = my_merge_sort(firstLine[1:])
for x in sortedLine:
    print(str(x) + " ", end="")
print()
