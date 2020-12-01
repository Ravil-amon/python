from sys import argv
from itertools import count

for arg in argv:
    n = argv[1]
    for i in count(start=int(n), step=2):
        if i > 100:
            break
        print(i)

# Почему print два раза не понял.
