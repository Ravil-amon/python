from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ['red', 'yellow', 'green']

    def running(self):
        for color in cycle(TrafficLight.__colors):
            sleep(2)
            if color == 'red':
                sleep(4)
            elif color == 'yellow':
                sleep(7)
            print(color)  # Предупреждение!!! Цикл бесконечный...


tl = TrafficLight()
tl.running()
