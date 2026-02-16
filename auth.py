def login(bank, account_number, password):
    account = bank.get_account(account_number)

    if account is None:
        return False, "Account not found."

    if account.password != password:
        return False, "Incorrect password."

    return True, account
