from capitalize import capitalize

if capitalize('hello') != 'Hello':
    raise Exception('Функия работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')
