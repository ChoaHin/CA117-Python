#!/usr/bin/env python3

import sys

def vowels(s):
    for char in "aeiou":
        if char not in s.lower():
            return False
    return True


short_vowel = str()
length = 100
iary_word = 0
e_count = 0
most_e = list()

for line in sys.stdin:
    line = line.strip()
    if vowels(line) and len(line) < length:
        length = len(line)
        short_vowel = line
    if line[-4:] == "iary":
        iary_word += 1
    if line.count("e") > e_count:
        e_count = line.count("e")
        most_e = list()
    if line.count("e") == e_count:
        most_e.append(line)

print("Shortest word containing all vowels:", short_vowel)
print("Words ending in iary:", iary_word)
print("Words with most e's:", most_e)
