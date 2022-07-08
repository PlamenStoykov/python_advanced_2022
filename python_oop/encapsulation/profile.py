class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) < 5 or len(value) > 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        upper = False
        digit = False
        for sign in value:
            if sign.isupper():
                upper = True
            elif sign.isdigit():
                digit = True
        if digit and upper and len(value) >= 8:
            self.__password = value
        else:
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
