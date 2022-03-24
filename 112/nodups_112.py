#!/usr/bin/env python3

from string import punctuation
import sys

seen = []
for line in sys.stdin:
    line = line.split()
    for i, word in enumerate(line):
        word = word.lower().strip(punctuation)
        if word not in seen:
            seen.append(word)
        else:
            line[i] = '.'
    print(' '.join(line))
