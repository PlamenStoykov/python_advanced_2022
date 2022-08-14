from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user(self, username):
        for u in self.users_collection:
            if u.username == username:
                return u

    def __is_owner(self, user, movie):
        if movie.owner == user:
            return True
        return False

    def register_user(self, username: str, age: int):
        current_user = self.__find_user(username)
        if current_user is not None:
            raise Exception("User already exists!")
        current_user = User(username, age)
        self.users_collection.append(current_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if user not in self.users_collection:
            raise Exception("This user does not exist!")
        if not self.__is_owner(user, movie) and user != None:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.__find_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not self.__is_owner(user, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == 'title':
                movie.title = value
            elif key == 'year':
                movie.year = value
            else:
                movie.age_restriction = value
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if not self.__is_owner(user, movie):
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if self.__is_owner(user, movie):
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        message = ''
        for m in list(sorted_movies):
            message += f'{m.details()}\n'
        return message.strip()

    def __str__(self):
        message = ''
        if not self.users_collection:
            message += "All users: No users.\n"
        else:
            message += f"All users: {', '.join([u.username for u in self.users_collection])}\n"
        if not self.movies_collection:
            message += "All movies: No movies."
        else:
            message += f"All movies: {', '.join([m.title for m in self.movies_collection])}"
        return message.strip()
