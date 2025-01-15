class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amout):
        self.account_balance += amout

    def withdraw(self, amount):
        if self.account_balance > amount:
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")
