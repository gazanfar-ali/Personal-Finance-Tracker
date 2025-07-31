import datetime

class Transaction:
    def __init__(self, date, category, trans_type, amount, description):
        # Accepts date as string 'YYYY-MM-DD' or as a datetime.date object
        if isinstance(date, str):
            self.date = datetime.datetime.strptime(date, "%Y-%m-%d").date()
        else:
            self.date = date
        self.category = category
        self.trans_type = trans_type  # "Income" or "Expense"
        self.amount = float(amount)
        self.description = description

    def to_dict(self):
        """
        Helper method to convert Transaction to a dictionary (for pandas, CSV, etc.)
        """
        return {
            "Date": self.date.strftime("%Y-%m-%d"),
            "Category": self.category,
            "Type": self.trans_type,
            "Amount": self.amount,
            "Description": self.description,
        }

    def __repr__(self):
        return (f"Transaction(date={self.date}, category='{self.category}', "
                f"type='{self.trans_type}', amount={self.amount}, description='{self.description}')")


class TransactionManager:
    def __init__(self, transactions=None):
        self.transactions = transactions if transactions is not None else []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def delete_transaction(self, idx):
        if 0 <= idx < len(self.transactions):
            del self.transactions[idx]
        else:
            raise IndexError("Transaction index out of range.")

    def get_all(self, filt=None):
        """
        Returns all transactions. 
        Optionally filtered by a function: filt(transaction) -> bool
        """
        if filt is None:
            return list(self.transactions)
        return list(filter(filt, self.transactions))

    def summary(self):
        total_income = sum(t.amount for t in self.transactions if t.trans_type == "Income")
        total_expense = sum(t.amount for t in self.transactions if t.trans_type == "Expense")
        savings = total_income - total_expense
        return {
            "Total Income": total_income,
            "Total Expense": total_expense,
            "Savings": savings,
        }

    def category_breakdown(self):
        """
        Returns a dictionary with {category: total_expenses_in_category}
        Counts only expenses.
        """
        breakdown = {}
        for t in self.transactions:
            if t.trans_type == "Expense":
                breakdown[t.category] = breakdown.get(t.category, 0) + t.amount
        return breakdown
