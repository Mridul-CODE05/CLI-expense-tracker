
# 📌CLI Expense Tracker

A command-line expense tracker built as a Personal learning project to explore Python, JSON persistence, input validation, Git, GitHub, and software design principles.

## ✨Features

- Add expenses
- View all expenses
- Delete expenses
- Calculate total spending
- Input validation and error handling
- JSON-based data persistence



## ⚙️ Requirements
```md
Python 3.14+
```
## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/Mridul-CODE05/CLI-expense-tracker
```

### 2. Navigate into the project directory
```bash
cd CLI-expense-tracker
```


## 🚀Usage/Examples

Run the program
```bash
python3 main.py
```

You will see the main menu:
```
===== Expense Tracker =====

Please select an option:
1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Spending
5. Exit

Enter your choice:
```

### 1. Add Expense
Enter the expense name and amount:
```
Enter your choice: 1

Enter expense name: Food
Enter expense amount: ₹250
Expense 'Food' of amount ₹250.0 added successfully!
```

### If an invalid amount is entered:
```
Enter expense amount: ₹dfdf
please enter a valid amount!
```

### 2. View Expenses
Displays all saved expenses:
```
Enter your choice: 2

Expenses:
1. Food - ₹250.0
2. Gym - ₹1000.0
```

### 3. Delete Expense
Show a numbered list of all expenses:
```
Enter your choice: 3

Expenses:
0. Back
1. Food - ₹250.0
2. Gym - ₹1000.0
```
Enter the number to delete:
```
Which Expense do you want to delete: 2

Expense 'Gym' of amount ₹1000.0 deleted successfully!
```

### 4. Total spending
Display the total of all added expenses:
```
Enter your choice: 4

Calculating Total Spending: 
Successfully calculated Total Spending!
--> ₹250.0
```

### 5. Exiting the program
```
Enter your choice: 5

Exiting the Expense Tracker. Goodbye!
```

## 🗂Project Structure

```text
CLI-expense-tracker/
├── main.py
├── functions.py
├── expenses.json
├── .gitignore
└── README.md
```
## 💾Data Storage
All expenses are stored locally in a JSON file (expenses.json) so your data persists between runs.
## 🧠Lessons Learned

- Proper defining of variables
- Calling the Functions at the right place
- Modular code organization
- JSON serialization and file handling
- Input validation and exception handling
- Git and GitHub workflows
- Refactoring and debugging techniques


## 🛠Roadmap

- Expense categories
- Search expenses
- Edit existing expenses
- Budget tracking
- Monthly reports
- Expense statistics
- Add charts for spending analysis
- Better CLI formatting (colors, tables)
- Database support instead of JSON
