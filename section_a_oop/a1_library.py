class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

        self.book_status = "Available"
        self.borrower = None

    def borrow(self, member_name):
        if self.book_status == "Available":
            self.borrower = member_name
            self.book_status = "Borrowed"
            print(f"Book borrowed by: {self.borrower}")
        else:
            print(f"Book not available, borrowed by {self.borrower}")
    
    def return_book(self):
        if self.book_status == "Borrowed":
            self.book_status = "Available"
            print(f"Book returned by {self.borrower}")
            self.borrower = None
        else:
            print("Book is in stock")

    def display_status(self):
        if self.book_status == "Available":
            print(self.book_status)
        else:
            print(f"Book borrowed by {self.borrower}")

b1 = Book(101, "The Alchemist", "Paul Coehl")

# print(b1.book_id, b1.title, b1.author)
# b1.display_status()
# b1.borrow("Ashwin")
# b1.borrow("Akshay")
# b1.return_book()
# b1.display_status()
