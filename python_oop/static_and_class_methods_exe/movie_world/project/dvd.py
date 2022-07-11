class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.age_restriction = age_restriction
        self.creation_month = creation_month
        self.creation_year = creation_year
        self.name = name
        self.id = id
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        months_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
                       9: 'September', 10: 'October', 11: 'November', 12: 'December'}
        tokens = date.split('.')
        month = months_dict[int(tokens[1])]
        year = int(tokens[2])
        return cls(name, id, year, month, age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
