#!/usr/bin/env python3

import sys
#Primes: [2, 3, 5, 7]
def primecomps(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


for line in sys.stdin:
    num = int(line.strip()) + 1
    primes = [n for n in range(num) if primecomps(n)]
    print("Primes:", primes)
