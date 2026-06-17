from functions import *

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