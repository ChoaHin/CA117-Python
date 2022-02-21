#!/usr/bin/env python3

import sys

location = sys.stdin.readline().strip()
p = sys.stdin.read().strip()

def A(ls):
    tmp = ls[0]
    ls[0] = ls[1]
    ls[1] = tmp
    return ls

def B(ls):
    tmp = ls[1]
    ls[1] = ls[2]
    ls[2] = tmp
    return ls

def C(ls):
    tmp = ls[0]
    ls[0] = ls[2]
    ls[2] = tmp
    return ls


prize = '123'
prize = prize.replace(location, '0')
prize_ls = [char for char in prize]

for char in p:
    if char == 'A':
        prize_ls = A(prize_ls)
    elif char == 'B':
        prize_ls = B(prize_ls)
    elif char == 'C':
        prize_ls = C(prize_ls)

print(''.join(prize_ls).find('0') + 1)
