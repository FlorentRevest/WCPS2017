#!/usr/bin/env python3

word = input()
upper = word.upper()
if(word[1::] == upper[1::]):
    print(word.swapcase())
else:
    print(word)
