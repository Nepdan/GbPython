seasons_list = ["Зима", "Весна", "Лето", "Осень"]
seasons_dict = {1:"Зима", 2:"Весна", 3:"Лето", 4:"Осень"}
monthNumber = int(input("Введите номер месяца от 1 до 12: "))
if monthNumber ==1 or monthNumber == 12 or monthNumber == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif monthNumber == 3 or monthNumber == 4 or monthNumber ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif monthNumber == 6 or monthNumber == 7 or monthNumber == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif monthNumber == 9 or monthNumber == 10 or monthNumber == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])