#!/usr/bin/env python3

import sys

def anagram(a, b):
    if sorted(a) != sorted(b):
        return False
    else:
        return True


for line in sys.stdin:
    [left, right] = line.strip().split()
    print(anagram(left, right))
