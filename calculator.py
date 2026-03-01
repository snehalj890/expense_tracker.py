import json
import os

class Calculator:
    def __init__(self, filename="history.json"):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_history(self):
        with open(self.filename, "w") as file:
            json.dump(self.history, file, indent=4)

    def calculate(self, a, b, operation):
        if operation == "1":
            result = a + b
        elif operation == "2":
            result = a - b
        elif operation == "3":
            result = a * b
        elif operation == "4":
            if b != 0:
                result = a / b
            else:
                print("Cannot divide by zero.")
                return None
        else:
            print("Invalid operation.")
            return None
        self.history.append(f"{a} {operation} {b} = {result}")
        self.save_history()
        return result

    def view_history(self):
        if not self.history:
            print("No calculations yet.")
            return
        print("\n📜 Calculation History:")
        for h in self.history:
            print(h)

def main():
    calc = Calculator()
    while True:
        print("\n=== Simple Calculator ===")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. View History")
        print("6. Exit")
        choice = input("Choose: ")
        if choice in ["1","2","3","4"]:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                res = calc.calculate(a, b, choice)
                if res is not None:
                    print("Result:", res)
            except ValueError:
                print("Enter valid numbers.")
        elif choice == "5":
            calc.view_history()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()