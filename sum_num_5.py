my_mlist = (sum(map(int, input('Введите строку чисел через пробел: ').split())))
print(my_mlist)
while True:
    if input('Выход - q, или\nлюбая клавиша - продолжить ввод чисел:  ').upper() == 'Q':
        break
    num = sum(map(int, input(': ').split()))
    my_mlist = my_mlist + num
    print(my_mlist)
