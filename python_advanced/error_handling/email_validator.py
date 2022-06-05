from errors import MustContainAtSymbolError, NameTooShortError, InvalidDomainError

domains = ['com', 'bg', 'org', 'net']
email = input()
while email != 'End':
    tokens = email.split('@')
    domain_ending = tokens[-1].split('.')[-1]
    if len(tokens) != 2:
        raise MustContainAtSymbolError("Email must contain @")
    elif len(tokens[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif domain_ending not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    else:
        print('Email is valid')
    email = input()
