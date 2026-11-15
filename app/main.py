# from app.models.transaction import Income, Expense

# # Create income object

# salary = Income(30000,"Monthly Salary","Company Salary")

# # Create Expense object

# food = Expense(3000,"Monthly Food","Food")


# # Display Transaction details

# print(salary.get_details())
# print(food.get_details())





from app.models.account import Account


# Create an account
account = Account("Ajit", 10000)

print("Account Owner:", account.owner)
print("Initial Balance:", account.balance)


# Deposit money
print(account.deposit(2000))

# Withdraw money
print(account.withdraw(3000))

# Check final balance
print("Final Balance:", account.balance)

