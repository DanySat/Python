word = str(input("Введи строку текста:"))

# вариант 1 (через индексы)
length_word = len(word)
length_word = length_word - 1
i = 0
k = 0
while length_word - i >= i:
    if word[length_word - i] == word[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
    print(f"{word} обычное")
else:
    print(f"{word} палиндром")

# вариант 2 (переворачиваем слово и сравниваем)
mirror = word[::-1]
if word == mirror:
    print(f"{word} палиндром")
else:
    print(f"{word} обычное")