from math import hypot

kat_1 = int(input('Введите значение катета а: '))
kat_2 = int(input('Введите значение катета b: '))
hypot_ = int(input('Введите значение гипотенузы с: '))

otvet = (hypot(kat_1, kat_2))

    # 3 4 5
if hypot_ == otvet:
    print ('треугольник прямоугольный')
else:
    print ('неверно')
