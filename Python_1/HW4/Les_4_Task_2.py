First_story = {'В.В.ПУТИН.': '\n Короткая история, как я встретил Президента и играл с ним в Пэйнтболл!'}
Second_story = {'ЭКЗОТИЧЕСКИЙ ОПЫТ!': '\n История о том, xто я приготовил что-то странное, но очень вкусное!.'}
Third_story = {'КУЛЬТУРНОУ ОБАГАЩЕНИЕ.': '\n Приключение по Шоколадным музеям Бельгии! Спойлер: Много сахара!'}

for key, value in First_story.items():

    print('\n' * 1, key)

    print(value)

print('  ' * 23)
print(' - ' * 23)

for key, value in Second_story.items():

    print('\n' * 1, key)

    print(value)

print('  ' * 23)
print(' - ' * 23)

for key, value in Third_story.items():

    print('\n' * 1, key)

    print(value)
