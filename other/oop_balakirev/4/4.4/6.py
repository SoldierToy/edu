class Furniture:
    def __init__(self, name, weight):
        self._name = self.__verify_name(name)
        self._weight = self.__verify_weight(weight)

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

        return name

    def __verify_weight(self, weight):
        if not (isinstance(weight, int) or isinstance(weight, float)):
            raise TypeError('вес должен быть положительным числом')

        if weight <= 0:
            raise TypeError('вес должен быть положительным числом')

        return weight


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors

    def get_attrs(self):
        return tuple([x for x in self.__dict__])


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height

    def get_attrs(self):
        return tuple([x for x in self.__dict__])


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square

    def get_attrs(self):
        return tuple([x for x in self.__dict__])


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
