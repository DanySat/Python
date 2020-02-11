while True:
    number = int(input("Введи целое число от 3 до 20: "))
    if 2 < number < 21:
        print('Пятикратное число равно: ' + str(number * 5))
        break
    else:
        print('Неверное число.')
        continue
