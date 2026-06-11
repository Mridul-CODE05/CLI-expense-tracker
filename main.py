while True:
    print("===== Expense Tracker =====")
    print()
    print("Please select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")
    print()
    choice = input("Enter your choice: ")
    print()

    if choice == '1':
        name = input("Enter expense name: ")
        currency = "₹"
        amount = float(input(f"Enter expense amount: {currency}"))
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        print()
        break
