# Enter your task description
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")


match priority :
    case "high":
        print(f"Reminder: '{task}' is a high priority task.")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task.")
    case "low":
        print(f"Reminder: '{task}' is a low priority task.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level.")


# Step 3: Check if the task is time-bound
if time_bound == "yes":
    print("That requires immediate attention today!")



