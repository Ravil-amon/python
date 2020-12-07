import json

income = {}
incomes = 0
average_income = 0
i = 0
with open('f_task_7.txt') as file:
    for line in file:
        name, firm, proceeds, costs = line.split()
        income[name] = float(proceeds) - float(costs)
        if income.setdefault(name) >= 0:
            incomes = incomes + income.setdefault(name)
            i += 1
    print(f'Прибыль каждой компании - {income}')
    if i != 0:
        average_income = incomes / i
        print(f'Средняя прибыль - {average_income:.2f}')

with open('f_task_7.json', 'w') as write_js:
    json.dump(income, write_js)
    js_str = json.dumps(income)  # Создан файл с расширением json.
