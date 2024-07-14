import json
from library import Library
from book import Book

def save_books(library, filename):
    data = {
        'books': [{
            'title': book.title,
            'authors': book.authors,
            'ISBN': book.ISBN,
            'publishing_year': book.publishing_year,
            'price': book.price,
            'quantity': book.quantity
        } for book in library.books],
        'lent_books': {book.title: borrowers for book, borrowers in library.lent_books.items()}
    }
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_books(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    library = Library()
    for book_data in data['books']:
        book = Book(book_data['title'], book_data['authors'], book_data['ISBN'],
                    book_data['publishing_year'], book_data['price'], book_data['quantity'])
        library.books.append(book)
    for book_title, borrowers in data['lent_books'].items():
        for book in library.books:
            if book.title == book_title:
                library.lent_books[book] = borrowers
    return library
