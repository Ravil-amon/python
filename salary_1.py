from sys import argv

for arg in argv:
    job_in_hour, rate_in_hour, bonus = argv[1:4]
    salary = (int(job_in_hour) * int(rate_in_hour)) + int(bonus)
print(f'Зарплата сотрудника: {salary}')
