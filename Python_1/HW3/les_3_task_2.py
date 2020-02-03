text = str(input('Введи строку текста: '))
i = 0
capital = 0
lowercase = 0
other = 0
while i < len(text):
    if text[i].isupper() == True:
        capital += 1
    elif text[i].islower() == True:
        lowercase += 1
    else:
        other += 1
    i += 1

print('Длина строки равна: ', len(text))
print('Строчных букв: ', lowercase)
print('Прописных букв: ', capital)

