# src/sample_data.py
from .models import Transaction

sample_transactions = [
    Transaction("2025-01-03", "Salary", "Income", 30000, "Monthly Salary"),
    Transaction("2025-01-04", "Rent", "Expense", 9000, "January Rent"),
    # ... other entries
]
