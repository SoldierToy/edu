class StringDigit(str):
    def __init__(self, string):
        self.check_str(string)
        self.string = string

    @staticmethod
    def check_str(string: str):
        if string.isdigit():
            return string
        else:
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other: str):
        self.check_str(other)
        return StringDigit(self.string + other)

    def __radd__(self, other: str):
        self.check_str(other)
        return StringDigit(other + self.string)


sd = StringDigit("123")
sd = sd + "456"  # StringDigit: 123456
sd = "789" + sd  # StringDigit: 789123456
sd = sd + "12f"  # ValueError
