from functions import *

def show_expense(currency): # Prints the currently added expenses
    if not expenses:
            print("No expenses to show.")
    else:
        print("All Expenses:")
        for i, expense in enumerate(expenses, start=1):
            category = expense.get("category")
            if category:
                print(f"{i}. {expense["category"]}: {expense["name"]} - {currency}{expense["amount"]}")
            else:    
                print(f"{i}. {expense["name"]} - {currency}{expense["amount"]}")
    input("\n↳ ")

def show_category():
    for i, expen in enumerate(expenses, start=1):
        category = expen.get("category")
        if not category:
            print("No categories to show.")
        else:
            print("All Categories: ")
            print(f"{i}. {expen["category"]}" )
    input("\n↳ ")

def show():
    print("1. Expense")
    print("2. Category")
    print()
    choice = input("Enter your choice: ")
    print()
    if choice.isdigit() == False:
        print("Please enter a valid integer!")
        input("\n↳ ")
        return
    else:
        if choice == '1':
            show_expense(currency='₹')
        elif choice == '2':
            show_category()
        else:
            print("Please enter a valid integer!")
            input("\n↳ ")
            return
