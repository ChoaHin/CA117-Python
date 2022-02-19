#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r") as f:
    a = f.read().split()
with open(sys.argv[2], "r") as f:
    b = f.read().split()

i = 0
while i < len(a):
    print(f"{a[i]}\n{b[i]}")
    i += 1
