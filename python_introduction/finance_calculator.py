# Ask the user to enter their monthly income
# We convert the input to a float in case they enter values like 5000.50
income = float(input("Enter your monthly income: "))

# Ask the user to enter their total monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings by subtracting expenses from income
monthly_savings = income - expenses

# Project annual savings using the formula:
# Annual savings = (monthly savings * 12) + (5% interest on yearly savings)
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print out the user's monthly savings
print("Your monthly savings are $" + str(monthly_savings) + ".")

# Print out the projected annual savings including interest
print("Projected savings after one year, with interest, is: $" + str(annual_savings) + ".")
