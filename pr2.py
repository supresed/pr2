import calendar
year = int(input("Укажите год: "))
result = 0;
for i in range(1, 13):
    daysInMonth = calendar.monthrange(year, i)[1]
    for j in range(1, daysInMonth+1):
        num1 = int(j/10)
        num2 = int(j%10)
        result += num1 + num2
print(result)
    