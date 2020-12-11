from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    def fabric(self):
        self.fabric_coat = self.v / 6.5 + 0.5
        print(f'{self.fabric_coat:.2f}')


class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    def fabric(self):
        self.fabric_costume = 2 * self.h + 0.3
        print(f'{self.fabric_costume:.2f}')


class Expense:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    @property
    def expen(self):
        print(str(f'Расход ткани: {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3):.2f}'))


coat = Coat(60)
coat.fabric()

cos = Costume(180)
cos.fabric()

exp = Expense(60, 180)
exp.expen
