class Account:

    account_balance = 0.00

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"The Name of this account is {self.name}"


new_account = Account("Samuel")
print(new_account.account_balance)




