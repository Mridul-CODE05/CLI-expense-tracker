import json

expenses = []
expense = {}

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
    print("1. Add")
    print("2. View")
    print("3. Delete")
    print("4. Total")
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
    # expense = {"name": name, "amount": amount}
    expense["name"] = name
    expense["amount"] = amount
    if expenses:
        print(f"Expense '{name}' of amount {currency}{amount} added successfully!")
    else:
        print("Failed to add expense. Please try again.")
    

    cate_ques: str = input("Add Category? (y/n)").lower()
    if cate_ques == "y":
        category = input("Enter category name: ")
        category_lower = category.lower()
        expense["category"] = category
        print(f"{name} is added to Category '{category}'")
    expenses.append(expense)
    input("\n↳ ")
    

expenses = load_data()
