# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = 123

numberOne = number // 100
numberTwo = (number // 10) % 10
numberThree = number % 10

print(numberOne + numberTwo + numberThree)