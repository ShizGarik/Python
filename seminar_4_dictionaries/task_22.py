# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint

def Multi_array(array, element):
    array = []
    for _ in range(element):
        array.append(randint(0, 5))
    return array

n_element = int(input("Кол-во элементов первого множества: "))
m_element = int(input("Кол-во элементов второго множества: "))
# Два пустых массива для добавления рандомных чисел
my_dict_n = [] 
my_dict_m = []
# Присвоение массива с числами
my_dict_n = Multi_array(my_dict_n, n_element)
my_dict_m = Multi_array(my_dict_m, m_element)
print(my_dict_n)
print(my_dict_m)
# Преобразование массива в список и вывод без повторений в порядке возрастания
my_dict_m = set(my_dict_m)
my_dict_n = set(my_dict_n)
print(*my_dict_n.intersection(my_dict_m))

