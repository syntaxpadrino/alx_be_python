import sys
import os
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            try:
                return float(f.read())
            except ValueError:
                return 0.0
    return 0.0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def main():
    # Load previous balance
    current_balance = load_balance()
    account = BankAccount(current_balance)

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command, *params = sys.argv[1].split(":")
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid command format. Use <command>:<amount> or display")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display" and amount is None:
        print(account.display_balance())
    else:
        print("Invalid command or missing amount.")
        sys.exit(1)

    # Save the updated balance
    save_balance(account._account_balance)

if __name__ == "__main__":
    main()
