task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        msg = f"Reminder: '{task}' is a high priority task"
    case "medium":
        msg = f"Note: '{task}' is a medium priority task"
    case "low":
        msg = f"Note: '{task}' is a low priority task"
    case _:
        msg = f"Task: '{task}'"

if time_bound == "yes":
    msg += " that requires immediate attention today!"
else:
    msg += ". Consider completing it when you have free time."

print(msg)

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Prepare base message
if priority == "high":
    message = f"Reminder: '{task}' is a high priority task"
elif priority in ["medium", "low"]:
    message = f"Note: '{task}' is a {priority} priority task"
else:
    message = f"Note: '{task}' has an unspecified priority"

# Add time sensitivity note
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

print(message)

