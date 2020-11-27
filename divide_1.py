try:
    def my_div(a, b):
        print(f'{a / b:.2f}')


    c = int(input('Введите число: '))
    d = int(input('Введите ещё одно число: '))
    my_div(c, d)
except ZeroDivisionError:
    print("Error! На 0 делить нельзя! <;=0")
