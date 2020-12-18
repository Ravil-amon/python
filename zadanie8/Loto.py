import random


def numbers(count, min_count, max_count):
    row = []
    while len(row) < count:
        new = random.randint(min_count, max_count)
        if new in row:
            continue
        row.append(new)
    return row


class Card:
    def __init__(self):
        card = numbers(15, 1, 90)
        self.amount = []
        for i in range(0, 3):
            tmp = sorted(card[5 * i: 5 * (i + 1)])
            for _ in range(0, 4):
                index = random.randint(0, 9)
                tmp.insert(index, 0)
            self.amount += tmp

    def __str__(self):
        b = '--------------------------'
        card = ''
        for index, num in enumerate(self.amount):
            if num == 0:
                card += '  '
            elif num < 10:
                card += f'{str(num)}'
            else:
                card += str(num)
            if (index + 1) % 9 == 0:
                card += '\n'
            else:
                card += ' '
        return card + b


class Gamers:
    def __init__(self):
        self.man_card = Card()
        self.comp_card = Card()
        print(f'----- Ваша карточка ------\n{self.man_card}')

    def __str__(self):
        return f'-- Карточка компьютера ---\n{self.comp_card}'


game = Gamers()
print(game)
