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


    expenses = []  # This will hold the list of expenses
    expense = {} # This will hold the details of a single expense
    if choice == '1':
        name = input("Enter expense name: ")
        currency = "₹"
        amount = float(input(f"Enter expense amount: {currency}"))
        expense = {"name": name, "currency": currency, "amount": amount}
        expenses.append(expense)
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        print()
        break
