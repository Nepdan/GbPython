earnings = int(input("Введите выручку: "))
costs = int(input("Введите издержки: "))

if earnings > costs:
    print("Прибыль - выручка больше издержек")
    profit = earnings - costs
    rent = profit/earnings
    print(rent)
    employeeNumber = int(input("Введите число сотрудников: "))
    employeeProfit = profit / employeeNumber
    print(employeeProfit)
else:
    print("Убыток - издержки больше выручки")

