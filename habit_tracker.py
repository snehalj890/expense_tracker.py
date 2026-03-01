import json
import os

class Habit:
    def __init__(self, name, done=False):
        self.name = name
        self.done = done

    def to_dict(self):
        return {"name": self.name, "done": self.done}

class HabitTracker:
    def __init__(self, filename="habits.json"):
        self.filename = filename
        self.habits = self.load_habits()

    def load_habits(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Habit(**h) for h in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_habits(self):
        with open(self.filename, "w") as file:
            json.dump([h.to_dict() for h in self.habits], file, indent=4)

    def add_habit(self):
        name = input("Enter habit name: ")
        self.habits.append(Habit(name))
        self.save_habits()
        print("✅ Habit added!\n")

    def mark_done(self):
        if not self.habits:
            print("No habits yet.")
            return
        for idx, h in enumerate(self.habits, start=1):
            status = "✅" if h.done else "❌"
            print(f"{idx}. [{status}] {h.name}")
        try:
            choice = int(input("Enter habit number to mark done: "))
            if 1 <= choice <= len(self.habits):
                self.habits[choice-1].done = True
                self.save_habits()
                print("🎉 Habit marked done!\n")
            else:
                print("Invalid number.")
        except ValueError:
            print("Enter a valid number.")

    def view_habits(self):
        if not self.habits:
            print("No habits yet.")
            return
        for idx, h in enumerate(self.habits, start=1):
            status = "✅" if h.done else "❌"
            print(f"{idx}. [{status}] {h.name}")

def main():
    tracker = HabitTracker()
    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit Done")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            tracker.add_habit()
        elif choice == "2":
            tracker.mark_done()
        elif choice == "3":
            tracker.view_habits()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()