#!/usr/bin/env python3

class Contact():
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return ('{} {} {}'.format(self.name, self.phone, self.email))

class ContactList():
    def __init__(self):
        self.d = {}

    def add(self, data):
        self.d[data.name] = data

    def remove(self, data):
        if data in self.d:
            del self.d[data]

    def get(self, data):
        if data in self.d:
            return self.d[data]

    def __str__(self):
        s = []
        s.append('Contact list')
        s.append('------------')
        for k, v in sorted(self.d.items()):
            s.append(f'{v}')
        return "\n".join(s)
