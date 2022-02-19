#!/usr/bin/env python3

import sys
[num, alp] = sys.stdin.readlines()

num = num.strip().split()
num.sort(key=int)

alp = list(alp.strip())
alp_sort = sorted(alp)

d = dict()
i = 0
while i < len(num):
    d[alp_sort[i]] = num[i]
    i += 1

result = list()
for char in alp:
    result.append(d[char])
print(" ".join(result))
