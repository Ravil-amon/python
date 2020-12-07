file = open('tex_f.txt', 'w')
line = input('Введите цифры через пробел\n: ')
file.write(line)
file.close()

f = open('tex_f.txt')
my_num = line.split()
print(sum(map(int, my_num)))
file.close()
