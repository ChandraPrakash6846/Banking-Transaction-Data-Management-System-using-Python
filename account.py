class Account:
    def __init__(self,account_number,account_holder_name,password,balance = 0 ,transaction_history = None):
        self.account_number=account_number
        self.account_holder_name=account_holder_name
        self.password=password
        self.balance=balance
        self.transactions = transaction_history if transaction_history is not None else []

    def add_transaction(self,acc_type,amount):
        record = {
             "type": acc_type,
             "amount": amount,
            "balance": self.balance
            }
        self.transactions.append(record)

    def deposit(self,amount):
        if amount <= 0:
            return (False, "Deposit amount must be positive.")
        else:
            self.balance += amount
            self.add_transaction("Deposit", amount)
            return (True, f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self,amount):
        if amount <= 0:
            return (False, "Withdrawal amount must be positive.")
        elif amount > self.balance:
            return (False, "Insufficient funds.")
        else:
            self.balance -=amount
            self.add_transaction("Withdrawal", amount)
            return (True, f"Withdrew {amount}. New balance is {self.balance}.")
        
    def show_transactions(self):
        return self.transactions
    
    def to_dict(self):
        return {
            "account_number": self.account_number,
            "account_holder_name": self.account_holder_name,
            "password": self.password,
                "balance": self.balance,
            "transaction_history": self.transactions
        }
    
    def from_dict(data):
        return Account(
            account_number=data["account_number"],
            account_holder_name=data["account_holder_name"],
            password=data["password"],
            balance=data.get("balance", 0),
            transaction_history=data.get("transaction_history", [])
        )
