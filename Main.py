import auth as au
import bank as bk
import storage as st

loaded_accounts = st.load_data()

bank = bk.Bank()
bank.accounts = loaded_accounts


def clear_screen():
    print("\033[2J\033[H", end="")


def line(width=50, char="="):
    return char * width


def title(text):
    print(line())
    print(text.center(50))
    print(line())


def menu(options, heading):
    print(f"\n{heading}")
    print(line(50, "-"))
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")
    print(line(50, "-"))


def prompt_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print("Invalid choice. Please try again.")


def prompt_amount(prompt):
    while True:
        try:
            amount = float(input(prompt).strip())
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
            return amount
        except ValueError:
            print("Please enter a valid number.")


while True:
    clear_screen()
    title("NATIONAL TRUST BANK - SECURE CONSOLE")
    menu(["Create Account", "Login", "Exit"], "MAIN MENU")
    choice = prompt_choice("Enter your choice: ", {"1", "2", "3"})

    if choice == "1":
        clear_screen()
        title("CREATE ACCOUNT")
        name = input("Enter account holder name: ")

        while True:
            set_pass = input("Do you want to set your own password? (y/n): ").lower()

            if set_pass == "y":
                password = input("Enter your password: ")
                break
            elif set_pass == "n":
                password = None
                break
            else:
                print("Please enter only 'y' or 'n'.")

        status, acc_no, pwd = bank.create_account(name, password)

        print("\nAccount created successfully!")
        print("Account Number:", acc_no)
        print("Password:", pwd)
        input("\nPress Enter to return to the main menu...")

        st.save_data(bank.accounts)


    elif choice == "2":
        clear_screen()
        title("LOGIN")
        acc_no = input("Enter account number: ")
        password = input("Enter password: ")

        status, result = au.login(bank, acc_no, password)

        if not status:
            print(result)
            input("\nPress Enter to return to the main menu...")
        else:
            account = result
            print(f"\nWelcome, {account.account_holder_name}")

            while True:
                menu(
                    ["Deposit", "Withdraw", "View Transactions", "Logout"],
                    "ACCOUNT MENU"
                )
                acc_choice = prompt_choice("Enter choice: ", {"1", "2", "3", "4"})

                if acc_choice == "1":
                    amount = prompt_amount("Enter amount to deposit: ")
                    s, m = account.deposit(amount)
                    print(m)
                    if s:
                        st.save_data(bank.accounts)
                    input("Press Enter to continue...")

                elif acc_choice == "2":
                    amount = prompt_amount("Enter amount to withdraw: ")
                    s, m = account.withdraw(amount)
                    print(m)
                    if s:
                        st.save_data(bank.accounts)
                    input("Press Enter to continue...")

                elif acc_choice == "3":
                    transactions = account.show_transactions()
                    print("\nTRANSACTIONS")
                    print(line(50, "-"))
                    if not transactions:
                        print("No transactions found.")
                    else:
                        for txn in transactions:
                            print(txn)
                    print(line(50, "-"))
                    input("Press Enter to continue...")

                elif acc_choice == "4":
                    st.save_data(bank.accounts)
                    break
    elif choice == "3":
        clear_screen()
        title("THANK YOU")
        print("Your data has been saved.")
        st.save_data(bank.accounts)
        break
