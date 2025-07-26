
# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9  # For converting Fahrenheit to Celsius C = (F−32)× 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5  # For converting Celsius to Fahrenheit F = C x 9/5 + 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

def main():
    try:
# Ask the user to enter a temperature value
# Try to convert the input to a float (to allow decimals)
        temperature = float(input("Enter the temperature to convert: "))

 # Ask the user whether the input is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

           # If user enters C (Celsius), convert to Fahrenheit
        if unit == 'C':
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted}°F")

             # If user enters F (Fahrenheit), convert to Celsius
        elif unit == 'F':
            converted = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted}°C")

        # If the unit is not C or F, show error
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    # If user enters something that is not a number, catch the error
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Only run the main function if this file is being executed directly
if __name__ == "__main__":
    main()