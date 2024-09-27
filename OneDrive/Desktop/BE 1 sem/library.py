class Library:
    def __init__(self):
        self.books = []

    def add_book(self, isbn, title, author, year):
        """Add a new book to the library."""
        self.books.append({"isbn": isbn, "title": title, "author": author, "year": year, "borrowed": False})

    def borrow_book(self, isbn):
        """Borrow a book from the library if it is available."""
        for book in self.books:
            if book["isbn"] == isbn:
                if not book["borrowed"]:
                    book["borrowed"] = True
                    return f'You have borrowed "{book["title"]}".'
                else:
                    return "This book is already borrowed."
        return "Book not found."

    def return_book(self, isbn):
        """Return a borrowed book to the library."""
        for book in self.books:
            if book["isbn"] == isbn:
                if book["borrowed"]:
                    book["borrowed"] = False
                    return f'You have returned "{book["title"]}".'
                else:
                    return "This book was not borrowed."
        return "Book not found."

    def available_books(self):
        """List all available books in the library."""
        return [book for book in self.books if not book["borrowed"]]

# Example usage
if __name__ == "__main__":
    library = Library()
    library.add_book("978-3-16-148410-0", "Book One", "Author A", 2020)
    library.add_book("978-1-234-56789-7", "Book Two", "Author B", 2021)

    print("Available books:", library.available_books())
    print(library.borrow_book("978-3-16-148410-0"))
    print("Available books after borrowing:", library.available_books())
    print(library.return_book("978-3-16-148410-0"))
    print("Available books after returning:", library.available_books())
