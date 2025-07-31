# Personal Finance Tracker

A simple and practical CLI Python application to help you track your income, expenses, and savings, and visualize your financial data with charts.

---

## Features

- Add, view, delete, and filter transactions (income and expenses)
- Summary of total income, expenses, and savings
- Expense breakdown by category
- Visualize data with:
  - Pie chart of expenses by category
  - Line graph showing monthly income and expenses
  - Bar chart of expenses by category
- Data persisted in CSV format for easy import/export
- Preloaded with 100 sample transactions covering multiple categories and months

---

## Project Structure
``` bash
personal_finance_tracker/
│
├── data/
│ └── transactions.csv # Stores income/expense data (CSV)
│
├── src/
│ ├── init.py # (Optional, package marker)
│ ├── models.py # Classes: Transaction, TransactionManager
│ ├── sample_data.py # 100 sample transactions for testing
│ ├── tracker.py # CLI functions: add/view/delete/filter
│ └── visualizer.py # Matplotlib chart functions
│
├── main.py # Entry point: CLI menu & interaction
├── requirements.txt # Python libraries needed
└── README.md # This documentation
```
---

## Getting Started

### Prerequisites
```bash
- Python 3.8 or higher installed on your system
- Pip package manager (usually comes with Python)
```

### Installation
```bash
1. Clone or download this repository.
2. (Optional but recommended) Create a Python virtual environment and activate it:
3. Install required Python libraries:
```

## Usage & CLI Menu

Once running, you'll see a menu with these options:

1. **Add Transaction** 
   Enter date, category, type (Income/Expense), amount and description.

2. **View All Transactions**  
   See a detailed list of all transactions with index numbers.

3. **View Summary**  
   Shows total income, expenses, and net savings.

4. **View Expense Breakdown by Category**  
   Shows how much you spent in each expense category.

5. **Filter Transactions (Date/Category)**  
   Search transactions by a date range or specific category.

6. **Delete a Transaction**  
   Remove a transaction by its index.

7. **Plot Expense Pie Chart**  
   Displays a pie chart of your expenses broken down by category.

8. **Plot Monthly Income/Expense Trends**  
   Shows a line chart of income and expenses over months.

9. **Plot Expense by Category Bar Chart**  
   Shows a bar chart visualizing total expenses per category.

10. **Save & Exit**  
   Saves all transactions into `data/transactions.csv` and quits.

---

## Data Persistence

- Your transactions are saved in `data/transactions.csv`.
- On startup, the app loads this CSV; if it's missing or empty, the app loads 100 sample transactions from `src/sample_data.py`.
- Be sure to save before exiting to persist any new or modified data.

---

## Requirements

| Package    | Minimum Version | Purpose                                   |
|------------|-----------------|-------------------------------------------|
| pandas     | 1.1.0           | Data manipulation and CSV handling        |
| matplotlib | 3.3.0           | Plotting and visualizing finance charts   |

*Explanation:*
These libraries enable data handling and chart plotting. Install them with:


## Who Is This For?

- Beginner to intermediate Python users who want a real-world project to learn from.
- Individuals wanting a lightweight tool to track personal finances via CLI.
- Developers looking to build on the project by adding GUI, reports, authentication, or more.

---

## How It Works: Overview of Code Components

- **`src/models.py`**: Defines `Transaction` and `TransactionManager` classes for managing transaction data.
- **`src/sample_data.py`**: Contains 100 predefined sample transactions for testing/demo.
- **`src/tracker.py`**: Functions for user interaction like adding, deleting, filtering, and printing transactions.
- **`src/visualizer.py`**: Functions using matplotlib for generating charts to visualize financial data.
- **`main.py`**: Ties everything together with a menu-driven CLI loop.

---

## Future Enhancements

- GUI using Tkinter, PyQt, or another framework.
- User authentication & multi-user support.
- Budget limits, alerts, and notifications.
- Monthly or yearly financial reports generation (PDF or CSV).
- Integration with bank APIs for automatic transaction imports.

---

## Contributions

Feel free to fork, improve, and submit pull requests. Any feedback, feature requests, or bug reports are welcome!

---

## License

## License

This project is under a **Custom Viewing & Learning License** by GAZANFAR ALI.  
**NO COPYING:** You may only view the code for educational purposes; you must NOT copy, use, modify, or distribute it.  
To request permission for any other use, contact GAZANFAR ALI at [itsgazanfar@gmail.com](mailto:itsgazanfar@gmail.com) or LinkedIn: https://www.linkedin.com/in/gazanfar-ali.

---

## Contact
• Gmail : itsgazanfar@gmail.com

• LinkedIn : https://www.linkedin.com/in/gazanfar-ali


---

Happy budgeting and coding! 🚀

