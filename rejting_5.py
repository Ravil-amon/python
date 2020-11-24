# Реализуем структуру "Рейтинг".
my_list = [8, 8, 7, 5, 5, 5, 4, 3, 2, 2, 2]
print(my_list)
i = int(input('Введите число: '))
my_list.append(i)
my_list.sort()
my_list.reverse()
print(my_list)
