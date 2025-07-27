#  Import what we need from the datetime module
from datetime import datetime, timedelta

#  Part 1: Function to display the current date and time
def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
 
    # Format the date to a readable string: "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")

     # Print the result
    print("Current date and time:", formatted_date)

     # Part 2: Function to calculate the future date
def calculate_future_date(days):
    # Get today's date (current date and time)
    today = datetime.now()
    
    # Add the number of days to today using timedelta
    future_date = today + timedelta(days=days)
    
    # Format the future date to just "YYYY-MM-DD"
    formatted_future = future_date.strftime("%Y-%m-%d")
    
    # Print the result
    print("Future date:", formatted_future)

    #  Main block: This runs only if the script is run directly
if __name__ == "__main__":
    # Call the function to display current date and time
    display_current_datetime()

    # Ask the user to input a number of days
    try:
        # Get input and convert to integer
        days_input = int(input("Enter the number of days to add to the current date: "))

        # Call the future date calculation function
        calculate_future_date(days_input)

    except ValueError:
        # Handle if the user didn't enter a number
        print("Invalid input! Please enter a number.")