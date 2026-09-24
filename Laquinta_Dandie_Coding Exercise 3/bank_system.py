"""Secure Bank Account & ATM system demonstrating OOP fundamentals:
instance methods, encapsulation, abstraction, and properties."""


class BankAccount:
    """A bank account with a protected balance and a transaction log."""

    def __init__(self, account_holder, initial_deposit=0.0):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        self.account_holder = account_holder      # public attribute
        self._balance = initial_deposit           # non-public (by convention)
        self._transactions = []                   # internal log

    # ---- Property: balance -------------------------------------------
    @property
    def balance(self):
        """Current balance (read access)."""
        return self._balance

    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = new_balance

    # ---- Instance methods --------------------------------------------
    def deposit(self, amount):
        """Add funds. Returns the updated balance."""
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        self._balance += amount
        self._transactions.append(f"Deposit: +{amount:.2f}")
        return self._balance

    def withdraw(self, amount):
        """Remove funds. Returns the amount withdrawn."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than 0.")
        if self._balance < amount:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        self._transactions.append(f"Withdrawal: -{amount:.2f}")
        return amount

    def get_transaction_history(self):
        """Return a COPY so callers can't alter the internal log."""
        return self._transactions.copy()


class ATM:
    """Simple interface that hides BankAccount's validation details."""

    def __init__(self, bank_account):
        if not isinstance(bank_account, BankAccount):
            raise TypeError("bank_account must be a BankAccount instance.")
        self._account = bank_account
        self.__pin = "1234"                       # name-mangled: _ATM__pin
        self._is_authenticated = False

    def authenticate(self, entered_pin):
        if entered_pin == self.__pin:
            self._is_authenticated = True
            return True
        self._is_authenticated = False
        return False

    def check_balance(self):
        if not self._is_authenticated:
            print("Access denied: please authenticate first.")
            return None
        return self._account.balance

    def perform_deposit(self, amount):
        if not self._is_authenticated:
            print("Access denied: please authenticate first.")
            return False
        try:
            new_balance = self._account.deposit(amount)
            print(f"Deposit successful. New balance: {new_balance:.2f}")
            return True
        except ValueError as err:
            print(f"Deposit failed: {err}")
            return False

    def perform_withdrawal(self, amount):
        if not self._is_authenticated:
            print("Access denied: please authenticate first.")
            return False
        try:
            taken = self._account.withdraw(amount)
            print(f"Please take your cash: {taken:.2f}")
            return True
        except ValueError as err:
            print(f"Withdrawal failed: {err}")
            return False

    def print_mini_statement(self):
        if not self._is_authenticated:
            print("Access denied: please authenticate first.")
            return
        history = self._account.get_transaction_history()
        print("--- Mini Statement (last 3) ---")
        if not history:
            print("No transactions yet.")
        for entry in history[-3:]:
            print(entry)
        print("-------------------------------")


if __name__ == "__main__":
    print("=== 1. Account creation ===")
    acct = BankAccount("Ada Lovelace", 500.0)
    print(f"{acct.account_holder} starts with {acct.balance:.2f}")

    try:
        BankAccount("Bad Start", -50)
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("\n=== 2. Modifying balances ===")
    print("Deposit 250 ->", acct.deposit(250))
    print("Withdraw 100 ->", acct.withdraw(100))
    acct.balance = 900                            # valid setter use
    print("Setter set balance to", acct.balance)
    for label, action in [
        ("set balance = -5", lambda: setattr(acct, "balance", -5)),
        ("deposit -20", lambda: acct.deposit(-20)),
        ("withdraw 99999", lambda: acct.withdraw(99999)),
    ]:
        try:
            action()
        except ValueError as e:
            print(f"Invalid ({label}): {e}")

    print("\n=== 3. Direct access to atm.__pin ===")
    atm = ATM(acct)
    try:
        print(atm.__pin)
    except AttributeError as e:
        print(f"AttributeError: {e}")
    print("(Mangled name still exists:", hasattr(atm, "_ATM__pin"), ")")

    print("\n=== 4. Full ATM workflow ===")
    print("Balance before login:", atm.check_balance())
    print("Wrong PIN:", atm.authenticate("0000"))
    print("Correct PIN:", atm.authenticate("1234"))
    print("Balance:", atm.check_balance())
    atm.perform_deposit(150)
    atm.perform_deposit(-10)
    atm.perform_withdrawal(200)
    atm.perform_withdrawal(1_000_000)
    atm.print_mini_statement()