#!/usr/bin/env python3

#1 3 1990
#12 10 1992
#9 5 1995

import sys
import calendar

for line in sys.stdin:
    [day, month, year] = line.strip().split()
    weekday = calendar.weekday(int(year), int(month), int(day))
    if weekday == 0:
        print("You were born on a Monday and Monday's child is fair of face.")
    elif weekday == 1:
        print("You were born on a Tuesday and Tuesday's child is full of grace.")
    elif weekday == 2:
        print("You were born on a Wednesday and Wednesday's child is full of woe.")
    elif weekday == 3:
        print("You were born on a Thursday and Thursday's child has far to go.")
    elif weekday == 4:
        print("You were born on a Friday and Friday's child is loving and giving.")
    elif weekday == 5:
        print("You were born on a Saturday and Saturday's child works hard for a living.")
    elif weekday == 6:
        print("You were born on a Sunday and Sunday's child is fair and wise and good in every way.")
