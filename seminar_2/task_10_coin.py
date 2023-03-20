# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

coin = randint(2,10)          # колличество монет
countTails = 0    # Решка
countEmblem = 0   # Герб

for _ in range(coin):
    a = randint(0,1)
    print(a, end=" | ")

    if a < 1:
        countTails += 1
    else:
        countEmblem += 1

if countEmblem < countTails:
    print(f"\nМонет с гербом меньше, переверните {countEmblem} монет")
else:
    print(f"\nМонет с решкой меньше, переверните {countTails} монет")
