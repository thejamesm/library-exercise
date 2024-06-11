class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name, memberId):
        self.name = name
        self.memberId = memberId
        self.borrowedBooks = []

class Library:
    def checkoutBook(self, member, book):
        if book.available:
            member.borrowedBooks.append(book)
            book.available = False
            print(f"{member.name} borrowed {book.title}")
        else:
            print(f"{member.name} would like to borrow {book.title}, but it is currently unavailable")
    
    def returnBook(self, member, book):
        if book in member.borrowedBooks:
            member.borrowedBooks.remove(book)
            book.available = True
            print(f"{member.name} returned {book.title}")
        else:
            print(f"{book.title} not currently checked out by {member.name}")

myLibrary = Library()
member1 = Member("James", 1)
member2 = Member("Muhammed", 2)
book1 = Book("Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = Book("Lord of the Rings", "JRR Tolkein")
book3 = Book("Gödel, Escher, Bach", "Douglas Hofstadter")

# Some test actions
myLibrary.checkoutBook(member1, book1)
myLibrary.checkoutBook(member2, book2)
myLibrary.checkoutBook(member1, book2)
myLibrary.checkoutBook(member1, book3)
myLibrary.returnBook(member1, book1)
myLibrary.checkoutBook(member2, book1)