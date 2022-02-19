#!/usr/bin/env python3

import sys
#Multiples of 3 replaced: [1, 2, 'X', 4, 5, 'X', 7, 8]
def repcomps(n):
    return[num if num % 3 else "X" for num in range(1, n + 1)]


for line in sys.stdin:
    n = int(line.strip())
    print("Multiples of 3 replaced:", repcomps(n))
