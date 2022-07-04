from project.library import Library
from project.user import User


class Registration:
    def add_user(self, user: User, library: Library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library):
        current_user = None
        for u in library.user_records:
            if u.user_id == user_id:
                current_user = u
        if current_user is not None and new_username != current_user.username:
            library.user_records.remove(current_user)

            if current_user.username in library.rented_books:
                old_value = library.rented_books.pop(current_user.username)
                current_user.username = new_username
                library.rented_books[current_user.username] = old_value
            current_user.username = new_username
            library.user_records.append(current_user)
            return f"Username successfully changed to: {new_username} for user id: {user_id}"

        elif current_user is not None and new_username == current_user.username:
            return f"Please check again the provided username - it should be different than the username used so far!"
        elif current_user is None:
            return f"There is no user with id = {user_id}!"
