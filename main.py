from functions import print_menu, add_expense, show_expense, delete_expense, total_spending, save_data, load_data

expenses = []  # This will hold the list of expenses
expense = {} # This will hold the details of a single expense

while True: # Runs infinitely until exited by the user
    print_menu()
    currency: str = "₹"
    choice = (input("Enter your choice: "))
    if choice.isdigit() == False:
        print("Please enter a valid integer!")
        input("\n↳ ")
        continue
    print()

    if choice == '1':
        add_expense(currency)
        save_data()

    elif choice == '2':
        show_expense(currency)
    
    elif choice == '3':
        delete_expense(currency)
        save_data()
    
    elif choice == '4':
        total_spending(currency)

    elif choice == '5':
        print("Exiting the Expense Tracker. Goodbye!")
        print()
        save_data()
        break

    else:
        print("Please enter a valid menu number!")
        input("\n↳ ")
        continue

    save_data()
