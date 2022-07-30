class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books_storage = []

    def find_book(self, title):
        try:
            return [book for book in self.books_storage if book.title == title][0]
        except IndexError:
            return f'There is no book named {title} in this library'
