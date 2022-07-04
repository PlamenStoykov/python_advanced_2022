from project.user import User


class Library:

    def __init__(self):
        self.user_records = []  # list of user objects
        self.books_available = {}  # author -> list of the available books
        self.rented_books = {}  # username -> {book_name:days to return the book}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.books_available[author]:
            self.rented_books[user.username] = {book_name: days_to_return}
            self.books_available[author].remove(book_name)
            user.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        # already rented
        return f'The book "{book_name}" is already rented and will be available in ' \
               f'{self.rented_books[user.username][book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User):
        if book_name in self.rented_books[user.username]:
            self.books_available[author].append(book_name)
            user.books.remove(book_name)
        else:
            return f"{user.username} doesn't have this book in his/her records!"
