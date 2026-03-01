import json
import os

class Conversion:
    def __init__(self, from_currency, to_currency, amount, result):
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.amount = amount
        self.result = result

    def to_dict(self):
        return {"from_currency": self.from_currency, "to_currency": self.to_currency, "amount": self.amount, "result": self.result}

class CurrencyConverter:
    rates = {
        "USD": 1,
        "INR": 82,
        "EUR": 0.91,
        "GBP": 0.79
    }

    def __init__(self, filename="conversion_history.json"):
        self.filename = filename
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Conversion(**c) for c in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_history(self):
        with open(self.filename, "w") as file:
            json.dump([c.to_dict() for c in self.history], file, indent=4)

    def convert(self):
        try:
            amount = float(input("Enter amount: "))
            from_cur = input("From (USD/INR/EUR/GBP): ").upper()
            to_cur = input("To (USD/INR/EUR/GBP): ").upper()
            if from_cur not in self.rates or to_cur not in self.rates:
                print("Invalid currency.")
                return
            result = round(amount / self.rates[from_cur] * self.rates[to_cur], 2)
            self.history.append(Conversion(from_cur, to_cur, amount, result))
            self.save_history()
            print(f"{amount} {from_cur} = {result} {to_cur}")
        except ValueError:
            print("Invalid amount.")

    def view_history(self):
        if not self.history:
            print("No conversions yet.")
            return
        print("\n📜 Conversion History:")
        for h in self.history:
            print(f"{h.amount} {h.from_currency} → {h.result} {h.to_currency}")

def main():
    converter = CurrencyConverter()
    while True:
        print("\n=== Currency Converter ===")
        print("1. Convert")
        print("2. View History")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            converter.convert()
        elif choice == "2":
            converter.view_history()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()