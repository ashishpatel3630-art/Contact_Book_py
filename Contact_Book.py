import json
import os

CONTACT_BOOK = "ContactBook.json"


def load_data():
    if os.path.exists(CONTACT_BOOK):
        with open(CONTACT_BOOK, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    with open(CONTACT_BOOK, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact(contacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts(contacts)
    print("✅ Contact Added Successfully")

def show_contacts(contacts):
    if not contacts:
        print("❌ No contacts found")
        return

    print("\n===== CONTACT LIST =====")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
        print("----------------------")


def update_contact(contacts):
    name = input("Enter name to update: ")

    if name in contacts:
        print("Leave blank if you don't want to change a field")

        phone = input("New Phone: ")
        email = input("New Email: ")

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email

        save_contacts(contacts)
        print("✅ Contact Updated")
    else:
        print("❌ Contact not found")


def delete_contact(contacts):
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("🗑️ Contact Deleted")
    else:
        print("❌ Contact not found")


def main():
    contacts = load_data()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            show_contacts(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid Choice")

if __name__ == "__main__":
    main()