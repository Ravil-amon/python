def my_func(x, y):
    y += 1
    for i in range(y, 0):
        x = x * x
        y += 1
    return 1 / x


print(my_func(2, -2))
print(my_func(2, -3))
print(my_func(2, -4))
print(my_func(2, -8))
