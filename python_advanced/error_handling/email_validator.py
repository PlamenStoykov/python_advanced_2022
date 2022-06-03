class NameTooShortError(Exception,):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


domains = ['.com', '.bg', '.org', '.net']
email = input()
while email != 'End':
    condition = False
    for i in domains:
        if i in email:
            condition = True
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(email[:email.index('@')]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif not condition:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print('Email is valid')
    email = input()



