class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):

        if isinstance(value, float):
            return cls(int(value))

        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        def roman_to_int(roman, values={'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}):
            """Convert from Roman numerals to an integer."""
            numbers = []
            for char in roman:
                numbers.append(values[char])
            total = 0
            for num1, num2 in zip(numbers, numbers[1:]):
                if num1 >= num2:
                    total += num1
                else:
                    total -= num1
            return total + num2

        return cls(roman_to_int(value))

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            if '.' not in value:
                return cls(int(value))
        return 'wrong type'


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
