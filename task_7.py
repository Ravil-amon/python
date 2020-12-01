from math import factorial


def fact(n):
    k = factorial(n)
    yield k


for i in fact(4):
    print(i)

# Увы. Разложить факториал не смог.
