import random as rm
import account as ac


class Bank:
    def __init__(self):
        self.accounts = {}

    def generate_account_number(self):
        while True:
            acc_no = str(rm.randint(10000000, 99999999))
            if acc_no not in self.accounts:
                return acc_no

    def generate_password(self, length=8):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        password = ''.join(rm.choice(characters) for _ in range(length))
        return password

    def create_account(self, account_holder_name, password=None):
        account_number = self.generate_account_number()

        if password is None:
            password = self.generate_password()

        new_account = ac.Account(account_number, account_holder_name, password)
        self.accounts[account_number] = new_account

        return True, account_number, password

    def get_account(self, account_number):
        return self.accounts.get(account_number, None)
