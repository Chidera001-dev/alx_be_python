# Ask the user for their current age
# input() shows a question and waits for the user to type something
# int() converts the input (which is text) into a number
age = int(input("How old are you? "))

# Calculate how old the user will be in 2050
# Since the current year is 2023, we add 27 years
future_age = age + 27

# Print the result in a clear sentence
print("In 2050, you will be", future_age, "years old.")