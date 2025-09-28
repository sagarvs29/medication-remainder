from abc import ABC, abstractmethod

# Abstract base class
class Account(ABC):
    def __init__(self, acc_number):
        self.acc_number = acc_number

    @abstractmethod
    def account_type(self):
        pass

class CheckAccount(Account):
    def __init__(self, acc_number, acc_holdername):
        super().__init__(acc_number)
        self.acc_holdername = acc_holdername

    def account_type(self):
        return "Checking Account"

class SavingAccount(Account):
    def __init__(self, acc_number, balance=0):
        super().__init__(acc_number)
        self.balance = balance

    def account_type(self):
        return "Saving Account"

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        self.balance -= amount

    def check_balance(self):
        print(f"Balance: {self.balance}")

# Example usage
saving_acc = SavingAccount("123456", 1000)
saving_acc.deposit(500)
saving_acc.withdrawal(200)
saving_acc.check_balance()
print(saving_acc.account_type())

check_acc = CheckAccount("789012", "John Doe")
print(check_acc.account_type())
