import os
import sys
import csv
import json

current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
csv_file = os.path.join(current_dir, "bank_accounts.csv")
json_file = os.path.join(current_dir, "bank_accounts.json")


class BankAccount:
    minimum_balance = 50000

    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(
            f"| {self.account_number:9} | {self.account_name:15} | {self.balance:>15} |")

    def withdraw(self, amount):
        if 0 < amount <= self.balance - BankAccount.minimum_balance:
            self.balance -= amount
        else:
            raise ValueError(
                f"Số tiền trong tài khoản phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền trong tài khoản phải lớn hơn 0")

    @classmethod
    def from_csv(cls, csv_file):
        accounts = []

        with open(csv_file,encoding = 'utf8') as file:
            reader = csv.reader(file)

            for account_number, account_name, balance in reader:
                accounts.append(
                    cls(account_number, account_name, int(balance)))

        return accounts
    @classmethod
    def from_json(cls, json_file):
        accounts = []
        with open(json_file,encoding = 'utf8' ) as json_file1:
            data = json.load(json_file1)
            for p in data :
                 accounts.append(
                    cls(p['account_number'], p['account_name'], int(p['balance'])))
            
        return accounts

csv_accounts = BankAccount.from_csv(csv_file)
json_accounts = BankAccount.from_json(json_file)

print(f"| {'Number':9} | {'Account Name':15} | {'Balance':15} |")
print(f"|{'-' * 11}|{ '-' * 17 }|{'-' * 17}|")
for account in json_accounts:
    account.display()
