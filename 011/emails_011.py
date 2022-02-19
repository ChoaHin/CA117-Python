#!/usr/bin/env python3

import sys

def email_name(s):
    position = s.find("@")
    s = (s[:position])
    [name, surname] = s.split(".")
    surname = "".join(char for char in surname if char.isalpha())
    full_name = name.capitalize(), surname.capitalize()
    return " ".join(full_name)


for line in sys.stdin:
    print(email_name(line))