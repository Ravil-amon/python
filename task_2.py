my_file = open('my_text.txt')
lines = 0
for l in my_file:
    lines += 1
    l = l.split()
    words = 0
    for d in l:
        words += 1
    print(f'Количество слов в строке - {words}')
print(f'Строк - {lines}')
my_file.close()

my_file = open('my_text.txt')
read_text = my_file.read()
words = read_text.split()
print(f'Общее количество слов - {len(words)}')
my_file.close()


with open('test.txt') as f:
    lines = f.readlines()
print('РљРѕР»РёС‡РµСЃС‚РІРѕ СЃС‚СЂРѕРє:', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} СЃС‚СЂРѕРєР° СЃРѕРґРµСЂР¶РёС‚ - {} СЃР»РѕРІ'.format(num_line, len(line.split())))
