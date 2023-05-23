from account import Account
from decimal import Decimal

if __name__ == '__main__':

    new_name = input("Enter Your Name: \n")

    new_balance = Decimal(input("Enter Your Opening Balance \n"))

    account1 = Account(new_name, new_balance)
    print(account1)
