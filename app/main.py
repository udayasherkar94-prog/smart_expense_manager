from app.models.transaction import Income, Expense

# Create income object

salary = Income(30000,"Monthly Salary","Company Salary")

# Create Expense object

food = Expense(3000,"Monthly Food","Food")


# Display Transaction details

print(salary.get_details())
print(food.get_details())
