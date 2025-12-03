from transaction import Income, Expense
from datetime import datetime


class BudgetTracker:

    def __init__(self):
        self.transactions = []

    # Add Income
    def add_income(self):
        print("\n--- Add Income ---")

        date = input("Enter date (YYYY-MM-DD) or press Enter for today's date: ").strip()

        # If the user pressed Enter → fill with today's date
        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        # Loop until user enters a valid positive amount
        while True:
            amount_input = input("Enter amount: ").strip()

            try:
                amount = float(amount_input)
            except ValueError:
                print(" Invalid amount! Must be a number.")
                continue

            if amount <= 0:
                print(" Amount must be a positive number. Please try again.")
                continue

            break  # valid amount, exit loop

        category = input("Enter category: ").strip()
        if category == "":
            print(" Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        income = Income(date, amount, category, description)
        self.transactions.append(income)
        print("✔ Income added successfully!")

    # Add Expense
    def add_expense(self):
        print("\n--- Add Expense ---")

        date = input("Enter date (YYYY-MM-DD) or press Enter for today's date: ").strip()
        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        # Loop until user enters a valid positive amount
        while True:
            amount_input = input("Enter amount: ").strip()

            try:
                amount = float(amount_input)
            except ValueError:
                print(" Invalid amount! Must be a number.")
                continue

            if amount <= 0:
                print(" Amount must be a positive number. Please try again.")
                continue

            break  # valid amount

        category = input("Enter category: ").strip()
        if category == "":
            print(" Category cannot be empty.")
            return

        description = input("Enter description: ").strip()

        expense = Expense(date, amount, category, description)
        self.transactions.append(expense)
        print("✔ Expense added successfully!")


    # Listing All Transactions

    def list_transactions(self):
        print("\n--- All Transactions ---")
        if not self.transactions:
            print("No transactions recorded.")
            return
        for t in self.transactions:
            print(t)


    # Code that I use to Filter Transactions

    def filter_transactions(self):
        print("\n--- Filter Options ---")
        print("1. By Type (income/expense)")
        print("2. By Category")
        print("3. By Month (YYYY-MM)")
        choice = input("Choose filter: ")

        if choice == "1":
            ttype = input("Enter type (income/expense): ").lower()
            results = [t for t in self.transactions if t.type == ttype]

        elif choice == "2":
            cat = input("Enter category: ").lower()
            results = [t for t in self.transactions if t.category == cat]

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            results = [t for t in self.transactions if t.date.startswith(month)]

        else:
            print("Invalid filter option!")
            return

        if not results:
            print("No matching transactions.")
        else:
            print("\n--- Filter Results ---")
            for r in results:
                print(r)


    # Code for Summary Report

    def show_summary(self):
        def show_summary(self):
            print("\n--- Summary ---")

            total_income = sum(t.amount for t in self.transactions if t.type == "income")
            total_expense = sum(t.amount for t in self.transactions if t.type == "expense")
            balance = total_income - total_expense

            print(f"Total Income: {total_income}")
            print(f"Total Expense: {total_expense}")
            print(f"Balance: {balance}")

            print("\nPer-Category Totals:")
            category_totals = {}

            for t in self.transactions:
                if t.category not in category_totals:
                    category_totals[t.category] = 0
                category_totals[t.category] += t.amount

            # This loop must end BEFORE printing All Transactions, otherwise my code will duplicate some info
            for cat, amt in category_totals.items():
                print(f"{cat.title()}: {amt}")


            # Code for listing ALL transactions - as individuals :)

            print("\nAll Transactions:")
            for t in self.transactions:
                print(t)

