class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an initial balance."""
        self._account_balance = initial_balance if initial_balance >= 0 else 0
    def deposit(self, amount):
        """Deposit a specified amount into the account."""

        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        """Withdraw a specified amount from the account."""
        if amount > 0:  # Check if the withdrawal amount is positive
            if self._account_balance >= amount:  # Ensure the account has sufficient balance for the withdrawal
                self._account_balance -= amount  # Deduct the withdrawal amount from the account balance
                return True  # Return True to indicate the withdrawal was successful
            else:
                return False  # Return False if the account balance is insufficient for the withdrawal
        else:
            print("Withdrawal amount must be positive.")  # Inform the user that the withdrawal amount must be positive
            return False  # Return False to indicate the withdrawal was unsuccessful due to invalid input
    def display_balance(self):
        """Display the current account balance."""
        return f"Current balance: ${self._account_balance:.2f}"