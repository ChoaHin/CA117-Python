#!/usr/bin/env python3

import sys
# 5 11 22 0 66 17 99 100 18 68 73 44
# five eleven twenty-two zero sixty-six seventeen ninety-nine one hundred eighteen sixty-eight seventy-three forty-four

f_digit_dict = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

sp_dict = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirdteen',
    14: 'forteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    100: 'one hundred'
}

s_digit_dict = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety'
}

for line in sys.stdin:
    ans = []
    line = line.strip().split()
    for n in line:
        try:
            if len(n) == 1:
                ans.append(f_digit_dict[int(n)])
            elif n[0] == '1':
                ans.append(sp_dict[int(n)])
            elif int(n) < 100:
                token = []
                token.append(s_digit_dict[int(n[0])])
                if n[1] != '0':
                    token.append(f_digit_dict[int(n[1])])
                ans.append("-".join(token))
        except(KeyError):
            ans.append("unknown")
    print(" ".join(ans))
