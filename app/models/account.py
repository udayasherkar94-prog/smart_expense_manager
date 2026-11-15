
from decimal import Decimal, InvalidOperation


class Account:

    def __init__(self, owner, initial_balance=0):

        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Account owner cannot be empty")

        self.owner = owner.strip()

        # Private attribute
        self.__balance = self._validate_amount(
            initial_balance,
            allow_zero=True
        )

    def _validate_amount(self, amount, allow_zero=False):

        try:
            amount = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number")

        if not amount.is_finite():
            raise ValueError("Amount must be a finite number")

        if allow_zero:
            if amount < 0:
                raise ValueError("Balance cannot be negative")
        elif amount <= 0:
            raise ValueError("Amount must be greater than zero")

        return amount

    @property
    def balance(self):
        # Read-only access to the private balance
        return self.__balance

    def deposit(self, amount):

        amount = self._validate_amount(amount)

        self.__balance += amount

        return f"Deposit successful. Balance: Rs. {self.__balance:.2f}"

    def withdraw(self, amount):

        amount = self._validate_amount(amount)

        if amount > self.__balance:
            raise ValueError("Insufficient account balance")

        self.__balance -= amount

        return f"Withdrawal successful. Balance: Rs. {self.__balance:.2f}"
