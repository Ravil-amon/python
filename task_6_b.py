from sys import argv
from itertools import cycle


if "h" in argv:
    my_list = [True, 'ABC', 123, None]
    c = 0
    for el in cycle(my_list):
        if c > 7:
            break
        print(el)
        c += 1
