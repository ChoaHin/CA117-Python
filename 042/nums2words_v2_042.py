#!/usr/bin/env python3

import sys
# 5 1 2 b 6 7 99 10 8 8 3 4
# five one two unknown six seven unknown ten eight eight three four
words = 'zero,one,two,three,four,five,six,seven,eight,nine,ten'
n2w_dict = {str(n): w for n, w in enumerate(words.split(","))}

for line in sys.stdin:
    ans = []
    line = line.strip().split()
    for n in line:
        try:
            ans.append(n2w_dict[n])
        except(KeyError):
            ans.append("unknown")
    print(" ".join(ans))
