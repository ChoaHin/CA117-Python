#!/usr/bin/env python3

import sysx

def sum_factors(n):
    factor = [i for i in range(1, n // 2 + 1) if n % i == 0]
    return sum(factor)

def is_perfect(n1, n2):
    return n1 == n2


for line in sys.stdin:
    line = int(line.strip())
    factor = sum_factors(line)
    print(is_perfect(line, factor))
