# src/tracker.py

import pandas as pd
from .models import Transaction

def load_transactions(filepath):
    """
    Load transactions from a CSV file into a list of Transaction objects.
    If the file does not exist, returns an empty list.
    """
    transactions = []
    try:
        df = pd.read_csv(filepath)
        for _, row in df.iterrows():
            transactions.append(Transaction(
                row["Date"],
                row["Category"],
                row["Type"],
                row["Amount"],
                row["Description"]
            ))
    except FileNotFoundError:
        print(f"{filepath} not found, starting fresh!")
    return transactions


def save_transactions(transactions, filepath):
    """
    Save a list of Transaction objects to a CSV file.
    """
    df = pd.DataFrame([t.to_dict() for t in transactions])
    df.to_csv(filepath, index=False)


def add_transaction_ui(manager):
    """
    Command line interface for adding a single transaction.
    Transaction is added to the manager.
    """
    print("\nAdd New Transaction:")
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip()
    trans_type = input("Type (Income/Expense): ").strip().capitalize()
    # Validate transaction type
    while trans_type not in ("Income", "Expense"):
        print("Invalid Type! Enter 'Income' or 'Expense'")
        trans_type = input("Type (Income/Expense): ").strip().capitalize()

    try:
        amount = float(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount! Transaction not added.")
        return
    
    description = input("Description: ").strip()

    try:
        transaction = Transaction(date, category, trans_type, amount, description)
        manager.add_transaction(transaction)
        print("Transaction added successfully!")
    except Exception as e:
        print(f"Failed to add transaction: {e}")


def print_summary(manager):
    """
    Print a summary of total income, expenses, and savings.
    """
    summary = manager.summary()
    print("\nSummary:")
    for key, value in summary.items():
        print(f"{key}: {value:.2f}")


def print_category_breakdown(manager):
    """
    Print expense breakdown by category.
    """
    breakdown = manager.category_breakdown()
    print("\nExpense Breakdown by Category:")
    if not breakdown:
        print("No expenses recorded.")
    else:
        for category, total in breakdown.items():
            print(f"{category}: {total:.2f}")


def print_all_transactions(manager):
    """
    Print all transactions with their index, to allow reference or deletion.
    """
    if not manager.transactions:
        print("\nNo transactions available.")
        return

    print("\nAll Transactions:")
    print("-" * 70)
    print(f"{'Index':<5} {'Date':<12} {'Category':<15} {'Type':<10} {'Amount':<10} Description")
    print("-" * 70)
    for idx, t in enumerate(manager.transactions):
        print(f"{idx:<5} {t.date} {t.category:<15} {t.trans_type:<10} {t.amount:<10.2f} {t.description}")
    print("-" * 70)


def delete_transaction_ui(manager):
    """
    Command line interface for deleting a transaction by index.
    """
    print_all_transactions(manager)
    try:
        idx_str = input("Enter the index of transaction to delete: ").strip()
        idx = int(idx_str)
        manager.delete_transaction(idx)
        print("Transaction deleted successfully.")
    except ValueError:
        print("Invalid input: not an integer.")
    except IndexError as e:
        print(f"Error: {e}")


def filter_transactions_ui(manager):
    """
    Filter transactions by date range or category and print matching transactions.
    """
    print("\nFilter Transactions")
    filter_type = input("Filter by (date/category): ").strip().lower()

    if filter_type == "date":
        start_date = input("Start Date (YYYY-MM-DD) or leave blank: ").strip()
        end_date = input("End Date (YYYY-MM-DD) or leave blank: ").strip()

        def filter_func(t):
            if start_date:
                try:
                    d_start = pd.to_datetime(start_date).date()
                    if t.date < d_start:
                        return False
                except Exception:
                    print("Invalid start date format.")
                    return False
            if end_date:
                try:
                    d_end = pd.to_datetime(end_date).date()
                    if t.date > d_end:
                        return False
                except Exception:
                    print("Invalid end date format.")
                    return False
            return True

    elif filter_type == "category":
        category = input("Enter category to filter by: ").strip().lower()
        def filter_func(t):
            return t.category.lower() == category

    else:
        print("Invalid filter type. Showing all transactions.")
        filter_func = None

    filtered = manager.get_all(filter_func)
    if not filtered:
        print("No transactions found for the given filter.")
        return

    print("\nFiltered Transactions:")
    print("-" * 70)
    print(f"{'Date':<12} {'Category':<15} {'Type':<10} {'Amount':<10} Description")
    print("-" * 70)
    for t in filtered:
        print(f"{t.date} {t.category:<15} {t.trans_type:<10} {t.amount:<10.2f} {t.description}")
    print("-" * 70)
