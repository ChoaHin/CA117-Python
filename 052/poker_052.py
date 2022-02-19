#!/usr/bin/env python3

import sys

rank = 'A23456789TJQK'
counter = {k: 0 for k in rank}

hand = sys.stdin.readline().strip().split()
for card in hand:
    counter[card[0]] += 1

print(max(counter.values()))
