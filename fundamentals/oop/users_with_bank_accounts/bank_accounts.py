class BankAccount:
    
    all_accounts = []
    # don't forget to add some default values for these parameters!
    # innit method has attriubites for the instance of the class
        # your code here! (remember, instance attributes go here)
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        print(self)
        # instance and object used almost interchagnaebly 
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(self.int_rate)
        print(self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self
        # the return self statment needed on all methods to allow chaining methods
    @classmethod
    def all_instances(cls):
        for account in cls.all_accounts:
            print(f"Your balance is {account.balance} and your and your interest rate is {account.int_rate}.")


# eric_account.deposit(500)
# eric_account.deposit(1200)
# eric_account.deposit(100)
# eric_account.withdraw(250)
# eric_account.yield_interest()
# eric_account.display_account_info()

# eric_account.deposit(500).deposit(1200).deposit(100).withdraw(250).yield_interest().display_account_info()

# lisa_account.deposit(500)
# lisa_account.deposit(4000)
# lisa_account.withdraw(100)
# lisa_account.withdraw(250)
# lisa_account.withdraw(1000)
# lisa_account.withdraw(50)
# lisa_account.yield_interest()
# lisa_account.display_account_info()

# lisa_account.deposit(500).deposit(4000).withdraw(100).withdraw(250).withdraw(1000).withdraw(50).yield_interest().display_account_info()