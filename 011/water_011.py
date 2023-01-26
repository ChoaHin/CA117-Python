#!/usr/bin/env python3

import sys

[water, buckets] = sys.stdin.readlines()
buckets = buckets.split()

filled_busket_counter = 0 #number of busket could be filled
total_volumn = 0  #total empty volumn
for token in buckets:
    total_volumn += int(token)
    if total_volumn <= int(water):
        #add counter only when all busket could be filled
        filled_busket_counter += 1

print(filled)
