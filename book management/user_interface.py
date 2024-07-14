from library import Library
from book import Book

class UserInterface:
    def __init__(self):
        self.library = Library()
        self.library.load_from_file()

    def display_menu(self):
        print("\nWelcome to the Book Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Books")
        print("4. Search Books by Author")
        print("5. Remove Book")
        print("6. Lend Book")
        print("7. Return Book")
        print("8. View Lent Books")
        print("9. Exit")

    def handle_user_input(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.library.view_books()
            elif choice == '3':
                self.search_books()
            elif choice == '4':
                self.search_books_by_author()
            elif choice == '5':
                self.remove_book()
            elif choice == '6':
                self.lend_book()
            elif choice == '7':
                self.return_book()
            elif choice == '8':
                self.view_lent_books()
            elif choice == '9':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_book(self):
        title = input("Enter title: ")
        authors = input("Enter authors (comma separated): ").split(',')
        ISBN = input("Enter ISBN: ")
        publishing_year = input("Enter publishing year: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        book = Book(title, authors, ISBN, publishing_year, price, quantity)
        self.library.add_book(book)

    def search_books(self):
        term = input("Enter search term (title or ISBN): ")
        results = self.library.search_books(term)
        for book in results:
            print(book)

    def search_books_by_author(self):
        author = input("Enter author name: ")
        results = self.library.search_books_by_author(author)
        for book in results:
            print(book)

    def remove_book(self):
        term = input("Enter search term (title or ISBN): ")
        self.library.remove_book(term)

    def lend_book(self):
        term = input("Enter search term (title or ISBN): ")
        borrower = input("Enter borrower's name: ")
        self.library.lend_book(term, borrower)

    def return_book(self):
        term = input("Enter search term (title or ISBN): ")
        borrower = input("Enter borrower's name: ")
        self.library.return_book(term, borrower)

    def view_lent_books(self):
        for book, borrowers in self.library.lent_books.items():
            print(f"{book} lent to {', '.join(borrowers)}")
