# arithmetic_operations.py

# Define the function to perform arithmetic operations

def perform_operation(num1, num2, operation):

    match operation:
        case "add":
            return num1 + num2
        case "substract":
            return num1 - num2
        case "multipy":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            else :
                return num1 / num2
        case _ :
               return "Error: Invalid operation"
        


