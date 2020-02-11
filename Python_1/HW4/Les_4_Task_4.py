Nick_Names = input('Введи имена через пробел: ')
Names = Nick_Names.split()

e = 1
worlds = []

for i in range(len(Names)):
    if Names[e[1]] in 'ауыояиюеё':
        worlds.append(Names[e])
        e += 1
print(worlds.capitalize())
