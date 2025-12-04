

# Budget Tracker - Programming 1 Formative Project

This project is a simple command-line budget tracker written in Python.
It allows a user to record income and expenses, view all transactions, filter them, and see a financial summary.

It is built using Python and Object Oriented Programming(OOP).

## 1. Project Overview

The goal of this project is to help users track how they spend and earn money.
The program runs in the terminal and lets the user enter the date, amount, category, and a small description for every transaction.

I followed a day-by-day plan to build the project gradually (classes first, features later, then menu and documentation).

## 2. Features

#### Add income 
- User enters date, amount, category, description

- Press Enter to auto-fill today’s date

- Amount must be a positive number

#### Add expenses
- User enters date, amount, category, description

- Press Enter to auto-fill today’s date

- Amount must be a positive number

#### View all transactions
- Displays each transaction with type, date, category, amount, and description

#### Filter transactions
- By type (income/expense)

- By category

- By month (YYYY-MM)

#### View summary
- Total income

- Total expenses

- Balance

- Per-category totals

- All transactions listed again

#### Delete a transaction
- Transaction list shown with numbers

- nUser chooses a number to delete

- Validates incorrect inputs and out-of-range numbers

#### Input Validation

- Prevents negative amounts

- Forces numeric values

- Category cannot be empty

## 3. How to Run the Program

- Open the project folder in PyCharm.

- Make sure all files are in the same directory:main.py, budget_tracker.py, transaction.py

Run the program using: python main.py or press Run inside PyCharm.

## 4. Menu Structure

After running the program, you get the following menu:

                        === Budget Tracker Menu ===
        1. Add Income
        2. Add Expense
        3. List Transactions
        4. Filter Transactions
        5. Show Summary
        6. Delete a Transaction
        0. Exit



Each option requests the necessary inputs and then displays results in the terminal.

## 5. Sample Interaction

Example of adding income:

    --- Add Income ---
    Enter date (YYYY-MM-DD) or press Enter for today's date:
    Enter amount: -20
    Amount must be a positive number. Please try again.
    Enter amount: 500
    Enter category: salary
    Enter description: December payment
    ✔ Income added successfully!

Example of Listing Transactions:

     --- All Transactions ---
     [Income] 2025-12-04 | salary | 500 | November payment

Example of Filtering by month:

     --- Filter Options ---
     1. By Type (income/expense)
     2. By Category
     3. By Month (YYYY-MM)
     Choose filter: 3
    Enter month (YYYY-MM): 2025-12

    --- Filter Results ---
    [Income] 2025-12-04 | salary | 500 | November payment



Example of the summary:

    T--- Summary ---
    Total Income: 500.0
    Total Expense: 0.0
    Balance: 500.0

    Per-Category Totals:
    salary: 500.0

    All Transactions:
    [Income] 2025-12-04 | salary | 500 | November payment
    
Example of deleting a transaction:
 
     --- Delete a Transaction ---

    1. 2025-12-04 - salary - 500.0 - November payment

    Enter the number of the transaction to delete: 1
    ✔ Deleted: salary - 500.0 on 2025-12-04


## 6. Folder Structure

     BudgetTracker/
                 │
                 ├── main.py
                 ├── budget_tracker.py
                 ├── transaction.py
                 ├── README.md
                 ├── reflection.txt
                 └── repository_link.txt


## 7. Project Status 
All core features have been implemented successfully, and the project is fully functional in the terminal.