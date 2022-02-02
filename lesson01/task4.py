number = input("Введите число")
length = len(number)
k = 0

for i in number:
    if int(i) > int(k):
        k = i

print(k)