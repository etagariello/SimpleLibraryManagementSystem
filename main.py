import books
import members


def display_menu():
    print("\nLibrary Management System")
    print("----------------------------")
    print("1. Add a new book to the library.")
    print("2. Register a new library member.")
    print("3. Borrow a book.")
    print("4. Return a book.")
    print("5. Find a book.")
    print("6. Display all books.")
    print("7. Find a member.")
    print("8. Display all members.")
    print("9. Exit.")
    print("----------------------------")


def actions():
    while True:
        display_menu()

        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            added_title = input("Book name:")
            added_author = input("Author name:")
            added = books.add_book(added_title, added_author)  # Call function to add a new book
            print(added)

        elif choice == "2":
            registered_name = input("Name:")
            registered = members.register_member(registered_name)  # Call function to register a new member
            print(registered)

        elif choice == "3":
            borrow_title = input("Book name:")
            borrowed_author = input("Author name:")
            borrowed = books.borrow_book(borrow_title, borrowed_author)  # Call function to borrow a book
            print(borrowed)

        elif choice == "4":
            return_title = input("Book name:")
            returned_author = input("Author name:")
            returned = books.return_book(return_title, returned_author)  # Call function to return a book
            print(returned)

        elif choice == "5":
            find_title = input("Book name:")
            find_author = input("Author name:")
            found_book = books.find_book(find_title, find_author)  # Call function to display all books
            print(found_book)

        elif choice == "6":
            display_books = books.library_books  # Call function to display all members
            print(display_books)

        elif choice == "7":
            find_name = input("Name:")
            found_name = members.find_member(find_name)
            print(found_name)

        elif choice == "8":
            display_members = members.library_members
            print(display_members)

        elif choice == "9":
            print("Thank you for using the Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


actions()
