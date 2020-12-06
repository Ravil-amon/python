class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.surname} {self.name}.\nЗанимаемая должность: {self.position}.')

    def get_total_income(self):
        sal = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход: {sal}')


pos = Position('Иван', 'Иванов', 'директор', 50000, 70000)
pos.get_full_name()
pos.get_total_income()
