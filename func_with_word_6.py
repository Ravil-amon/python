def int_func(wd):
    return wd.title()


print(int_func('king'))

str_word = ['skrin sudocu wudu function gippopotam']
result = list(map(int_func, str_word))
print(result)
