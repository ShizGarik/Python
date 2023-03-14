# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# Input: 5 6 
# Output: 2 3

from random import randint

a = randint(2,10)
b = randint(2,10)

sumNumbers = a + b      # Сумма чисел
productNumbers = a * b  # Произведение чисел
print(f"Подсказка!\nСумма чисел {sumNumbers}\nПроизведение чесел {productNumbers}\n")

answerSum = int(input("Отгадай первое число: "))
answerProduct = int(input("Отгадай второе число: "))

while answerSum != a or answerProduct != b:
    print("\033[A                          \033[A") # Для удаления 
    print("\033[A                          \033[A") # последних двух строчек
 
    answerSum = int(input("Отгадай первое число: "))
    answerProduct = int(input("Отгадай второе число: "))
print(f"Угадал! {answerSum} и {answerProduct}")