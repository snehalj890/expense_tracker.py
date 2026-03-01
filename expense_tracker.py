import json
import os

# ----- Class Definitions -----
class Expense:
    """Represents a single expense item."""
    def __init__(self, item, amount, category):
        self.item = item
        self.amount = amount
        self.category = category

    def to_dict(self):
        """Convert expense to dictionary for JSON storage."""
        return {"item": self.item, "amount": self.amount, "category": self.category}

class ExpenseTracker:
    """Handles all expense tracking logic."""
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = self.load_expenses()

    # --- File Handling ---
    def load_expenses(self):
        """Load expenses from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Expense(**exp) for exp in data]
            except json.JSONDecodeError:
                print("Error reading JSON file, starting fresh.")
        return []

    def save_expenses(self):
        """Save expenses to JSON file."""
        with open(self.filename, "w") as file:
            json.dump([exp.to_dict() for exp in self.expenses], file, indent=4)

    # --- Core Functionality ---
    def add_expense(self):
        """Add a new expense."""
        try:
            item = input("Enter item name: ")
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            expense = Expense(item, amount, category)
            self.expenses.append(expense)
            self.save_expenses()
            print("✅ Expense added successfully!\n")
        except ValueError:
            print("❌ Invalid amount! Please enter a number.\n")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded yet.\n")
            return
        print("\n📊 Your Expenses:")
        for idx, exp in enumerate(self.expenses, start=1):
            print(f"{idx}. {exp.item} - ${exp.amount:.2f} ({exp.category})")
        print()

    def summary_by_category(self):
        """Show total spending per category."""
        summary = {}
        for exp in self.expenses:
            summary[exp.category] = summary.get(exp.category, 0) + exp.amount
        if not summary:
            print("No expenses to summarize.\n")
            return
        print("\n📈 Summary by Category:")
        for cat, total in summary.items():
            print(f"{cat}: ${total:.2f}")
        print()

# ----- Main Program -----
def main():
    tracker = ExpenseTracker()

    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summary by Category")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.summary_by_category()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()