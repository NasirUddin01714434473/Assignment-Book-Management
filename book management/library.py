from book import Book

class Library:
    def __init__(self):
        self.books = []
        self.lent_books = {}

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()

    def view_books(self):
        for book in self.books:
            print(book)

    def search_books(self, term):
        results = [book for book in self.books if term in book.title or term in book.ISBN]
        return results

    def search_books_by_author(self, author):
        results = [book for book in self.books if author in book.authors]
        return results

    def remove_book(self, term):
        book_to_remove = None
        for book in self.books:
            if term in book.title or term in book.ISBN:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_to_file()
        else:
            print("This book isn’t available to remove.")

    def lend_book(self, term, borrower):
        for book in self.books:
            if term in book.title or term in book.ISBN:
                if book.quantity > 0:
                    book.quantity -= 1
                    if book not in self.lent_books:
                        self.lent_books[book] = []
                    self.lent_books[book].append(borrower)
                    self.save_to_file()
                    return
                else:
                    print("Not enough books available to lend.")
                    return
        print("This book isn’t available to lend.")

    def return_book(self, term, borrower):
        for book, borrowers in self.lent_books.items():
            if term in book.title or term in book.ISBN:
                if borrower in borrowers:
                    book.quantity += 1
                    borrowers.remove(borrower)
                    self.save_to_file()
                    return
        print("Book not found in lent books or incorrect borrower.")

    def save_to_file(self):
        from storage import save_books
        save_books(self, 'library_data.txt')

    def load_from_file(self):
        from storage import load_books
        loaded_library = load_books('library_data.txt')
        self.books = loaded_library.books
        self.lent_books = loaded_library.lent_books
