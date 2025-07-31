# src/visualizer.py

import matplotlib.pyplot as plt
import pandas as pd

def plot_expense_pie(transactions):
    """
    Plots a pie chart of expenses by category.
    Accepts: List of Transaction objects.
    """
    df = pd.DataFrame([t.to_dict() for t in transactions if t.trans_type == "Expense"])
    if df.empty:
        print("No expenses to plot.")
        return
    breakdown = df.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(7, 7))
    breakdown.plot.pie(autopct='%1.1f%%', startangle=140)
    plt.title("Expense Breakdown by Category")
    plt.ylabel("")  # Hide y-axis label for cleanliness
    plt.show()


def plot_monthly_trends(transactions):
    """
    Plots line charts of monthly income and expenses.
    Accepts: List of Transaction objects.
    """
    df = pd.DataFrame([t.to_dict() for t in transactions])
    if df.empty:
        print("No transactions to plot.")
        return
    df['Month'] = pd.to_datetime(df['Date']).dt.to_period('M').astype(str)
    income = df[df['Type'] == "Income"].groupby('Month')['Amount'].sum()
    expense = df[df['Type'] == "Expense"].groupby('Month')['Amount'].sum()

    months = sorted(set(income.index).union(expense.index))
    income = income.reindex(months, fill_value=0)
    expense = expense.reindex(months, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(months, income.values, marker='o', label="Income")
    plt.plot(months, expense.values, marker='o', label="Expense")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    plt.title("Monthly Income and Expenses")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_category_bar(transactions):
    """
    Plots a bar chart showing total expense per category.
    Accepts: List of Transaction objects.
    """
    df = pd.DataFrame([t.to_dict() for t in transactions if t.trans_type == "Expense"])
    if df.empty:
        print("No expenses to plot.")
        return
    cat_totals = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
    plt.figure(figsize=(10, 6))
    cat_totals.plot(kind='bar')
    plt.ylabel("Total Spent")
    plt.title("Expenses by Category")
    plt.tight_layout()
    plt.show()
