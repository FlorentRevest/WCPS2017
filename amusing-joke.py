#!/usr/bin/env python3

guest = [x for x in input()]
host = [x for x in input()]
letters = [x for x in input()]

sortedLetters = sorted(letters)
sortedExpected = sorted(guest + host)
if sortedLetters == sortedExpected:
    print("YES")
else:
    print("NO")
