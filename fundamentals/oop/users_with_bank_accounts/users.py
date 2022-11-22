from bank_accounts import BankAccount

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = BankAccount(int_rate = 0.1, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info()
    def transfer_money(self, amount, other_user):
        self.account.withdraw(amount)
        other_user.make_deposit(amount)

cole = User('cole','jacobs','cole@gmail.com',23)
aaron = User('aaron','andrews','aaron@gmail.com',41)

# Add a display_user_balance method to the User class that displays user's account balance

# SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

# SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.






