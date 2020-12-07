rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('num.txt') as file_obj:
    for line in file_obj:
        lines = line.split(' - ')
        print(lines)
        if lines[0] in rus:
            word = rus[lines[0]]
            new_file.append(word + ' - ' + lines[1])
    print(new_file)
file_write = open('num_new.txt', 'w')
file_write.writelines(new_file)
file_write.close()
