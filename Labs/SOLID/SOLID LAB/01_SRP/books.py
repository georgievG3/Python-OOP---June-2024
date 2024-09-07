#ex_1
# class Book:
#     def __init__(self, title, author, location):
#         self.title = title
#         self.author = author
#         self.location = location
#         self.page = 0
#
#     def turn_page(self, page):
#         self.page = page
#
#SOLUTION
from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def get_book(self, title):

        try:
            book = [b for b in self.books if b.title == title][0]
            return book
        except IndexError:
            return "Sorry, book not found"

    def remove_book(self, title):

        for b in self.books:
            if b.title == title:
                del b


library = Library()
for num in range(1, 6):
    b = Book(f"Title{num}", f"Author{num}")
    library.add_book(b)
