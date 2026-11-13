from decimal import Decimal,InvalidOperation

# Parent Class

class Transaction:

        def __init__(self,amount,description):

                try:
                        amount = Decimal(str(amount))

                except (InvalidOperation,ValueError):
                        raise ValueError("Amount must be a valid number")       

                if not amount.is_finite() or amount <= 0:

                        raise ValueError("Amount must be greater than zero")

                if not isinstance(description,str) or not description.strip():

                        # no description.strip() evaluate true if description is empty
                        # if it have only whitespace and tabs not chars it returns None
                        # false if it contains any char or string

                        raise ValueError("Description cannot be empty")

                self.amount = amount
                self.description = description.strip()

        def get_details(self):
                return f"{self.description}: Rs. {self.amount:.2f}"



# child class

class Income(Transaction):

        def __init__(self,amount,description,source):

                super().__init__(amount,description)

                self.source = source

        def get_details(self):
                return f"Income | {self.source} | {self.description} | Rs. {self.amount:.2f}"



# child class

class Expense(Transaction):

        def __init__(self, amount, description,category):
                super().__init__(amount, description)

                self.category = category 


        def get_details(self):
                return f"Expense | {self.category} | {self.description} | Rs.{self.amount:.2f}"



                       
