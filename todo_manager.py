import json
import os

# ----- Class Definitions -----
class Task:
    """Represents a single task."""
    def __init__(self, title, status="Pending"):
        self.title = title
        self.status = status  # Pending or Done

    def to_dict(self):
        """Convert task to dictionary for JSON storage."""
        return {"title": self.title, "status": self.status}

class ToDoList:
    """Handles all to-do list logic."""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # --- File Handling ---
    def load_tasks(self):
        """Load tasks from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Task(**task) for task in data]
            except json.JSONDecodeError:
                print("Error reading JSON file, starting fresh.")
        return []

    def save_tasks(self):
        """Save tasks to JSON file."""
        with open(self.filename, "w") as file:
            json.dump([task.to_dict() for task in self.tasks], file, indent=4)

    # --- Core Functionality ---
    def add_task(self):
        """Add a new task."""
        title = input("Enter task title: ")
        task = Task(title)
        self.tasks.append(task)
        self.save_tasks()
        print("✅ Task added successfully!\n")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks yet.\n")
            return
        print("\n📋 To-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status_symbol = "✅" if task.status == "Done" else "❌"
            print(f"{idx}. [{status_symbol}] {task.title}")
        print()

    def mark_done(self):
        """Mark a task as completed."""
        self.view_tasks()
        try:
            task_no = int(input("Enter task number to mark as done: "))
            if 1 <= task_no <= len(self.tasks):
                self.tasks[task_no - 1].status = "Done"
                self.save_tasks()
                print("🎉 Task marked as done!\n")
            else:
                print("❌ Invalid task number.\n")
        except ValueError:
            print("❌ Please enter a valid number.\n")

# ----- Main Program -----
def main():
    todo = ToDoList()

    while True:
        print("=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            todo.add_task()
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.mark_done()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()