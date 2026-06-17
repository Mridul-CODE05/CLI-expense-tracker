from functions import *

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
