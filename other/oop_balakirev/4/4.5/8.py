from abc import ABC, abstractmethod


class CountryInterface(ABC):

    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def population(self):
        pass

    @property
    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def get_info(self):
        pass


class Country(CountryInterface):
    def __init__(self, name_c, population, square):
        self._name = name_c
        self._population = population
        self._square = square

    @property
    def name(self):
        return self._name

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, arg):
        self._population = arg

    @property
    def square(self):
        return self._square

    @square.setter
    def square(self, value):
        self._square = value

    def get_info(self):
        return f"{self._name}: {self._square}, {self._population}"

