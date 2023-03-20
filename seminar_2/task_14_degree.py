# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N

from random import randint

num = randint(2, 16)   # Потолок возводимых в степень чисел
degree = 2             # Число возводимое в степень i
res = 0
print(num)

for i in range(num):
    res = degree**i

    if res <= num:
        print(res, end=" | ")
