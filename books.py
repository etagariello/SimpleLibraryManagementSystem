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

    return f"We either don't own the book {title} by {author} or it's currently already borrowed, sorry."



def return_book(title, author):
    for book in library_books: #repeat for every book
        if title == book['title'] and author == book["author"] and  book['availability'] == False: #check if it is in the library and if it is NOT available
            book['availability'] = True #make it false because they returned it
            return f'The book {title} by {author} has been returned.'

    return f"We either don't own the book {title} by {author} or it was never borrowed, sorry."


def find_book(title, author,):
    for book in library_books: #repeat for every book
        if title == book['title'] and author == book["author"] and book['availability']:
            return f"We own the book {title} by {author}."

    return f"We do not have this book, sorry."


