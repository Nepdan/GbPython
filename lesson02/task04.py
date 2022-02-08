wordsString = input("Введите слова: ").split()
i = 1

for word in wordsString:
    print(f"{i}. {word[0:10]}")
    i += 1