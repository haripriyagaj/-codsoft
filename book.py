contacts = {}  # Dictionary to store contacts
def manage_contacts():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contacts[name] = {
                "phone_number": phone_number,
                "email": email,
                "address": address,
            }
            print(f"{name} has been added to your contacts.")

        elif choice == "2":
            if not contacts:
                print("No contacts found.")
            else:
                print("Contact List:")
                for index, name in enumerate(contacts.keys(), start=1):
                    print(f"{index}. {name} - {contacts[name]['phone_number']}")

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            matching_contacts = {}

            for name, contact_info in contacts.items():
                if keyword.lower() in name.lower() or keyword in contact_info["phone_number"]:
                    matching_contacts[name] = contact_info

            if matching_contacts:
                print("Matching Contacts:")
                for index, name in enumerate(matching_contacts.keys(), start=1):
                    print(f"{index}. {name} - {matching_contacts[name]['phone_number']}")
            else:
                print("No matching contacts found.")

        elif choice == "4":
            name = input("Enter the name of the contact to update: ")
            if name in contacts:
                phone_number = input("Enter new phone number: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                contacts[name].update({
                    "phone_number": phone_number,
                    "email": email,
                    "address": address,
                })
                print(f"{name}'s contact information has been updated.")
            else:
                print(f"{name} not found in contacts.")

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            if name in contacts:
                del contacts[name]
                print(f"{name} has been deleted from contacts.")
            else:
                print(f"{name} not found in contacts.")

        elif choice == "6":
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

