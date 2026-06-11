expenses = []  # This will hold the list of expenses
expense = {} # This will hold the details of a single expense

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
        expense = {"name": name, "currency": currency, "amount": amount}
        expenses.append(expense)
        if expenses:
            print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
        else:
            print("Failed to add expense. Please try again.")
    elif choice == '2':
        if not expenses:
            print("No expenses to show.")
        else:
            print("Expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense["name"]} - {expense["currency"]}{expense["amount"]}")
    

    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        print()
        break
