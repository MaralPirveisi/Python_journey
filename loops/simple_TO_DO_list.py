tasks = []

print("Welcome to your Task Manager")

while True:
    print("What would you like to do?")
    print("1.Add a task")
    print("2.Show all tasks")
    print("3.Exit")
    
    choice = input("Enter your choice (1/2/3):")
    
    if choice =='1':
        new_task = input("Enter the task:")
        tasks.append(new_task)
        print("Task added successfully!")
    
    elif choice =='2':
        print("Your Current Tasks:")
        if tasks == []:
            print("The list is empty.")
        else:
            for item in tasks:
                print("- " + item)
    
    elif choice =='3':
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please try again.")
