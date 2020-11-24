# Структура данных "Товары".
while True:
    print('Выбрать действие: "add" или "exit".')
    action = input(": ")
    tup = tuple()
    wares = []
    d = {}

    if action == 'add':
        count = 1
        print('Введите название товара')
        name = input(': ')
        d['название'] = name
        print('Введите цену')
        price = input(': ')
        d['цена'] = price
        print('Введите количество товара')
        quantity = input(': ')
        d['количество'] = quantity
        print('Введите единицы товара')
        unit = input(': ')
        d['единицы'] = unit

        d = f'{count},{d}'
        wares.append(d)
        print(wares)
        count += 1  # count не работает, дальше мысль не идёт...

    elif action == 'exit':
        break
    else:
        print('Error!!')
print()
