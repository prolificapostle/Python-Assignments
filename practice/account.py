from decimal import Decimal


class Account:

    bonus = 50

    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative..")
        self.__balance = amount

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount to deposit cannot be negative ")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient Balance")
        self.balance -= amount

    def __str__(self):
        return f"Name Of Account: {self.name} \nAccount Balance: {self.balance}"

    @classmethod
    def set_bonus(cls, amount):
        cls.bonus = amount


account2 = Account("Torin", Decimal(1000.00))
Account.set_bonus(400)
print(account2.bonus + account2.balance)





