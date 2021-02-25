"""
Question 7

"""
class BankAccount:
    def __init__(self, initial_balance):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0
        
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance = self.balance + amount
        
    def withdraw(self, amount):
        """
        Withdraws the amount from the account.  Each withdrawal resulting in a
        negative balance also deducts a penalty fee of 5 dollars from the balance.
        """
        self.balance = self.balance - amount
        if (self.balance < 0) :
            self.fees = self.fees + 5
            self.balance = self.balance - 5
        
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
        
    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees

my_account = BankAccount(10)
my_account.withdraw(15)
my_account.deposit(20)
print my_account.get_balance(), my_account.get_fees()

"""
Question 8

"""
class BankAccount:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.fees = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance = self.balance - amount
        if (self.balance < 0) :
            self.fees = self.fees + 5
            self.balance = self.balance - 5
        """
        Withdraws the amount from the account.  Each withdrawal
        resulting in a negative balance also deducts a penalty 
        fee of 5 dollars from the balance.
        """

    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance

    def get_fees(self):
        """Returns the total fees ever deducted from the account."""
        return self.fees
    
        
account1 = BankAccount(10)
account1.withdraw(15)
account2 = BankAccount(15)
account2.deposit(10)
account1.deposit(20)
account2.withdraw(20)
print account1.get_balance(), account1.get_fees(), account2.get_balance(), account2.get_fees()
