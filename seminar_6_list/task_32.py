# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

print("Ввод через пробел!")
start, finish = list(map(int,input("Диапазон: ").split()))
print(start, finish)

size_array = 15
array = [randint(-10, 10) for _ in range(size_array)]
print(array)

# my_array = []
for i in range(size_array):
    if start <= array[i] <= finish:
        print(i, end=" ")
# print(*my_array)