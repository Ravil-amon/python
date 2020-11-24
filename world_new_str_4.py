# Ввод пронумерованных слов с новой строки.
datt = []
datt = input('Ввести слова через пробел: ')
dat = datt.split()
for num, val in enumerate(dat, 1):
    print(str(num) + str(val[:10]))  # Ограничение слова 10 букв.
