class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn}) - [{status}]"


class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"Success: {self.name} borrowed '{book.title}'.")
            return True
        print(f"Error: '{book.title}' is already borrowed.")
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            if book.return_book():
                self.borrowed_books.remove(book)
                print(f"Success: {self.name} returned '{book.title}'.")
                return True
        print(f"Error: {self.name} does not have '{book.title}' checked out.")
        return False

    def __str__(self):
        borrowed_titles = ", ".join([b.title for b in self.borrowed_books]) or "None"
        return f"Patron: {self.name} (ID: {self.patron_id}) | Borrowed: {borrowed_titles}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, title, author, isbn):
        if isbn not in self.books:
            new_book = Book(title, author, isbn)
            self.books[isbn] = new_book
            print(f"Library: Added '{title}' to the inventory.")
        else:
            print(f"Library: Book with ISBN {isbn} already exists.")

    def register_patron(self, name, patron_id):
        if patron_id not in self.patrons:
            new_patron = Patron(name, patron_id)
            self.patrons[patron_id] = new_patron
            print(f"Library: Registered patron {name} with ID {patron_id}.")
        else:
            print(f"Library: Patron ID {patron_id} is already registered.")

    def borrow_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)

        if not patron:
            print(f"Transaction Failed: Patron ID {patron_id} not found.")
            return
        if not book:
            print(f"Transaction Failed: Book with ISBN {isbn} not found.")
            return

        patron.borrow_book(book)

    def return_book(self, patron_id, isbn):
        patron = self.patrons.get(patron_id)
        book = self.books.get(isbn)

        if not patron:
            print(f"Transaction Failed: Patron ID {patron_id} not found.")
            return
        if not book:
            print(f"Transaction Failed: Book with ISBN {isbn} not found.")
            return

        patron.return_book(book)

    def display_info(self):
        print("\n--- Current Library Status ---")
        print("\nBooks Inventory:")
        if not self.books:
            print("  No books in the library.")
        for book in self.books.values():
            print(f"  - {book}")
        
        print("\nRegistered Patrons:")
        if not self.patrons:
            print("  No registered patrons.")
        for patron in self.patrons.values():
            print(f"  - {patron}")
        print("------------------------------\n")


if __name__ == "__main__":
    my_library = Library()

    while True:
        print("\n=== LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add a New Book")
        print("2. Register a New Patron")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Display Library Information")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            title = input("Enter book title: ").strip()
            author = input("Enter book author: ").strip()
            isbn = input("Enter book ISBN: ").strip()
            if title and author and isbn:
                my_library.add_book(title, author, isbn)
            else:
                print("Error: Fields cannot be empty.")

        elif choice == '2':
            name = input("Enter patron name: ").strip()
            patron_id = input("Enter patron ID: ").strip()
            if name and patron_id:
                my_library.register_patron(name, patron_id)
            else:
                print("Error: Fields cannot be empty.")

        elif choice == '3':
            patron_id = input("Enter patron ID: ").strip()
            isbn = input("Enter book ISBN to borrow: ").strip()
            if patron_id and isbn:
                my_library.borrow_book(patron_id, isbn)
            else:
                print("Error: Fields cannot be empty.")

        elif choice == '4':
            patron_id = input("Enter patron ID: ").strip()
            isbn = input("Enter book ISBN to return: ").strip()
            if patron_id and isbn:
                my_library.return_book(patron_id, isbn)
            else:
                print("Error: Fields cannot be empty.")

        elif choice == '5':
            my_library.display_info()

        elif choice == '6':
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number between 1 and 6.")