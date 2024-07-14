class Book:
    def __init__(self, title, authors, ISBN, publishing_year, price, quantity):
        self.title = title
        self.authors = authors  # This should be a list of author names
        self.ISBN = ISBN
        self.publishing_year = publishing_year
        self.price = float(price)
        self.quantity = quantity

    def __str__(self):
        return (f"Title: {self.title}, Authors: {', '.join(self.authors)}, "
                f"ISBN: {self.ISBN}, Year: {self.publishing_year}, "
                f"Price: ${self.price:.2f}, Quantity: {self.quantity}")

    def __repr__(self):
        return self.__str__()
