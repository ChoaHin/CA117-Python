#!/usr/bin/env python3
# doing list or dictionary is way slower, and there is function to detech digit upper and lower
import sys

case = ["digit", "upper", "lower", "special"]
case_dic = {token: False for token in case}

for line in sys.stdin:
    line = line.strip()
    case_dic = {token: False for token in case}
    for char in line:
        if char.isdigit():
            case_dic["digit"] = True
        elif char.isupper():
            case_dic["upper"] = True
        elif char.islower():
            case_dic["lower"] = True
        else:
            case_dic["special"] = True
    level = 0
    for x in case_dic:
        level = level + case_dic[x]

    print(level)
