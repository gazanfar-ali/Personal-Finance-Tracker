#main.py

import os
from src.models import TransactionManager
from src.sample_data import sample_transactions
from src.tracker import (
    add_transaction_ui,
    print_summary,
    print_all_transactions,
    delete_transaction_ui,
    filter_transactions_ui,
    print_category_breakdown,
    load_transactions,
    save_transactions,
)
from src.visualizer import plot_expense_pie, plot_monthly_trends, plot_category_bar

DATA_PATH = "data/transactions.csv"

def main():
    print("Welcome to Personal Finance Tracker!")

    # Load transactions from CSV if available; otherwise load sample data
    if os.path.exists(DATA_PATH):
        transactions = load_transactions(DATA_PATH)
        if not transactions:
            print("CSV found but empty or invalid, loading sample data.")
            transactions = sample_transactions.copy()
    else:
        print(f"{DATA_PATH} not found, loading sample data.")
        transactions = sample_transactions.copy()

    manager = TransactionManager(transactions)

    menu = """
--- Personal Finance Tracker Menu ---
1. Add Transaction
2. View All Transactions
3. View Summary (Income, Expense, Savings)
4. View Expense Breakdown by Category
5. Filter Transactions (Date/Category)
6. Delete a Transaction
7. Plot Expense Pie Chart
8. Plot Monthly Income/Expense Trends
9. Plot Expense by Category Bar Chart
10. Save & Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option (1-10): ").strip()

        if choice == "1":
            add_transaction_ui(manager)
        elif choice == "2":
            print_all_transactions(manager)
        elif choice == "3":
            print_summary(manager)
        elif choice == "4":
            print_category_breakdown(manager)
        elif choice == "5":
            filter_transactions_ui(manager)
        elif choice == "6":
            delete_transaction_ui(manager)
        elif choice == "7":
            plot_expense_pie(manager.transactions)
        elif choice == "8":
            plot_monthly_trends(manager.transactions)
        elif choice == "9":
            plot_category_bar(manager.transactions)
        elif choice == "10":
            save_transactions(manager.transactions, DATA_PATH)
            print("Transactions saved. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 10.")


if __name__ == "__main__":
    main()
