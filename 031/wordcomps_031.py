#!/usr/bin/env python3

import sys

def wordcomps(s):
    if len(s) == 17:
        seventeen_ls.append(s)
    elif len(s) >= 18:
        eighteen_plus_ls.append(s)
    if s.lower().count("a") == 4:
        four_a.append(s)
    if s.lower().count("q") >= 2:
        multi_q.append(s)
    if "cie" in s.lower():
        cie_ls.append(s)
    if sorted(s.lower()) == sorted("angle") and s.lower() != "angle":
        angle.append(s)


seventeen_ls = list()
eighteen_plus_ls = list()
four_a = list()
multi_q = list()
cie_ls = list()
angle = list()

for line in sys.stdin:
    line = line.strip()
    wordcomps(line)

print("Words containing 17 letters:", seventeen_ls)
print("Words containing 18+ letters:", eighteen_plus_ls)
print("Words with 4 a's:", four_a)
print("Words with 2+ q's:", multi_q)
print("Words containing cie:", cie_ls)
print("Anagrams of angle:", angle)
