#!/usr/bin/env python3

import sys

def substring(left, right):
    return left.lower() in right.lower()


for line in sys.stdin:
    tokens = line.strip().split()
    [left, right] = tokens
    print(substring(left, right))
