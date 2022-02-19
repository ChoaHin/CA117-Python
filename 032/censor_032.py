#!/usr/bin/env python3

import sys

with open(sys.argv[1], "r")as f:
    words = f.read().split()

for line in sys.stdin:
    for word in words:
        line = line.replace(word, "@" * len(word))
    print(line.strip())
