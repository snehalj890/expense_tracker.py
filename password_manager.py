import json
import os

class Credential:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {"website": self.website, "username": self.username, "password": self.password}

class PasswordManager:
    def __init__(self, filename="passwords.json"):
        self.filename = filename
        self.credentials = self.load_credentials()

    def load_credentials(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Credential(**c) for c in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_credentials(self):
        with open(self.filename, "w") as file:
            json.dump([c.to_dict() for c in self.credentials], file, indent=4)

    def add_credential(self):
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")
        self.credentials.append(Credential(website, username, password))
        self.save_credentials()
        print("✅ Credential saved!\n")

    def view_credentials(self):
        if not self.credentials:
            print("No credentials yet.")
            return
        print("\n🔑 Saved Credentials:")
        for c in self.credentials:
            print(f"{c.website} | {c.username} | {c.password}")

def main():
    pm = PasswordManager()
    while True:
        print("\n=== Password Manager ===")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            pm.add_credential()
        elif choice == "2":
            pm.view_credentials()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()