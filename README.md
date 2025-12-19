# Budget Tracker

> A simple command-line interface (CLI) application to track personal expenses, manage a budget, and calculate total costs.

## 📖 Description
This project is a Python-based Budget Tracker that allows users to record their daily expenses. It uses Object-Oriented Programming (OOP) to manage data and stores all records persistently in a JSON file (`budget.json`). It also includes a unique feature to "pay off" balances, creating a ledger of expenses vs. payments.

## 🌟 Key Features
* **Add Expenses:** Input item name, price, and category (e.g., Food, Rent, Fun).
* **View History:** Display a list of all recorded expenses.
* **Calculate Totals:** Automatically sums up all expenses to show your current debt/spending.
* **Pay Off Balance:** Allows users to pay the "Total" or a "Custom" amount. This adds a negative entry to the ledger to reduce the total balance.
* **Data Persistence:** Automatically saves and loads data using `budget.json`.
* **Unit Testing:** Includes automated tests to verify the logic works correctly.

## 🛠️ Technologies Used
* **Python 3**
* **JSON:** For data storage.
* **Unittest:** For code testing and validation.

## 📂 Project Structure
* `main.py`: The user interface and menu loop.
* `manager.py`: Handles the logic (adding, calculating totals, saving/loading).
* `expense.py`: Defines the `Expense` class structure.
* `test_manager.py`: Contains unit tests to ensure the code works as expected.
* `budget.json`: The database file where expenses are stored.

## 🚀 How to Run
To use the Budget Tracker, follow these steps:

1. **Clone or Download** the project files.
2. **Open your terminal** and navigate to the project folder.
3. **Run the application**:
   ```bash
   python main.py
