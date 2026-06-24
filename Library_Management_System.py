class Library:
    def __init__(self):
        self.numBooks = 0
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.numBooks = len(self.books)

    def showInfo(self):
        print(f"The library has {self.numBooks} books. The books are:")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Harry Potter 1")
l1.addBook("Harry Potter 2")
l1.addBook("Harry Potter 3")
l1.addBook("Harry Potter 4")
l1.addBook("Harry Potter 5")
l1.showInfo()