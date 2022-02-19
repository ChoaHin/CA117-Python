#!/usr/bin/evn pythno3

import sys

def contain(c, s):
    for char in c:
        if char not in s:
            return False
        s = s.replace(char, "", 1)
    return True


for line in sys.stdin:
    [char, line] = line.strip().lower().split()
    print(contain(char, line))
