#!/usr/bin/env python3

import sys

def nice(s):
    tokens = ['n', 'i', 'c', 'e']
    for t in tokens:
        if s.count(t) != 1:
            return
    print(s)


for line in sys.stdin:
    line = line.strip()
    nice(line)
