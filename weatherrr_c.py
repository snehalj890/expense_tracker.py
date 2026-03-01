import json
import os

class WeatherEntry:
    def __init__(self, date, temperature, humidity, description):
        self.date = date
        self.temperature = temperature
        self.humidity = humidity
        self.description = description

    def to_dict(self):
        return {
            "date": self.date,
            "temperature": self.temperature,
            "humidity": self.humidity,
            "description": self.description
        }

class WeatherLogger:
    def __init__(self, filename="weather.json"):
        self.filename = filename
        self.entries = self.load_entries()

    def load_entries(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [WeatherEntry(**e) for e in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_entries(self):
        with open(self.filename, "w") as file:
            json.dump([e.to_dict() for e in self.entries], file, indent=4)

    def add_entry(self):
        date = input("Date (YYYY-MM-DD): ")
        try:
            temp = float(input("Temperature (°C): "))
            hum = float(input("Humidity (%): "))
        except ValueError:
            print("Invalid number.")
            return
        desc = input("Description: ")
        self.entries.append(WeatherEntry(date, temp, hum, desc))
        self.save_entries()
        print("✅ Entry added!\n")

    def view_entries(self):
        if not self.entries:
            print("No weather data yet.")
            return
        for e in self.entries:
            print(f"{e.date}: {e.temperature}°C, {e.humidity}%, {e.description}")

def main():
    logger = WeatherLogger()
    while True:
        print("\n=== Weather Logger ===")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            logger.add_entry()
        elif choice == "2":
            logger.view_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()