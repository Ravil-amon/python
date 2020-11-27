def my_func(a, b, c):
    if a > b and a > c and b > c:
        print(a + b)
    elif a > b and a > c and c > b:
        print(a + c)
    else:
        print(b + c)


my_func(3, 2, 1)
my_func(3, 1, 2)
my_func(1, 2, 3)
