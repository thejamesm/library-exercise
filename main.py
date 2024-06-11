class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def titleAndAuthor(self):
        return f'"{self.title}" by {self.author}'

class Member:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.borrowedBooks = []
    
    def listBorrowedBooks(self):
        print(f"{self.name} is currently borrowing:")
        for book in self.borrowedBooks:
            print("    ", book.titleAndAuthor())

class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def addBook(self, title, author):
        newBook = Book(title, author)
        self.books.append(newBook)
        return newBook

    def addMember(self, id, name):
        newMember = Member(id, name)
        self.members.append(newMember)
        return newMember

    def checkoutBook(self, member, book):
        if book.available:
            member.borrowedBooks.append(book)
            book.available = False
            print(f"> {member.name} borrowed {book.title}")
            return True
        else:
            print(f"> {member.name} attempted to borrow {book.title}, but it is currently unavailable")
            return False

    def returnBook(self, member, book):
        if book in member.borrowedBooks:
            member.borrowedBooks.remove(book)
            book.available = True
            print(f"> {member.name} returned {book.title}")
            return True
        else:
            print(f"> {member.name} cannot return {book.title} because it is not currently in their possession")
            return False

    def listBooks(self):
        print("Available books:")
        for book in self.books:
            print("    ", book.titleAndAuthor())   
        print()

    def listMembers(self):
        print("Library members:")
        for member in self.members:
            print(f"    {member.id}: {member.name}")
        print()

myLibrary = Library()
member1 = myLibrary.addMember(1, "James")
member2 = myLibrary.addMember(2, "Muhammed")
book1 = myLibrary.addBook("Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = myLibrary.addBook("Lord of the Rings", "JRR Tolkein")
book3 = myLibrary.addBook("Gödel, Escher, Bach", "Douglas Hofstadter")

# Print book collection and member list
myLibrary.listBooks()
myLibrary.listMembers()

# Some test transactions
myLibrary.checkoutBook(member1, book1)
myLibrary.checkoutBook(member2, book2)
myLibrary.checkoutBook(member1, book2)
myLibrary.checkoutBook(member1, book3)
member1.listBorrowedBooks()
myLibrary.returnBook(member1, book1)
member1.listBorrowedBooks()
myLibrary.checkoutBook(member2, book1)
member2.listBorrowedBooks()