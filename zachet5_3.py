num = int(input("Ввведите число: "))
chet_, nechet_ = 0, 0
while num != 0:
    p = num % 10
    if p % 2 == 0:
        chet_ += 1
    else:
        nechet_ += 1
    num //= 10
print(f"Количество четных - {chet_}\n"
      f"Количество нечетных - {nechet_}")