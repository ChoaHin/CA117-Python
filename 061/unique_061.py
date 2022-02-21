#!/usr/bin/env python3

import sys

def unique(s):
    ls = []
    for k in s:
        if s.count(k) == 1:
             ls.append(k)
    return ls


for line in sys.stdin:
    line = line.strip()
    ls = unique(line)
    if ls:
        print(max(ls))
    else:
        print('none')
