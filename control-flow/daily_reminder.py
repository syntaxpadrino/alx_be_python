task = input("Enter your task: ")
priority = input("Enter the priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "hight":
        if time_bound == "yes":
            print(f"Task '{task}' is a high priority and time-bound. Schedule it immediately.")
        else:
            print(f"Task '{task}' is a high priority but not time-bound. Schedule it soon.")
    case "medium":
        if time_bound == "yes":
            print(f"Task '{task}' is a medium priority and time-bound. Schedule it within the week.")
        else:
            print(f"Task '{task}' is a medium priority but not time-bound. Schedule it when possible.")
    case "low":
        if time_bound == "yes":
            print(f"Task '{task}' is a low priority and time-bound. Schedule it when convenient.")
        else:
            print(f"Task '{task}' is a low priority and not time-bound. You can do it later.")
    case _:
        print("Invalid priority level. Please enter 'high', 'medium', or 'low'.")
