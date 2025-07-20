# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Priority logic
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    # message += " that requires immediate attention today!"
        else: 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
    # message += ". Consider completing it when you have free time."
    #     message = (f"Reminder: '{task}' is a high priority task")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    # message += " that requires immediate attention today!"
        else: 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        # message = (f"Note: '{task}' is a medium priority task")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
    # message += " that requires immediate attention today!"
        else: 
            print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        # message = (f"Note: '{task}' is a low priority task")

# # time sensitivity
# if time_bound == "yes":
#     message += " that requires immediate attention today!"
# else:
#     message += ". Consider completing it when you have free time."

# Output 
# print(message)
