a = int(input('Введите число: '))

if a % 3 != 0 and a % 7 == 0 and a % 10 == 0:
    print('Верно')
else:
    print('Неверно')