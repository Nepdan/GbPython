rating = [9, 7, 6, 3, 1]
print(f"Рейтинг - {rating}")
a = int(input("Введите число: "))

for i in range(len(rating)):
    if rating[i] == a:
        rating.insert(i, a)
        break
    elif rating[0] < a:
        rating.insert(0, a)
        break
    elif rating[-1] > a:
        rating.append(a)
        break
    elif rating[i] > a and rating[i + 1] < a:
        rating.insert(i + 1, a)
        break
print(rating)