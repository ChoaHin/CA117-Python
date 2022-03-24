#!/usr/bin/env python3

import sys

def double_vowel(s):
    vowel = ['a', 'e', 'i', 'o', 'u']
    count = 0
    i = 0
    while i < len(s):
        if s[i] in vowel and s[i] == s[i + 1]:
            count += 1
        i += 1
    return count

def tagger(x):
    return x[1]


d = {}
for line in sys.stdin:
    d[line.strip()] = double_vowel(line)
print(max(d.items(), key=tagger)[0])
