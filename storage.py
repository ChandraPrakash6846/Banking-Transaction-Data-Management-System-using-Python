import json as js
import os
import account as ac


def save_data(accounts, filename="bank_data.json"):
    data = {acc_num: acc.to_dict() for acc_num, acc in accounts.items()}
    with open(filename, 'w') as f:
        js.dump(data, f, indent=4)

def load_data(filename="bank_data.json"):
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as f:
        data = js.load(f)
        accounts = {acc_num: ac.Account.from_dict(acc_data) for acc_num, acc_data in data.items()}
        return accounts