num = int(input('Введи целое число: '))
while num < 50:
    if num % 2 == 0:
        print(num)
    num = num + 1
print('Цикл завершён!')

num = int(input('Введи целое число: '))
while num < 50:
    num = num + 1
    if num % 2 != 0:
        continue
    print(num)
    print('continue снова не сработал')
print('Второй цикл завершён!')


num = int(input('Введи целое число: '))
while num < 50:
    num = num + 1
    if num == 13:
        break
    print(num)
print('Второй цикл завершён!')
