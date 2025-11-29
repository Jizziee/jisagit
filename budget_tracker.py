class BudgetTracker:

    def __init__(self):
        self.transactions = []

    def add_income(self):
        pass

    def add_expense(self):
        pass

    def list_transactions(self):
        pass

    def filter_transactions(self):
        pass

    def show_summary(self):
        pass

#DAY 3
from transaction import Transaction, Income, Expense

class Budget:
    def __init__(self):
        self.transactions = []  # list that stores all Income and Expense objects

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def list_transactions(self):
        return self.transactions

    def get_summary(self):
        total_income = 0
        total_expense = 0

        for t in self.transactions:
            if isinstance(t, Income):
                total_income += t.amount
            elif isinstance(t, Expense):
                total_expense += t.amount

        balance = total_income - total_expense

        return total_income, total_expense, balance



