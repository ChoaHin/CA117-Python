#!/usr/bin/env python3

class Meeting():
    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)'

class Schedule():
    def __init__(self):
        self.d = {}

    def add(self, m):
        self.d[m.hour] = m

    def __str__(self):
        s = []
        s.append('Schedule')
        s.append('--------')
        for k, v in sorted(self.d.items()):
            s.append(f'{v}')
        s.append(f'Meetings today: {len(self.d)}')
        return '\n'.join(s)


# do a overload __eq__ and __gt__
# then the sort function will work