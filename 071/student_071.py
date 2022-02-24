#!/usr/bin/env python3

class Student():
    def set_attributes(self, sid, name, modlist=None):

        self.sid = sid
        self.name = name
        self.modlist = [] if modlist is None else modlist

    def print_attributes(self):
            print(
                f'ID: {self.sid}\n'
                f'Name: {self.name}\n'
                f'Modules: {", ".join(self.modlist)}')

    def add_module(self, module):
        if module not in self.modlist:
            self.modlist.append(module)

    def del_module(self, module):
        if module in self.modlist:
            self.modlist.remove(module)
