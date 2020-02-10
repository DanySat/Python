true_password = '12345'
password = input('Введи пароль: ')
if password == true_password:
    print('Пароль принят')
    print('Это тоже блок для if')
    name = input('Как тебя зовут: ')
    if name == 'admin':
        print('Приветсвую тебя повелитель!!!')
    else:
        print('Привет обычный пользователь.')
else:
    print('Пароль неверный')
    print('Вызываю полицию! ' * 3)


print('А этот текст появляется всегда!!!')

