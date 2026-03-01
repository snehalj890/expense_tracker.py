import json
import os

class BMIRecord:
    def __init__(self, name, height, weight, bmi):
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi

    def to_dict(self):
        return {"name": self.name, "height": self.height, "weight": self.weight, "bmi": self.bmi}

class BMICalculator:
    def __init__(self, filename="bmi_history.json"):
        self.filename = filename
        self.records = self.load_history()

    def load_history(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [BMIRecord(**r) for r in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_history(self):
        with open(self.filename, "w") as file:
            json.dump([r.to_dict() for r in self.records], file, indent=4)

    def calculate_bmi(self):
        try:
            name = input("Name: ")
            height = float(input("Height (m): "))
            weight = float(input("Weight (kg): "))
            bmi = round(weight / (height**2), 2)
            self.records.append(BMIRecord(name, height, weight, bmi))
            self.save_history()
            print(f"{name}, your BMI is {bmi}")
        except ValueError:
            print("Invalid input.")

    def view_history(self):
        if not self.records:
            print("No records yet.")
            return
        print("\n📊 BMI History:")
        for r in self.records:
            print(f"{r.name}: BMI={r.bmi} (Height={r.height}m, Weight={r.weight}kg)")

def main():
    calc = BMICalculator()
    while True:
        print("\n=== BMI Calculator ===")
        print("1. Calculate BMI")
        print("2. View History")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            calc.calculate_bmi()
        elif choice == "2":
            calc.view_history()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()