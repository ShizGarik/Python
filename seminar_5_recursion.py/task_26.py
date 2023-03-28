# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def degree_func(num, degree):
    if degree <= 0:
        return 1
    return num * degree_func(num, degree - 1)

number = int(input("Число: "))
degree = int(input("Степень: "))

print(degree_func(number, degree))