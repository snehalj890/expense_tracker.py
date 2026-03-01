import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    return [Contact(**c) for c in data]
            except json.JSONDecodeError:
                return []
        return []

    def save_contacts(self):
        with open(self.filename, "w") as file:
            json.dump([c.to_dict() for c in self.contacts], file, indent=4)

    def add_contact(self):
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        self.contacts.append(Contact(name, phone, email))
        self.save_contacts()
        print("Contact added!\n")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts yet.")
            return
        for idx, c in enumerate(self.contacts, start=1):
            print(f"{idx}. {c.name} | {c.phone} | {c.email}")

    def search_contact(self):
        query = input("Enter name to search: ").lower()
        found = [c for c in self.contacts if query in c.name.lower()]
        if not found:
            print("No contacts found.")
        for c in found:
            print(f"{c.name} | {c.phone} | {c.email}")

def main():
    book = ContactBook()
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            book.add_contact()
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            book.search_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()