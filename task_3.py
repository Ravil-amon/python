with open('salary.txt') as my_f:
    sal = []
    poor = []
    my_list = my_f.read().split('\n')
    for i in my_list:
        print(i)
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}.\nCредний оклад {sum(map(float, sal)) / len(sal):.2f}')
