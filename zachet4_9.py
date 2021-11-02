from random import randint

old_lst = [randint(-100, 100) for _ in range(10)]
new_lst = [d ** 2 if d % 2 == 0 else d * 2 for d in old_lst]

print(
    f"Старый массив - {old_lst}",
    f"Измененный массив - {new_lst}",
    sep="\n"
)
