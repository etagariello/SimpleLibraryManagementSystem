import tkinter as tk
from tkinter import messagebox, simpledialog

import members
import books


def register_member():
    # Call the function to register a member
    name = simpledialog.askstring("Input", "Enter your name:")
    if name:  # Check if the user provided a name (didn't press cancel)
        if name in members.library_members:
            messagebox.showwarning("Warning", "You are already a member!")

        else:
            members.register_member(name)
            messagebox.showinfo("Success!", "You have successfully become a member WOOOOOOOOOOO!")

    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


def borrow_book():
    # Call the function to borrow a book
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            borrowing_book = books.borrow_book(title, author)  # Using the function from books.py
            if borrowing_book == f'The book {title} has been borrowed.':
                messagebox.showinfo("Success", "Book borrowed successfully!")
            else:
                messagebox.showwarning("Warning", "Book borrowing failed. Either the book does not exist "
                                                  "or is already being borrowed.")

        else:
            messagebox.showwarning("Warning", "Book borrowing cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book borrowing cancelled. Title was not provided.")


def return_book():
    # Call the function to return a book
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            returning_book = books.return_book(title, author)  # Using the function from books.py
            if returning_book == f'The book {title} by {author} has been returned.':
                messagebox.showinfo("Success", "Book returned successfully!")
            else:
                messagebox.showwarning("Warning", "Book returning failed. Either the book does not exist "
                                                  "or is was never borrowed.")

        else:
            messagebox.showwarning("Warning", "Book returning cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book returning cancelled. Title was not provided.")


def display_books():
    # Call the function to display all books
    messagebox.showinfo("List of books", f"{books.library_books}")


def display_members():
    # Call the function to display all members
    messagebox.showinfo("List of members", f"{members.library_members}")


def add_book():
    """Capture details and add a book to the library."""
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")

        if author:  # Check if the user provided an author
            adding_book = books.add_book(title, author)  # Using the function from books.py

            if adding_book == f"Sorry, but we already have the book {title} by {author} and we don't accept extras.":
                messagebox.showwarning("Warning", "Book addition failed. Book already in library.")

            else:
                messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Warning", "Book addition cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book addition cancelled. Title was not provided.")


def find_book():
    title = simpledialog.askstring("Input", "Enter the book's title:")
    if title:  # Check if the user provided a title (didn't press cancel)
        author = simpledialog.askstring("Input", "Enter the book's author:")
        if author:  # Check if the user provided an author
            searching_book = books.find_book(title, author)  # Using the function from books.py
            if searching_book == f"We own the book {title} by {author}.":

                messagebox.showinfo("Success", "Book found successfully!")
            else:
                messagebox.showwarning("Warning", "Book search failed. The book does not exist.")

        else:
            messagebox.showwarning("Warning", "Book search cancelled. Author was not provided.")
    else:
        messagebox.showwarning("Warning", "Book search cancelled. Title was not provided.")


def find_member():
    name = simpledialog.askstring("Input", "Enter the name:")
    if name:  # Check if the user provided a name (didn't press cancel)
        if name in members.library_members:  # Check if the name is in the list
            messagebox.showinfo("Success", f"{name} is in the member list.")

        else:
            messagebox.showwarning("Sorry", f"No one of the members goes by the name {name}")
    else:
        messagebox.showwarning("Warning", "Member search cancelled. Name was not provided.")

def exit_program():
    root.destroy()

root = tk.Tk()
root.geometry("300x500")
root.title("Library Management System")

# Menu buttons
add_book_btn = tk.Button(root, text="Add a new book", command=add_book)
add_book_btn.pack(pady=10)

register_member_btn = tk.Button(root, text="Register a new member", command=register_member)
register_member_btn.pack(pady=10)

borrow_book_btn = tk.Button(root, text="Borrow a book", command=borrow_book)
borrow_book_btn.pack(pady=10)

return_book_btn = tk.Button(root, text="Return a book", command=return_book)
return_book_btn.pack(pady=10)

display_books_btn = tk.Button(root, text="Display all books", command=display_books)
display_books_btn.pack(pady=10)

display_members_btn = tk.Button(root, text="Display all members", command=display_members)
display_members_btn.pack(pady=10)

find_members_btn = tk.Button(root, text="Find member", command=find_member)
find_members_btn.pack(pady=10)

find_book_btn = tk.Button(root, text="Find book", command=find_book)
find_book_btn.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=exit_program)
exit_btn.pack(pady=10)

root.mainloop()
