class Property:
    def __init__(self, purchase_price, current_value, rental_income, expenses, loan_amount):
        self.validate_positive_value(purchase_price, "Purchase Price")
        self.validate_positive_value(current_value, "Current Value")
        self.validate_positive_value(rental_income, "Rental Income")
        self.validate_positive_value(expenses, "Expenses")
        self.validate_positive_value(loan_amount, "Loan Amount")

        self.purchase_price = purchase_price
        self.current_value = current_value
        self.rental_income = rental_income
        self.expenses = expenses
        self.loan_amount = loan_amount

    def validate_positive_value(self, value, attribute_name):
        if value < 0:
            raise ValueError(f"{attribute_name} must be a positive value.")

    def calculate_appreciation(self):
        return ((self.current_value - self.purchase_price) / self.purchase_price) * 100

    def calculate_monthly_roi(self):
        net_income = self.rental_income * 12 - self.expenses
        return (net_income / self.purchase_price) * 100

    def calculate_total_roi(self):
        net_income = (self.current_value - self.purchase_price + self.rental_income * 12) - self.expenses
        return (net_income / self.purchase_price) * 100

# User input and instance creation
try:
    purchase_price = float(input("Enter Purchase Price: "))
    current_value = float(input("Enter Current Value: "))
    rental_income = float(input("Enter Rental Income: "))
    expenses = float(input("Enter Expenses: "))
    loan_amount = float(input("Enter Loan Amount: "))

    # Create an instance of the Property class
    property_instance = Property(purchase_price, current_value, rental_income, expenses, loan_amount)

    # Display the results
    print(f"\nResults for Property with Purchase Price: {purchase_price}, Current Value: {current_value}, Rental Income: {rental_income}, Expenses: {expenses}, Loan Amount: {loan_amount}")
    print(f"Annual Property Appreciation: {property_instance.calculate_appreciation()}%")
    print(f"Monthly ROI: {property_instance.calculate_monthly_roi()}%")
    print(f"Total ROI: {property_instance.calculate_total_roi()}%")

except ValueError as e:
    print(f"Error: {e}")
