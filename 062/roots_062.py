#!/usr/bin/env python3

import sys

def roots(a, b, c):
    a, b, c = int(a), int(b), int(c)
    if (b * b) - (4 * a * c) < 0:
        return None
    root1 = (-b + ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    root2 = (-b - ((b ** 2) - (4 * a * c)) ** 0.5) / (2 * a)
    return (f'r1 = {root1}, r2 = {root2}')


for line in sys.stdin:
    (a, b, c) = line.strip().split()
    print(roots(a, b, c))
