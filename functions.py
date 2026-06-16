import json

expenses = []  # This will hold the list of expenses with categories
expense = {} # This will hold the details of a single expense

def save_data():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)

def load_data():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
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
    if name.isdigit():
        print("Please enter a valid name!")
        input("\n↳ ")
        return
    amount = None
    try:
        amount = float(input(f"Enter expense amount: {currency}"))
    except ValueError:
        print("please enter a valid amount!")
        input("\n↳ ")
        return
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    if expenses:
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    else:
        print("Failed to add expense. Please try again.")
    

    cate_ques: str = input("Add Category? (y/n)").lower()
    if cate_ques == "y":
        category = input("Enter category name: ")
        category_lower = category.lower()
        expense = {"category": category_lower}
        if category_lower not in expense:
            expenses.append(category_lower)
        print(f"{name} is added to Category '{category}'")
    input("\n↳ ")
    

def show_expense(currency): # Prints the currently added expenses
    if not expenses:
            print("No expenses to show.")
    else:
        print("Expenses:")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense["name"]} - {currency}{expense["amount"]}")
    input("\n↳ ")

def delete_expense(currency): # Deletes the expenses according to the user's input
    if not expenses:
        print("No expenses to delete.")
    else:
        print("Expenses:")
        print("0. Back")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense["name"]} - {currency}{expense["amount"]}")
        delete_it = (input("Which Expense do you want to delete: "))
        if delete_it.isdigit() == False:
            print("Please enter a valid integer!")
            input("\n↳ ")
            return
        delete_it = int(delete_it) - 1
        if 0 <= delete_it and delete_it <= len(expenses)-1:
            deleted_item = expenses.pop(delete_it)
            print()
            print(f"Expense '{deleted_item["name"]}' of amount {currency}{deleted_item["amount"]} deleted successfully!")
        elif delete_it == 0:
            return
        else:
            print("Failed to delete Expense. Please try again.")
    input("\n↳ ")

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
    input("\n↳ ")

expenses = load_data()
