
from decimal import Decimal, InvalidOperation

from app.models.transaction import Income, Expense


class Account:

    def __init__(self, owner, initial_balance=0):

        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Account owner cannot be empty")

        self.owner = owner.strip()

        self.__balance = self._validate_amount(
            initial_balance,
            allow_zero=True
        )

        # Store all income and expense objects
        self.__transactions = []

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
        return self.__balance

    @property
    def transactions(self):
        # Return a tuple so callers cannot modify our list
        return tuple(self.__transactions)

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

    def add_income(self, income):

        if not isinstance(income, Income):
            raise TypeError("Expected an Income object")

        self.deposit(income.amount)

        self.__transactions.append(income)

        return f"Income added: {income.get_details()}"

    def add_expense(self, expense):

        if not isinstance(expense, Expense):
            raise TypeError("Expected an Expense object")

        self.withdraw(expense.amount)

        self.__transactions.append(expense)

        return f"Expense added: {expense.get_details()}"

    def get_transaction_history(self):

        for transaction in self.__transactions:
            print(transaction.get_details())
