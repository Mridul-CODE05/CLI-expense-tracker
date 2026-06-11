expenses: list[dict[str, str, float]] = []  # This will hold the list of expenses
expense: dict[str, str, float] = {} # This will hold the details of a single expense

def print_status():
    print("===== Expense Tracker =====")
    print()
    print("Please select an option:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Total Spending")
    print("5. Exit")
    print()

def add_expense(currency):
    name: str = input("Enter expense name: ")
    amount = float(input(f"Enter expense amount: {currency}"))
    expense = {"name": name, "currency": currency, "amount": amount}
    expenses.append(expense)
    if expenses:
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    else:
        print("Failed to add expense. Please try again.")

def show_expense():
    if not expenses:
            print("No expenses to show.")
    else:
        print("Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense["name"]} - {expense["currency"]}{expense["amount"]}")

def delete_expense():
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
            print(f"Expense '{deleted_item["name"]}' of amount {deleted_item["currency"]}{deleted_item["amount"]} deleted successfully!")
        elif delete_it == 0:
            return
        else:
            print("Failed to delete Expense. Please try again.")

def total_spending(currency):
    total = 0
    for a in expenses:
        total += a["amount"]
    if a["amount"] != 0:
        print("Calculating Total Spending: ")
        print(f"Successfully calculated Total Spending!")
        print(f"--> {currency}{total}")
    else:
        print("No expenses to total.")

while True:
    print_status()
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
