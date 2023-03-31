# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# 7 2 5
# 7 9 11 13 15
# el, step, quantity 

# el, step, quantity  = int(input("Первый элемент: ")), int(input("Шаг: ")), int(input("Размер массива: "))
print("Ввод через пробел!")
el, step, quantity = list(map(int,input("Первый элемент, шаг, размер массива: ").split()))
print(el, step, quantity )

my_array = []

while quantity > 0:
    my_array.append(el)
    el += step
    quantity -= 1
print(my_array)
