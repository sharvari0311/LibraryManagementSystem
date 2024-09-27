class Library:
    def __init__(self):
        self.books = []

    def add_book(self, isbn, title, author, year):
        self.books.append({"isbn": isbn, "title": title, "author": author, "year": year, "borrowed": False})

    def available_books(self):
        return [book for book in self.books if not book["borrowed"]]
