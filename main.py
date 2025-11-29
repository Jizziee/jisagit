from transaction import Income, Expense
from budget_tracker import Budget

def main():
    budget = Budget()

    # add test transactions
    t1 = Income("2025-03-01", 2000, "Salary", "March salary")
    t2 = Expense("2025-03-02", 150, "Food", "Groceries")

    budget.add_transaction(t1)
    budget.add_transaction(t2)

    print("All Transactions:")
    for t in budget.list_transactions():
        print(t)

    print("\nSummary:")
    income, expense, balance = budget.get_summary()
    print("Total Income:", income)
    print("Total Expense:", expense)
    print("Balance:", balance)

if __name__ == "__main__":
    main()

