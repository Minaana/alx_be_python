task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time = input("Is it time-bound? (yes/no):")
match priority :
    case "high" :
        if time == "yes" :
            print(task, "is a High priority that requires immediate attention today!: ",)
        else :
            print(task, "is a High priority that requires immediate attention!: ",)
    case "low" :
        if time == "yes" :
            print(task, "is a Low priority that can be done later today!: ",)
        else    :
            print(task, "is a low priority task. Consider completing it when you have free time.: ",)