#!/usr/bin/env python3

class BankAccount():
    def set_attributes(self, name, number, balance):
        self.name = name
        self.number = number
        self.balance = balance

    def print_attributes(self):
        print(
            f'Name: {self.name}\n'
            f'Account number: {self.number}\n'
            f'Balance: {self.balance:.2f}'
        )

    def deposit(self, deposit):
        self.balance = self.balance + deposit
