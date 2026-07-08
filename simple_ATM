first_balance = 1000
options = [
    "Check balance",
    "Deposit",
    "Withdraw",
    "Exit"
]
while True:
    print(options[0])
    print(options[1])
    print(options[2])
    print(options[3])
    choice = input("please enter your choice: ")
    if choice == "Check balance":
        print(f"Your balance is {first_balance}")
    elif choice == "Deposit":
        amount = int(input("Enter deposit amount: "))
        first_balance += amount
        print(f"Your balance is {first_balance}")
    elif choice == "Withdraw":
        amount = int(input("Enter withdraw amount: "))
        if amount <= first_balance:
            first_balance -= amount
            print(f"Your balance is {first_balance}")
        else:
            print("Not enough balance")
    elif choice == "Exit":
        print("Goodbye")
        break
    else:
        print("Invalid choice")
