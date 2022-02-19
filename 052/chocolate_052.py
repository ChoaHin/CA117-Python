#!/usr/bin/env python3

import sys

for line in sys.stdin:
    required = int(line.strip())
    i = 0
    while (i * 400) < required:
        i += 1
    print(i)
