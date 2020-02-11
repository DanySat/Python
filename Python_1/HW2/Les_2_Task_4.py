text = input('Введите текст: ')

a = text[1]
print(f'вторая с начала буква {a}')

b = text[-3]
print(f'третью с конца буква {b}')

print((text.replace(a, b)))
