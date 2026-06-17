from functions import *

def delete_expense(currency): # Deletes the expenses according to the user's input
    if not expenses:
        print("No expenses to delete.")
    else:
        print("Expenses:")
        print("0. Back")
        for i, exp_ense in enumerate(expenses, start=1):
            print(f"{i}. {exp_ense["name"]} - {currency}{exp_ense["amount"]}")
        delete_it = (input("Which Expense do you want to delete: "))
        if delete_it.isdigit() == False:
            print("Please enter a valid integer!")
            input("\n↳ ")
            return
        if delete_it == 0:
            return
        delete_it = int(delete_it) - 1
        if 0 <= delete_it and delete_it <= len(expenses)-1:
            deleted_item = expenses.pop(delete_it)
            print()
            print(f"Expense '{deleted_item["name"]}' of amount {currency}{deleted_item["amount"]} deleted successfully!")
        else:
            print("Failed to delete Expense. Please try again.")
    input("\n↳ ")

def delete_category():
    for i, expen in enumerate(expenses, start=1):
        cate = expen.get("category")
        category = []
        category.append(cate)
        if not cate:
            print("No categories to delete.")
        else:
            print("Categories: ")
            print("0. Back")
            for i, exp_ense in enumerate(expenses, start=1):
                print(f"{i}. {exp_ense["category"]}")
            delete = input("Which Category do you want to delete: ")
            if delete.isdigit() == False:
                print("Please enter a valid integer!")
                input("\n↳ ")
                return
            if delete == 0:
                return
            delete = int(delete) - 1
            if 0 <= delete and delete <= len(category) - 1:
                deleted_category = category.pop(delete)
                print()
                print(f"Category '{deleted_category["category"]}' deleted successfully!")
            else:
                print("Failed to delete Category. Please try again.")
    input("\n↳ ")