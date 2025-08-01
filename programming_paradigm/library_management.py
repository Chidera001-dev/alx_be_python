class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_available(self):
        return not self._is_checked_out
    
    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title}")
                return
        print(f"Book not available: {title}")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book.title}")
                return
        print(f"Book not found or not checked out: {title}")

    def list_available_books(self):
        print("Available books: ")
        for book in self._available():
            if book.is_available():
                print(f"- {book.title} by {book.author}")
                
