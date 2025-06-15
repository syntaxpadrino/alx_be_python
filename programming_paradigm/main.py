import sys
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def load_balance():
    """Load the account balance from a file, or return default if not found."""
    try:
        with open(BALANCE_FILE, "r") as f:
            balance = float(f.read())
            print(f"[DEBUG] Loaded balance: {balance}")
            return balance
    except (FileNotFoundError, ValueError):
        print("[DEBUG] No balance file found, using default 100")
        return 100  # Default starting balance

def save_balance(balance):
    """Save the current account balance to a file."""
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))
    print(f"[DEBUG] Saved balance: {balance}")

def main():
    # Initialize account with a starting balance of 100 or from file
    balance = load_balance()
    account = BankAccount(balance)

    # Check if a command was provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse the command and optional amount
    try:
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params else None
    except ValueError:
        print("Invalid command format. Use <command>:<amount> or display")
        sys.exit(1)

    # Execute the command
    if command == "deposit" and amount is not None:
        if amount > 0:
            account.deposit(amount)
            save_balance(account._account_balance)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if amount > 0:
            if account.withdraw(amount):
                save_balance(account._account_balance)
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
    elif command == "display" and amount is None:
        print(account.display_balance())
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()