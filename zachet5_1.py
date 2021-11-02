number = int(input("Введите натуральное число: "))
while number != 1:
    if number % 2 == 0:
        number //= 2
    elif number % 2 != 0:
        number = (number * 3 + 1) // 2

print(number)
