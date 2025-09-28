class BankAccount:
    def __init__(self):
        self.balance = 0
        print(f"Current balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

# Create an instance of BankAccount
account = BankAccount()

# Deposit amount
deposit_amount = int(input("Enter the deposit amount: "))
account.deposit(deposit_amount)

# Withdraw amount
withdraw_amount = float(input("Enter the withdrawal amount: "))
account.withdraw(withdraw_amount)

# Print the current balance
print(f"Current balance: {account.get_balance()}")
