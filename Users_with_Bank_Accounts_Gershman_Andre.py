class BankAccount:
    def __init__(self, balance, int_rate):
        self.balance = balance
        self.rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        fee = 5
        if amount > self.balance:
            self.balance -= fee
            print("Insufficient funds: Charging a $5 fee")
            return self
        else:
            self.balance -= amount
            return self

    def add_interest(self, int_rate=.02):
        interest = self.balance * int_rate
        self.balance += interest
        return self

    def display_account_info(self,):
        print("Current Balance:", self.balance)
        return self


class User:
    def __init__(self, name, email,):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self,):
        print(self.name)
        self.account.display_account_info()
        return self

    def added_interest(self,):
        self.account.add_interest()
        return self

    def transfer(self, other_user, amount):
        if self.account.balance < amount:
            print("Insufficient funds.")
            return self
        else:
            self.account.withdrawal(amount)
            other_user.account.deposit(amount)
            print(f"{self.name} transferred {amount} to {other_user.name}")
            return self


user1 = User("John", "@yahoo.com")
user1.make_deposit(200).make_deposit(
    150).added_interest().display_user_balance()

user2 = User("Doug", "@gmail.com")
user2.make_deposit(600).make_withdrawal(
    300).added_interest().display_user_balance()

user1.transfer(user2, 250)
user1.display_user_balance()
user2.display_user_balance()
