#!/usr/bin/env python3

import sys
import string

def alnum(s):
    stripped = [word.strip(string.punctuation) for word in s]
    return stripped

def word(ls, dic):
    for word in ls:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] += 1
    return dic


word_ls = {}
lines = sys.stdin.read().lower().split()
lines = alnum(lines)
(word(lines, word_ls))
for k, v in sorted(word_ls.items()):
    print(f'{k} : {v}')
