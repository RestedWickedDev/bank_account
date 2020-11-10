import random

class BankAccount:

    ### ATTRIBUTES
    def __init__(self, full_name, account_number, routing_number, balance) :
        self.full_name = full_name
        self.account_number = random.randint(10000000, 99999999)
        self.routing_number = 594434573
        self.balance = 0

    ### METHODS

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited: $" + str(amount))

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Amount Withdrawn: $" + str(amount))
        else:
            print("Amount Withdrawn; $" + str(amount))
            print("Insufficient funds")
            self.balance = self.balance - amount - 10
            print("You've been charged a $10 dollar overdraft fee")

    def get_balance(self):
        print("Your balance is: $" + str(self.balance))

    def add_interest(self):
        interest = self.balance *  0.00083 
        self.balance = self.balance + interest
        print("You've been paid $" + str(interest) + " in interest")

    def print_receipt(self):
        print("Full Name: " + str(self.full_name))
        print("Account Number: " + str(self.account_number))
        print("Routing Number: " + str(self.routing_number))
        print("Balance: $" + str(self.balance))


user = BankAccount("David", 0, 0, 0)
user.print_receipt()
user.deposit(100)
user.withdraw(110)
user.get_balance()
print()
user.print_receipt()

print()

user = BankAccount("Marco", 0, 0, 0)
user.print_receipt()
user.deposit(4000)
user.withdraw(433)
user.get_balance()
print()
user.print_receipt()

print()

user = BankAccount("Angel", 0, 0, 0)
user.print_receipt()
user.deposit(20000)
user.add_interest()
user.get_balance()
print()
user.print_receipt()