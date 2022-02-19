#!/usr/bin/env python3

import sys

def tagger(item):
   return item[1]

def vowel(s):
    vowels = {n: 0 for n in 'aeiou'}
    for char in s:
        if char in vowels:
            vowels[char] += 1
    return vowels


line = sys.stdin.read().lower()
vowels = vowel(line)
max_v_width = (len(str(max(vowels.values()))))
for k, v in sorted(vowels.items(), key=tagger, reverse=True):
    print(f'{k} : {v:>{max_v_width}}')
