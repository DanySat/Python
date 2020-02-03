while True:
    number = int(input("Введи число больше нуля и меньше десяти': "))
    if 0 < number < 10:
        print('Пятикратное число равно: ' + str(number * 5))
        break
    else:
        print('Неверное число.')
        continue
