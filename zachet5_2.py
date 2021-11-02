n, y, x = map(int, input("Введите число километров, процент и количество дней: ").split())

summ = n
for i in range(x):
    summ += n * ((100 + y) // 100)

print(f"Суммарное количество километров - {summ}")
