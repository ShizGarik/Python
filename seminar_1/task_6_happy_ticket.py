# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

ticket = 123456

numberOne = ticket // 1000
numberTwo = ticket % 1000

ticketOne = numberOne // 100
ticketTwo = (numberOne // 10) % 10
ticketThree = numberOne % 10
numberOne = ticketOne + ticketTwo + ticketThree

ticketOne = numberTwo // 100
ticketTwo = (numberTwo // 10) % 10
ticketThree = numberTwo % 10
numberTwo = ticketOne + ticketTwo + ticketThree

if numberOne == numberTwo:
    print('Счастливый номер')
else:
    print('Не повесло, покатайся еще')
