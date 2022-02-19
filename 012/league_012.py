#!/usr/bin/env python3

import sys

s = sys.stdin.readlines()

length = 0
for line in s:
    tokens = line.split()
    club = " ".join(tokens[1:-8])
    if len(club) > length:
        length = len(club)

print(f'POS {"CLUB":<{length}}  P   W   D   L  GF  GA  GD PTS')

for line in s:
    tokens = line.split()
    no = tokens[0]
    club = " ".join(tokens[1:-8])
    data_ls = tokens[-8:-2]
    sp_data_ls = tokens[-2:]

    new_data_ls = []
    for data_token in data_ls:
        new_data_ls.append(f"{data_token:>2}")
    data = "  ".join(new_data_ls)

    new_sp_data_ls = []
    for data_token in sp_data_ls:
        new_sp_data_ls.append(f"{data_token:>3}")
    sp_data = " ".join(new_sp_data_ls)

    print(f"{no: >3} {club:<{length}} {data} {sp_data}")
