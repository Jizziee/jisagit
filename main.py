
# Day 4
from budget_tracker import BudgetTracker

bt = BudgetTracker()

while True:
    print("\n--- Budget Tracker ---")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Summary")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bt.add_income()
    elif choice == "2":
        bt.add_expense()
    elif choice == "3":
        for t in bt.transactions:
            print(t)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

