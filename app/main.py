# from app.models.transaction import Income, Expense

# # Create income object

# salary = Income(30000,"Monthly Salary","Company Salary")

# # Create Expense object

# food = Expense(3000,"Monthly Food","Food")


# # Display Transaction details

# print(salary.get_details())
# print(food.get_details())






from app.models.account import Account
from app.models.transaction import Income, Expense


# Create an account
account = Account("Ajit")

# Create income transaction
salary = Income(
    30000,
    "Monthly Salary",
    "Company Salary"
)

# Create expense transactions
food = Expense(
    3000,
    "Monthly Food",
    "Food"
)

travel = Expense(
    2000,
    "Travel Expenses",
    "Transportation"
)


# Add transactions to account
print(account.add_income(salary))
print(account.add_expense(food))
print(account.add_expense(travel))


# Display account information
print("\nAccount Owner:", account.owner)
print("Current Balance:", account.balance)


# Display transaction history
print("\nTransaction History:")
account.get_transaction_history()


