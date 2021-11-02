a = (input('Введите трехзначное число: '))
number = [int(d) for d in a]
mul_number = number[0] * number[1] * number[2]

if mul_number < int(a):
    print('произведение меньше числа')
else:
    print('произведение больше числа')

if sum(number) % 5 == 0:
    print('сумма цифр кратна 5')
else:
    print('сумма цифр не кратна 5')