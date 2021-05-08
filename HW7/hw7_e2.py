import abc


class Products(abc.ABC):
    @abc.abstractmethod
    def get_coat_total(self):
        pass

    @abc.abstractmethod
    def get_suit_total(self):
        pass

    @abc.abstractmethod
    def get_total(self):
        pass


class Dress(Products):
    def __init__(self, s, h):
        self.coat_total = s / 6.5 + 0.5
        self.suit_total = h * 2 + 0.3
        self.all_total = self.coat_total + self.suit_total

    def get_coat_total(self):
        return f'Coat = {self.coat_total}'

    def get_suit_total(self):
        return f'Suit = {self.suit_total}'

    @property
    def get_total(self):
        return f'Total = {self.all_total}'


wear = Dress(14, 6)

print(wear.get_coat_total())
print(wear.get_suit_total())
print(wear.get_total)
