
def it_data(name, surname, year_of_birth, city_of_residence, email, tlf):
    print(
        f'Имя - {name}, фамилия - {surname}, год рождения - {year_of_birth}, '
        f'город проживания - {city_of_residence}, '
        f'email - {email}, телефон - {tlf}'
    )


it_data(name='Ivan', surname='Popov', year_of_birth=2000,
        city_of_residence='Rome',
        email='jjjff @ bk.ru', tlf=88333388499)
