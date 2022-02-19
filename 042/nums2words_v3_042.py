#!/usr/bin/env python3

import sys
# 5 1 2 0 6 7 9 10 8 8 3 4
# cuig aon do naid se seacht naoi deich ocht ocht tri ceathar

words = 'zero,one,two,three,four,five,six,seven,eight,nine,ten'
n2w_dict = {str(n): w for n, w in enumerate(words.split(","))}

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
    w2tran_dict = {}
    for line in lines:
        [num, word] = line.strip().split()
        w2tran_dict[str(num)] = word

for line in sys.stdin:
    ans = []
    line = line.strip().split()
    for n in line:
        try:
            ans.append(w2tran_dict[n2w_dict[n]])
        except(KeyError):
            ans.append("unknown")
    print(" ".join(ans))
