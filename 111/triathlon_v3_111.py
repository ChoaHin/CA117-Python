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
        total = sum(self.d.values())
        a.append('Race time: {}'.format(total))
        return "\n".join(a)

    def add_time(self, obj, time):
        self.d[obj] = time

    def get_time(self, obj):
        return self.d[obj]

    def __eq__(self, other):
        return sum(self.d.values()) == sum(other.d.values())

    def __gt__(self, other):
        return sum(self.d.values()) > sum(other.d.values())

def sorter(t):
    return t.name

class Triathlon():
    def __init__(self):
        self.d = {}

    def add(self, t):
        self.d[t.name] = t

    def remove(self, tid):
        del self.d[tid]

    def lookup(self, tid):
        if tid in self.d:
            return self.d[tid]
        return None

    def __str__(self):
        lista = [f'{t}' for t in sorted(self.d.values(), key=sorter)]
        return '\n'.join(lista)

    def best(self):
        return min(self.d.values())

    def worst(self):
        return max(self.d.values())
