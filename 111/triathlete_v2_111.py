#!/usr/bin/env python3

class Triathlete():
    def __init__(self, name, tid):
        self.d = {}
        self.name = name
        self.tid = tid

    def __str__(self):
        a = []
        a.append('Name: {}'.format(self.name))
        a.append('ID: {}'.format(self.tid))
        a.append('Race time: {}'.format(self.total_time()))
        return "\n".join(a)

    def total_time(self):
        return sum(self.d.values())

    def add_time(self, obj, time):
        self.d[obj] = time

    def get_time(self, obj):
        return self.d[obj]
