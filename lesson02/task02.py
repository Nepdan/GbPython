l = input("Введите значения списка через пробел: ").split()

for i in range(0, len(l), 2):
    if i + 1 == len(l):
        break
    else:
        l[i], l[i + 1] = l[i+1], l[i]
print(l)