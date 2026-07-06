# phone book
phonebook = {}   # Empty phonebook created when program starts
def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter contact number: ")
    phonebook[name] = number
    print(f"Contact '{name}' added successfully.\n")
def search_contact():
    name = input("Enter name to search: ")
    if name in phonebook:
        print(f"{name}'s number: {phonebook[name]}\n")
    else:
        print("Contact not found.\n")
def display_names():
    if phonebook:
        print("All contact names:")
        for name in phonebook:
            print(name)
        print()
    else:
        print("Phonebook is empty.\n")
def display_numbers():
    if phonebook:
        print("All contact numbers:")
        for num in phonebook.values():
            print(num)
        print()
    else:
        print("Phonebook is empty.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in phonebook:
        new_number = input("Enter new contact number: ")
        phonebook[name] = new_number
        print(f"Contact '{name}' updated successfully.\n")
    else:
        print("Contact not found.\n")
def delete_contact():
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact '{name}' deleted.\n")
    else:
        print("Contact not found.\n")
def delete_phonebook():
    phonebook.clear()
    print("All contacts deleted. Phonebook is now empty.\n")
def menu():
    while True:
        print("------- PHONEBOOK MENU --------")
        print("1. Add Contact")
        print("2. Search Contact by Name")
        print("3. Display All Contact Names")
        print("4. Display All Contact Numbers")
        print("5. Update Any Contact Number")
        print("6. Delete Any Contact")
        print("7. Delete Complete Phonebook")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_names()
        elif choice == '4':
            display_numbers()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            delete_phonebook()
        elif choice == '8':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
menu()


            



        



           
