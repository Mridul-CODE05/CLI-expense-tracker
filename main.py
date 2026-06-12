expenses: list[dict[str, str, float]] = []  # This will hold the list of expenses
expense: dict[str, str, float] = {} # This will hold the details of a single expense

def print_menu(): # Prints the menu at the start
    print("===== Expense Tracker =====")
    print()
    print("Please select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")
    print()

def add_expense(currency): # Adds the inputted expense into a list
    name: str = input("Enter expense name: ")
    amount = float(input(f"Enter expense amount: {currency}"))
    expense = {"name": name, "currency": currency, "amount": amount}
    expenses.append(expense)
    if expenses:
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    else:
        print("Failed to add expense. Please try again.")
    input("\nPress Enter to return to the menu...")

def show_expense(): # Prints the currently added expenses
    if not expenses:
            print("No expenses to show.")
    else:
        print("Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense["name"]} - {expense["currency"]}{expense["amount"]}")
    input("\nPress Enter to return to the menu...")

def delete_expense(): # Deletes the expenses according to the user's input
    if not expenses:
        print("No expenses to delete.")
    else:
        print("Expenses:")
        print("0. Back")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense["name"]} - {expense["currency"]}{expense["amount"]}")
        delete_it = int(input("Which Expense do you want to delete: ")) - 1
        if 0 <= delete_it and delete_it <= len(expenses)-1:
            deleted_item = expenses.pop(delete_it)
            print()
            print(f"Expense '{deleted_item["name"]}' of amount {deleted_item["currency"]}{deleted_item["amount"]} deleted successfully!")
        elif delete_it == 0:
            return
        else:
            print("Failed to delete Expense. Please try again.")
    input("\nPress Enter to return to the menu...")

def total_spending(currency): # Prints the total amount
    total = 0.0
    for a in expenses:
        total += a["amount"]
    if expenses:
        print("Calculating Total Spending: ")
        print(f"Successfully calculated Total Spending!")
        print(f"--> {currency}{total}")
    else:
        print("No expenses to total.")
    input("\nPress Enter to return to the menu...")

while True: # Runs infinitely until exited by the user
    print_menu()
    currency: str = "₹"
    choice = int(input("Enter your choice: "))
    print()

    if choice == 1:
        add_expense(currency)

    elif choice == 2:
        show_expense()
    
    elif choice == 3:
        delete_expense()
    
    elif choice == 4:
        total_spending(currency)

    elif choice == 5:
        print("Exiting the Expense Tracker. Goodbye!")
        print()
        break
