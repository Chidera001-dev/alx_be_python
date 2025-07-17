# Enter your task description
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority :
    case "high":
           message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        message = f"Reminder: '{task}' is a low priority task."
    case _:
        message = f"Reminder: '{task}' has an unknown priority level."


# Step 3: Check if the task is time-bound
if time_bound == "yes":
    message += " That requires immediate attention today!"

# Step 4: Display the final reminder
print(message)

