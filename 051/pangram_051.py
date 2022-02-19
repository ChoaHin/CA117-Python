#!/usr/bin/env python3

import sys
import string

for line in sys.stdin:
    complete = {n: True for n in [char for char in string.ascii_lowercase]}
    line = line.lower().strip()
    pangram_check = []
    for char in complete:
        if char not in line:
            pangram_check.append(char)
    if pangram_check:
        print(f'missing {"".join(n for n in pangram_check)}')
    else:
        print("pangram")
