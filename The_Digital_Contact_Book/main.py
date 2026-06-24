contact_book = {}

while True:
    choice = input("1. Add a Contact 2. View All Contacts 3. Exit Application: ")

    if choice == "1":

        name = input("Enter the name: ")
        number = input("Enter your 11-digit number: ")

        contact_book[name] = number
        print("Number saved successfully!")

    elif choice == "2":
        if not contact_book:
            print("No contact saved yet!")
        else:
            print(contact_book)

    elif choice == "3":
        print("Contact book closed")

    else:
        print("Invalid number choose 1-3")