my_file = open('my_f.txt', 'w')
line = input('Введите текст:\n')
while line:
    line += '\n'
    my_file.writelines(line)
    line = input('Введите текст:\n')
    if not line:
        break
my_file.close()

my_file = open('my_f.txt')
my_text = my_file.readlines()
for line in my_text:
    print(line.strip())
my_file.close()


with open('test.txt', 'w') as f:
    while True:
        line = input('Р’РІРµРґРёС‚Рµ СЃС‚СЂРѕРєСѓ: ')
        if line == '':
            break
        f.write(line + '\n')
