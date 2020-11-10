class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance) :
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

    ### METHODS

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Amount Deposited: $" + str(self.balance))

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
            print("Amount Withdrawn: $" + str(self.balance))
        else:
            print("Insufficient funds")

    def get_balance(self):
        print("Your balance is: $" + str(self.balance))

    def add_interest(self):
        interest = self.balance *  0.00083 
        self.balance = self.balance + interest

    def print_receipt(self):
        print(self.full_name)
        print(self.account_number)
        print(self.routing_number)
        print(self.balance)

