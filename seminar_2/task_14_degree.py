# Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N

num = 16    # Потолок возводимых в степень чисел
degree = 2  # Число возводимое в степень i
res = 0

for i in range(num):
    res = degree**i
    
    if res <= num:
        print(res)
