#!/usr/bin/env python3

import sys
# 5 1 2 0 6 7 9 10 8 8 3 4
# five one two zero six seven nine ten eight eight three four
words = 'zero,one,two,three,four,five,six,seven,eight,nine,ten'
n2w_dict = {n: w for n, w in enumerate(words.split(","))}

for line in sys.stdin:
    ans = []
    line = line.strip().split()
    for n in line:
        ans.append(n2w_dict[int(n)])
    print(" ".join(ans))
