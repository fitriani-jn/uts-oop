# Definisi class Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False     # Protected attribute
        self.__isbn = isbn              # Private attribute

    # Public method untuk menampilkan informasi buku
    def display_info(self):
        status = "Checked Out" if self._is_checked_out else "Available"
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.__isbn}, Status: {status}")

    # Public method untuk meminjam buku
    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    # Public method untuk mengembalikan buku
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not checked out.")

# Definisi class LibraryMember
class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name                # Public attribute
        self.member_id = member_id      # Public attribute
        self._checked_out_books = []    # Protected attribute

    # Public method untuk meminjam buku
    def borrow_book(self, book):
        book.check_out()
        if book._is_checked_out:  # Mengakses protected attribute
            self._checked_out_books.append(book)

    # Public method untuk mengembalikan buku
    def return_book(self, book):
        book.return_book()
        if not book._is_checked_out:  # Mengakses protected attribute
            self._checked_out_books.remove(book)

    # Public method untuk menampilkan informasi anggota
    def display_member_info(self):
        print(f"Member Name: {self.name}, Member ID: {self.member_id}, Checked Out Books: {[book.title for book in self._checked_out_books]}")

# Membuat objek dari class Book
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
book2 = Book("1984", "George Orwell", "9780451524935")

# Membuat objek dari class LibraryMember
member1 = LibraryMember("Alice", "M001")

# Menampilkan informasi buku
book1.display_info()
book2.display_info()

# Anggota meminjam buku
member1.borrow_book(book1)
member1.borrow_book(book2)

# Menampilkan informasi anggota
member1.display_member_info()

# Mengembalikan buku
member1.return_book(book1)

# Menampilkan informasi buku setelah pengembalian
book1.display_info()
book2.display_info()

# Menampilkan informasi anggota setelah pengembalian
member1.display_member_info()