# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
import random as r

n = r.randint(1, 100)
result = 1
arr = []
for i in range(1, n):
    if result < n:
        arr.append(result)
        result = 2 ** i

print(f"{n} -> {arr}")