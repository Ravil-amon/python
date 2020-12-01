from functools import reduce


def my_f(num1, num2):
    return num1 * num2


b = list(range(100, 1001, 2))
print(b)
my_list = reduce(my_f, [el for el in range(100, 1001) if el % 2 == 0])
print(my_list)
