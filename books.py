library_books: list = []

def add_book(title, author, availability = True): #adds books
     #create a dictionary for the book
    book = {"title": title, "author": author, "availability": availability}

     #add book to
    for existing_book in library_books:
        if title == existing_book['title'] and author == existing_book['author']:
            return f"Sorry, but we already have the book {title} by {author} and we don't accept extras."

    library_books.append(book)
    return f'The book {title} by {author} has been added to the library.'


def borrow_book(title, author):
    for book in library_books: #repeat for every book
        if title == book['title'] and author == book['author'] and book['availability']: #check if it is in the library and if it is available
            book['availability'] = False #make it false because they borrowed it+
            return f'The book {title} has been borrowed.'

        elif title != book['title'] and author != book['author']: #if not in library
            return f"There is no book named {title} by {author}."

        elif title == book['title'] and author == book['author'] and book['availability'] == False: #if in library but not available
            return f"There is a book named {title} by {author}, but it is not available."
            
               

def return_book(title, author):
    for book in library_books: #repeat for every book
        if title == book['title'] and author == book["author"] and  book['availability'] == False: #check if it is in the library and if it is NOT available
            book['availability'] = True #make it false because they returned it
            return f'The book {title} by {author} has been returned.'

        elif title != book['title'] and author != book["author"]: #if not in library
            return f"You're returning the book {title} by {author} to the wrong library, buddy."

        elif title == book['title'] and author == book["author"] and book['availability'] == True: #is available
            return f"We have the book {title} but it was never borrowed."


def find_book(title, author,):
    for book in library_books: #repeat for every book
        if title == book['title'] and author == book["author"] and book['availability']:
            return f"We own the book {title} by {author} and you are able to borrow it!"

        elif title == book['title'] and author == book["author"] and book['availability'] == False:
            return f"We own the book {title} by {author}, but someone is currently borrowing it. "

        elif title == book['title'] and author != book["author"]:
            return f"We own the book {title}, but it wasn't written by {author}."

        elif title != book['title'] and author == book["author"]:
            return f"We do not own the book {title}, but we do have other books by {author}."

        elif title != book['title'] and author != book["author"]:
            return f"We do not own the book {title} by {author}."

        
