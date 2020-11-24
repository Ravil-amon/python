# Месяцы и времена года.
# Словарь.
month = int(input('Введите номер месяца: '))
times_year = {
    1: 'Winter',
    2: 'Winter',
    12: 'Winter',
    3: 'Spring',
    4: 'Spring',
    5: 'Spring',
    6: 'Summer',
    7: 'Summer',
    8: 'Summer',
    9: 'Autumn',
    10: 'Autumn',
    11: 'Autumn'
}
print(times_year.get(month))
