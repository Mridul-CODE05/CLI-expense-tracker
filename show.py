from functions import *

def show_expense(currency): # Prints the currently added expenses
    if not expenses:
            print("No expenses to show.")
    else:
        print("Expenses:")
        for i, expense in enumerate(expenses, start=1):
            category = expense.get("category")
            if category:
                print(f"{i}. {expense["category"]}: {expense["name"]} - {currency}{expense["amount"]}")
            else:    
                print(f"{i}. {expense["name"]} - {currency}{expense["amount"]}")
    input("\n↳ ")
