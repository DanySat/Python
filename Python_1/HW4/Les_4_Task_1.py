massif = ["ДаблКилл...", "ТриплКилл...", "КвадраКилл...", "ПентаКилл...", "ГЕКСАКИЛЛ!", "ЧоГатушка!"]

a = 0

print('\n' * 1, 'Четные:', '\n' * 1)
while a < len(massif):
    print(massif[a],)
    a += 2

print('\n' * 1, 'Нечётные:', '\n' * 1)
for b in range(1, len(massif), 2):
    print(massif[b])
