from abc import ABC, abstractmethod

# Abstract base class
class Account(ABC):
    def __init__(self, acc_number):
        self.acc_number = acc_number

    @abstractmethod
    def account_type(self):
        pass

# Inherited class for CheckAccount
class CheckAccount(Account):
    def __init__(self, acc_number, acc_holdername):
        super().__init__(acc_number)
        self.acc_holdername = acc_holdername

    def account_type(self):
        return "Checking Account"

# Inherited class for SavingAccount
class SavingAccount(Account):
    def __init__(self, acc_number, balance=0):
        super().__init__(acc_number)
        self.balance = balance

    def account_type(self):
        return "Saving Account"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"The balance for account {self.acc_number} is {self.balance}.")

# 
#if __name__ == "__main__":
    # Create a SavingAccount object
saving_acc = SavingAccount(acc_number="123456", balance=1000)
    
    #  operations need to be performed
saving_acc.check_balance()
saving_acc.deposit(500)
saving_acc.withdrawal(200)
saving_acc.check_balance()
print(f"Account Type: {saving_acc.account_type()}")

    