class ContactManager:
    def __init__(self):
        self.contacts = {}

    def menu(self):
        print("\nContact Management System")
        print("1. Add New Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update an existing Contact")
        print("5. Delete a Contact")
        print("6. Exit The contact List")

    def add(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        address = input("Enter address: ")

        self.contacts[name] = {
            "Phone": phone,
            "Email": email,
            "Address": address
        }
        print("Contact added successfully!")

    def view(self):
        print("\nContact List:")
        for name, details in self.contacts.items():
            print(f"{name}: {details['Phone']}")

    def search(self):
        query = input("Enter name or phone number to search: ").lower()
        found = False

        for name, details in self.contacts.items():
            if query in name.lower() or query in details["Phone"]:
                found = True
                print(f"\n{name}'s Contact Details:")
                print(f"Phone: {details['Phone']}")
                print(f"Email: {details['Email']}")
                print(f"Address: {details['Address']}")
                break

        if not found:
            print("Contact not found.")

    def update(self):
        name = input("Enter the name of the contact to update: ")

        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            address = input("Enter new address: ")

            self.contacts[name] = {
                "Phone": phone,
                "Email": email,
                "Address": address
            }
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete(self):
        name = input("Enter the name of the contact to delete: ")

        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter What is needed to be done(1-6): ")

            if choice == "1":
                self.add()
            elif choice == "2":
                self.view()
            elif choice == "3":
                self.search()
            elif choice == "4":
                self.update()
            elif choice == "5":
                self.delete()
            elif choice == "6":
                print("Exiting Contact Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    contact_manager = ContactManager()
    contact_manager.run()
