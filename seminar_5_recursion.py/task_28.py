# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2 ---> 4

from random import randint

def total(a, c, b):
    summa = 0
    if c <= 0:
        return summa + b
    summa += a[0]
    a.pop(0)
    return summa + total(a, c - 1, b)

array_size = int(input("массив: "))
my_array = []
for _ in range(array_size):
    my_array.append(randint(0,5))
print(my_array)

number = int(input("число: "))

print(total(my_array, array_size, number))