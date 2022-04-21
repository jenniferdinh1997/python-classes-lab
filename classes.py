import random

class BankAccount():
    def __init__(self,owner,balance,account_no):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        self.balance -= amount

    def __str__(self):
        return f'Account {self.account_no} / Balance: {self.balance}'   


joe_account = BankAccount('Joe',50,111)
print(joe_account)

joe_account.deposit(100)
print(joe_account)

class SavingsAccount():
    def __init__(self,owner,balance,account_no):
        BankAccount.__init__(self,owner,balance,account_no)

    def withdraw(self,amount):
        print('No withdrawals permitted')

    def __str__(self):
        return f'Account {self.account_no} / Balance: {self.balance}' 

bill_account = SavingsAccount('Bill',100,111)
bill_account.withdraw(100)
print(bill_account)
