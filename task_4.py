class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print(f'Текущая скорость - {self.speed}')

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина стоит')

    def turn(self):
        print('Машина повернула налево')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Ваша скорость - {self.speed}\nУменьшить скорость до 60 км/час')


class SportCar(Car):
    def sport(self):
        return self.speed, self.color, self.name, self.is_police


class WorkCar(Car):
    def show_speed(self):
        super(WorkCar, self).show_speed()
        if self.speed > 40:
            print(f'Ваша скорость - {self.speed}\nУменьшить скорость до 40 км/час')


class PoliceCar(Car):
    def police(self):
        return self.speed, self.color, self.name, self.is_police


ca = Car(80, 'red', 'Lada')
print(ca.name)
ca.turn()
ca.show_speed()

tc = TownCar(70, 'green', 'bus')
print(tc.name)
tc.go()
tc.show_speed()

sc = SportCar(120, 'murrey', 'ferrari')
print(sc.name)
sc.turn()
print(sc.sport())
print(sc.is_police)

pc = PoliceCar(0, 'yellow', 'mersedes', True)
print(pc.name)
print(pc.is_police)
pc.show_speed()
pc.stop()

wc = WorkCar(50, 'crimson', 'truck')
print(wc.name)
wc.go()
wc.show_speed()
