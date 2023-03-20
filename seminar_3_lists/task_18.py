# Требуется найти в массиве A[1..myArray] самый близкий по величине элемент к заданному числу numberArray.
# Пользователь в первой строке вводит натуральное число myArray – количество элементов в массиве.
# В последующих  строках записаны myArray целых чисел Ai. Последняя строка содержит число numberArray
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

myArray = int(input("На сколько большой хочешь массив?: ")) # колличество элементов  в массиве
array = []  # массив

for _ in range(myArray):        # заполнение массива случайными числами
    array.append(randint(0, 5)) # append это добавление числа в массив
print(array)

numberArray = int(input("Какое число интересует?: "))

min = abs(numberArray - array[0]) # для сравнения взял первое число 
index = 0    # для записиси близкого числа

for i in range(1, myArray): # прохожу по массиву
    count = abs(numberArray - array[i])
    if count < min:
            min = count
            index = i
print(f'Число {array[index]} наиболее близко по величине к числу {numberArray}')
