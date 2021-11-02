zarplata_ = int(input('Зарплата: '))
staj_ = int(input('Стаж: '))
nadbavka2_5_ = zarplata_ * 0.02
nadbavka5_10_ = zarplata_ * 0.05

if staj_ in range(2, 6):
    summ1_ = nadbavka2_5_ + zarplata_
    print('Надбавка: ', nadbavka2_5_, 'Сумма к выплате: ', summ1_)
elif staj_ in range(5, 11):
    summ2_ = nadbavka5_10_ + zarplata_
    print('Надбавка: ', nadbavka5_10_, 'Сумма к выплате: ', summ2_)
else:
    pass